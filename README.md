# wakanda_task

An example of a blockchainized voter contract and everything that comes along with it

Decided to go for a dockerized environment. Why? Cause it's easier in case anyone wants to try it.
The idea is - you basically just run one script and that's it, the entire thing works.

# User's manual

All info regarding this app. Also provided some details regarding the architecture. 

## How to run?

You need to have docker installed and docker compose. The versions I'm running are:
- docker-compose: **1.29.2, build 5becea4c**
- docker: **20.10.7, build 20.10.7-0ubuntu5~20.04.2**

After you've installed docker and docker-compose, all you need to do is make the ./run script executable and then run the script. 

**WARNING:** if it takes too long to build, blockchain_api container will restart because it's waiting contract data from blockchain_cont. In case it happens just rerun the script and that's it.

In case you'd like to see what happens on the blockchain (transaction related), run the following command:

`docker logs -f wakanda_blockchain_cont`


## Registration page

![image](https://user-images.githubusercontent.com/67732669/183243822-318af0e4-2180-422b-bae1-e9d03d508da6.png)

This is just the most basic registration page, super simple. You enter an address and that's it. You can register multiple times obviously.

After you've registered you can go to the voting page.

## Voting page

![image](https://user-images.githubusercontent.com/67732669/183244228-3cb7b7d3-fba1-43a3-bdb2-8adb934071d0.png)

Here you can actually vote for one or multiple candidates, depending on the number of tokens you have. Just select the candidate and press vote, that's it.

## Contract specifics

How do the contracts work? There's two contracts (https://github.com/peromaric/wakanda_task/tree/main/wakanda_blockchain/contracts) --> wakandaERC20.sol and wakandaVotingContract.sol

These contracts get compiled and deployed within the blockchain_cont. 

### ERC20 specifics

function _beforeTokenTransfer - overrides the standard _beforeTokenTransfer function so that only the OWNER may transfer tokens. Why? Because when someone votes, the tokens get sent to the address of the candidate a voter voted for. We don't want anyone to be able to send the tokens and bypass the checks that exist on the server.
