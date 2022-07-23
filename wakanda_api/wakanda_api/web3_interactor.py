import json
from wakanda_api.module import Module
from typing import Optional
from web3 import Web3
import pathlib


class Web3Interactor(Module):
    def __init__(self, wakanda_api):
        super().__init__(wakanda_api)

        # Get the contract data
        self.abi: Optional[list] = None
        self.bytecode: Optional[str] = None
        self._read_and_parse_contract_json()

        self.w3: Web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        default_account = self.w3.eth.account \
            .privateKeyToAccount("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
        self.w3.eth.defaultAccount = default_account

        VotingContract = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)
        pass

    def _read_and_parse_contract_json(self) -> None:
        contract_parsed: Optional[dict] = None
        contract_path: pathlib.Path = pathlib.Path("./wakanda_api/WakandaVotingContract.json")

        with contract_path.open() as contract_json:
            contract_parsed = json.load(contract_json)

        self.abi = contract_parsed["abi"]
        self.bytecode = contract_parsed["bytecode"]
