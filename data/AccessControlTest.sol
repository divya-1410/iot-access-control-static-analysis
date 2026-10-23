
 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AccessControlTest {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Intentionally vulnerable test case:
    // Any caller can change the owner.
    function changeOwner(address newOwner) public {
        owner = newOwner;
    }

    // Protected control case:
    uint256 public protectedValue;

    function setProtectedValue(uint256 newValue) public {
        require(msg.sender == owner, "Not authorized");
        protectedValue = newValue;
    }
}
