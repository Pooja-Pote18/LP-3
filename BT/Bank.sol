# RUN THIS CODE TO REMIX IDLE

// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    uint256 balance = 0;
    address public accOwner;

    constructor() {
        accOwner = msg.sender;
    }

    // Deposit
    function Deposit() public payable {
        require(accOwner == msg.sender, "You are not an account owner");
        require(msg.value > 0, "Amount should be greater than 0!");
        balance += msg.value;
    }

    // Withdraw
    function Withdraw(uint256 amount) public {
        require(accOwner == msg.sender, "You are not an account owner");
        require(amount > 0, "Withdrawal amount should be greater than 0!");
        require(balance >= amount, "Insufficient balance");

        balance -= amount;
        payable(msg.sender).transfer(amount); // Send ETH back to the owner
    }

    // Show Balance
    function showBalance() public view returns (uint256) {
        require(accOwner == msg.sender, "You are not an account owner");
        return balance;
    }
}

