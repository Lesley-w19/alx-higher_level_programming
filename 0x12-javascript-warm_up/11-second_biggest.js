#!/usr/bin/node

/**
 * a script that searches the second biggest integer in the list of arguments.
 */

let max = 0;
let second_max = 0;

for (let i = 2; i < process.argv.length; i++) {
  let number = parseInt(process.argv[i]);

  if (max < number) {
    second_max = max;
    max = number;
  } else if (second_max < number) {
    second_max = number;
  }
}
console.log(second_max);
