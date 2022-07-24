// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title Wakanda
 * @dev Create a sample ERC20 standard token
 */
contract WakandaERC20 is ERC20 {
    
    address owner;

    constructor() ERC20("Wakanda", "WKND") {
        owner = msg.sender;
        _mint(address(this), 1000000);
    }
    
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        require(msg.sender == owner, "Only the owner can transfer tokens.");
    }

    function changeOwner(address _new_owner) public payable {
        require(msg.sender == owner, "Only the owner can change the owner's address");
        _mint(_new_owner, 1000000);
        owner = _new_owner;
    }
}