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

    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    function balanceOf(address account) public view returns (uint256) { 
        return token.balanceOf(account);
    }

    function vote(address _candidate) public {
        require(balanceOf(msg.sender) > 1 && checkIfCandidateExists(_candidate), "You're out of touch, I'm out of mind.");
        token.transfer(_candidate, 1);
    }

    function registerVoter(address _voter) public {
        token.transfer(_voter, 1);
    }

    function addCandidate(address _candidate) public {
        require((msg.sender == owner) && !checkIfCandidateExists(_candidate), "You can't add candidates unless you're the owner of the contract!");
        candidateList.push(_candidate);
    }

    function checkIfCandidateExists(address _candidate) internal view returns (bool) {
        for(uint i = 0; i < candidateList.length; i++) {
            if (candidateList[i] == _candidate) return true;
        }
        return false;
    }
}