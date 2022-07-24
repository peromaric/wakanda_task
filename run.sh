#!/bin/bash

docker-compose -f docker-compose.yml up -d --build

#Contracts deployement, save output to .ENV
docker exec -it wakanda_blockchain_cont npx hardhat run --network localhost \
  scripts/deploy.js > ./wakanda_api/wakanda_api/contract_data/addresses.json

#copy the contract.json to the app
docker cp wakanda_blockchain_cont:/app/wakanda_blockchain/artifacts/contracts/wakandaVotingContract.sol/WakandaVotingContract.json \
  wakanda_api/wakanda_api/contract_data/

docker cp wakanda_blockchain_cont:/app/wakanda_blockchain/artifacts/contracts/wakandaERC20.sol/WakandaERC20.json \
  wakanda_api/wakanda_api/contract_data/
