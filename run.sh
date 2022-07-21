#!/bin/bash

docker-compose -f docker-compose.yml up -d --build

docker exec -it wakanda_blockchain_cont npx hardhat run --network localhost scripts/deploy.js


