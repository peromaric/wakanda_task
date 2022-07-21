// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Wakanda
 * @dev Create a sample ERC20 standard token
 */
contract WakandaVotingContract {

    IERC20 private token;
    address private owner;
    address[] private candidateList;

    constructor(IERC20 _token, address _owner) {
        token = _token;
        owner = _owner;
    }

    function balanceOf(address account) public view returns (uint256) { 
        return token.balanceOf(account);
    }

    function vote(address _candidateAddress) public {
        require(balanceOf(msg.sender) > 1 && checkIfCandidateExists(_candidateAddress), "You're out of touch, I'm out of mind.");
        token.transferFrom(owner, _candidateAddress, 1);
    }

    function registerVoter(address _voterAddress) public {
        token.transferFrom(owner, _voterAddress, 1);
    }

    function addCandidate(address _candidate) public {
        require(msg.sender == owner, "You can't add candidates unless you're the owner of the contract!");
        candidateList.push(_candidate);
    }

    function checkIfCandidateExists(address _candidate) internal view returns (bool) {
        for(uint i = 0; i < candidateList.length; i++) {
            if (candidateList[i] == _candidate) return true;
        }
        return false;
    }
}