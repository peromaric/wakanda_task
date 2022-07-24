import json
from wakanda_api.module import Module
from typing import Optional
from web3 import Web3
import pathlib
import requests


class Web3Interactor(Module):
    def __init__(self, wakanda_api):
        super().__init__(wakanda_api)
        self.web3: Optional[Web3] = None
        self.candidate_data: Optional[dict] = None

        # Request and candidate data from API
        self.candidate_data = requests.get("https://wakanda-task.3327.io/list").json()

        # Get the contract data
        path_to_token_contract: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/WakandaERC20.json")
        path_to_voting_contract: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/WakandaVotingContract.json")
        path_to_deployed_contract_addresses: pathlib.Path = pathlib.Path("./wakanda_api/contract_data/addresses.json")

        token_contract_data: dict = self._read_and_parse_contract_json(path_to_token_contract)
        voting_contract_data: dict = self._read_and_parse_contract_json(path_to_voting_contract)
        deployed_contract_data: dict = self._read_and_parse_contract_json(path_to_deployed_contract_addresses)

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


        pass

    @staticmethod
    def _read_and_parse_contract_json(contract_path: pathlib.Path) -> Optional[dict]:
        contract_parsed: Optional[dict] = None

        with contract_path.open() as contract_json:
            contract_parsed = json.load(contract_json)

        return contract_parsed

    async def balance_of(self, address: str):
        await self.voting_contract.functions.balanceOf(address).call()

    async def register_voter(self, voter_address: str):
        await self.voting_contract.functions.registerVoter(voter_address).transact()

    async def add_candidate(self, candidate_address: str):
        await self.voting_contract.functions.addCandidate(candidate_address).transact()

    async def vote(self, candidate_address: str):
        await self.voting_contract.functions.vote(candidate_address).transact()