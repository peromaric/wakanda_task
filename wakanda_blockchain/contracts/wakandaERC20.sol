// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title Wakanda
 * @dev Create a sample ERC20 standard token
 */
contract WakandaERC20 is ERC20 {
    
    address owner;

    constructor(address _owner) ERC20("Wakanda", "WKND") {
        owner = _owner;
        _mint(owner, 100000000);
    }
    
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        require(msg.sender == owner, "ERC20WithSafeTransfer: invalid recipient");
    }

}