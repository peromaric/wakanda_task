import json
from eth_account import Account
from wakanda_api.module import Module
from typing import Optional, List
from web3 import Web3
import pathlib
import requests
from hexbytes import HexBytes
import asyncio
import time


class Web3Interactor(Module):
    def __init__(self, wakanda_api):
        super().__init__(wakanda_api)
        self.web3: Optional[Web3] = None
        self.candidate_data: Optional[dict] = None
        self.voter_list: list = []

        # Request and candidate data from API
        self.candidate_data = requests.get("https://wakanda-task.3327.io/list").json()

        # Get the contract data
        path_to_token_contract: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/WakandaERC20.json")
        path_to_voting_contract: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/WakandaVotingContract.json")
        path_to_deployed_contract_addresses: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/addresses.json")

        for attempt in range(30):
            try:
                token_contract_data: dict = self._read_and_parse_contract_json(path_to_token_contract)
                voting_contract_data: dict = self._read_and_parse_contract_json(path_to_voting_contract)
                deployed_contract_data: dict = self._read_and_parse_contract_json(path_to_deployed_contract_addresses)
            except IOError:
                print("Contract data still missing, reattempting to read from contracts.")
                time.sleep(10)

        # Fill provider and other web3 data
        self.w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        self.w3.eth.account = self.w3.eth.account \
            .privateKeyToAccount("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")

        self.token_contract = self.w3.eth.contract(
            address=deployed_contract_data["tokenContract"],
            abi=token_contract_data["abi"],
            bytecode=token_contract_data["bytecode"]
        )
        self.voting_contract = self.w3.eth.contract(
            address=deployed_contract_data["votingContract"],
            abi=voting_contract_data["abi"],
            bytecode=voting_contract_data["bytecode"]
        )

        # Generate candidate addresses and vote count fields
        for candidate in self.candidate_data["candidates"]:
            candidate["vote_count"] = 0
            candidate["rank"] = len(self.candidate_data["candidates"])
            candidate["address"] = Account.create().address
            asyncio.run(self.add_candidate(candidate["address"]))

    @staticmethod
    def _read_and_parse_contract_json(contract_path: pathlib.Path) -> Optional[dict]:
        contract_parsed: Optional[dict] = None

        with contract_path.open() as contract_json:
            contract_parsed = json.load(contract_json)

        return contract_parsed

    async def balance_of(self, address: str):
        balance = self.voting_contract.functions.balanceOf(address).call()
        return balance

    async def register_voter(self, voter_address: str):
        voter: HexBytes = self.voting_contract.functions.registerVoter(voter_address).transact()
        return voter.hex()

    async def add_candidate(self, candidate_address: str):
        candidate: HexBytes = self.voting_contract.functions.addCandidate(candidate_address).transact()
        return candidate.hex()

    async def vote(self, voter_address: str, candidate_addresses: List[str]):
        if voter_address in self.voter_list:
            return False
        else:
            try:
                for candidate_address in candidate_addresses:
                    self.voting_contract.functions.vote(voter_address, candidate_address).transact()
                self.voter_list.append(voter_address)
                return True
            except Exception:
                return False

    async def candidate_list(self):
        await self.update_candidate_vote_count()
        self.sort_candidates_by_vote_count()
        return self.candidate_data

    async def update_candidate_vote_count(self):
        for candidate in self.candidate_data["candidates"]:
            candidate["vote_count"] = await self.balance_of(candidate["address"])

    def sort_candidates_by_vote_count(self):
        candidates: list = self.candidate_data["candidates"]
        self.candidate_data["candidates"].sort(reverse=True, key=lambda e: e["vote_count"])

        for rank in range(1, len(candidates)):
            candidates[rank-1]["rank"] = rank
