#!/usr/bin/node

/**
 * a script that prints the addition of 2 integers
 */

function add (first, second) {
  return first + second;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
