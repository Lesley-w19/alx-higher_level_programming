#!/usr/bin/node

/**
 * a script that searches the second biggest integer in the list of arguments.
 */

let max = 0;
let secondMax = 0;

for (let i = 2; i < process.argv.length; i++) {
  const number = parseInt(process.argv[i]);

  if (max < number) {
    secondMax = max;
    max = number;
  } else if (secondMax < number) {
    secondMax = number;
  }
}
console.log(secondMax);
