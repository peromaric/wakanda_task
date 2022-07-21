// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {
  let wallet = new hre.ethers.Wallet("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80");

  const WakandaERC20 = await hre.ethers.getContractFactory("WakandaERC20");
  const WakandaVotingContract = await hre.ethers.getContractFactory("WakandaVotingContract");
  
  const wakandaERC20 = await WakandaERC20.deploy(wallet.address);
  await wakandaERC20.deployed();

  const wakandaVotingContract = await WakandaVotingContract.deploy(wakandaERC20.address, wallet.address);
  await wakandaVotingContract.deployed()
  
  console.log("TOKEN_CONTRACT:", wakandaERC20.address);
  console.log("VOTING_CONTRACT:", wakandaVotingContract.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
