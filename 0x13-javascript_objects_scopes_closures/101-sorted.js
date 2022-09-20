#!/usr/bin/node

/**
 *  a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
 * Your script must import dict from the file 101-data.js
 * In the new dictionary:
 *A key is a number of occurrences
 *A value is the list of user ids
 *Print the new dictionary at the end
 */

const dictionary = require("./101-data").dict;
console.log(dictionary);

const newDict = {};

const keys = Object.keys(dictionary);
const values = Object.values(dictionary);

for (const i in keys) {
  if (newDict[values[i]] === undefined) {
    newDict[values[i]] = [];
  }
  newDict[values[i]].push(keys[i]);
}
console.log(JSON.stringify(newDict));
