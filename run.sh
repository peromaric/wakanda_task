#!/bin/bash

# in case the containers are up down them
docker-compose -f docker-compose.yml down

# up and build containers. build for first run
docker-compose -f docker-compose.yml up -d --build

#Create a local tmp folder that contains exports
mkdir ./tmp

# PATHS
BLOCKCHAIN_CONT_CONTRACT_PATH="/app/wakanda_blockchain/artifacts/contracts"
API_CONT_CONTRACT_PATH="/app/wakanda_api/wakanda_api/contract_data"

#Contracts deployement, save output to .ENV
docker exec -it wakanda_blockchain_cont npx hardhat run --network localhost \
  scripts/deploy.js > ./tmp/addresses.json

#Copy the contract.json to the temporary folder

docker cp wakanda_blockchain_cont:$BLOCKCHAIN_CONT_CONTRACT_PATH/wakandaVotingContract.sol/WakandaVotingContract.json \
  ./tmp/

docker cp wakanda_blockchain_cont:$BLOCKCHAIN_CONT_CONTRACT_PATH/wakandaERC20.sol/WakandaERC20.json \
  ./tmp/

#Copy contract and address data to api cont (it waits for the data to arrive)
docker cp ./tmp/WakandaVotingContract.json \
  wakanda_api_cont:$API_CONT_CONTRACT_PATH

docker cp ./tmp/WakandaERC20.json \
  wakanda_api_cont:$API_CONT_CONTRACT_PATH

docker cp ./tmp/addresses.json \
  wakanda_api_cont:$API_CONT_CONTRACT_PATH

#Remove tmp folder
rm -rf ./tmp
