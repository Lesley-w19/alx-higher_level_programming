#!/usr/bin/node

/**
 * a script that imports an array and computes a new array.
 * Your script must import list from the file 100-data.js
 * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
 * Print both the initial list and the new list
 */

const list = require('./100-data').list;
const newList = [];
console.log(list);
list.map((l, index) => {
  newList.push((l *= index));
  return newList;
});
console.log(newList);
