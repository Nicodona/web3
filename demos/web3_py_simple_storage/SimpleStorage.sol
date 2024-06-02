// SPDX-Lincense-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 public myNum;

    struct People {
        uint256 myNum;
        string name;
    }

    People[] public people;

    mapping(string => uint) public nameToNum;

    function store(uint256 _myNum) public returns (uint256) {
        myNum = _myNum;
        return _myNum;
    }

    function retrieve() public view returns (uint256) {
        return myNum + myNum;
    }

    function addPerson(string memory _name, uint _num) public {
        people.push(People(_num, _name));
        nameToNum[_name] = _num;
    }
}
