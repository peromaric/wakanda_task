#!/bin/bash

docker-compose -f docker-compose.yml up -d --build

#Create a local tmp folder that contains exports
mkdir ./tmp

#Contracts deployement, save output to .ENV
docker exec -it wakanda_blockchain_cont npx hardhat run --network localhost \
  scripts/deploy.js > ./tmp/addresses.json

#Copy the contract.json to the temporary folder

docker cp wakanda_blockchain_cont:/app/wakanda_blockchain/artifacts/contracts/wakandaVotingContract.sol/WakandaVotingContract.json \
  ./tmp/

docker cp wakanda_blockchain_cont:/app/wakanda_blockchain/artifacts/contracts/wakandaERC20.sol/WakandaERC20.json \
  ./tmp/

#Copy contract and address data to api cont (it waits for the data to arrive)
docker cp ./tmp/WakandaVotingContract.json \
  wakanda_api_cont:/app/wakanda_api/wakanda_api/contract_data/

docker cp ./tmp/WakandaERC20.json \
  wakanda_api_cont:/app/wakanda_api/wakanda_api/contract_data/

docker cp ./tmp/addresses.json \
  wakanda_api_cont:/app/wakanda_api/wakanda_api/contract_data/

#Remove tmp folder
rm -rf ./tmp
