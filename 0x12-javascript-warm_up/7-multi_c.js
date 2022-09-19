#!/usr/bin/node

/**
 * a script that prints x times “C is fun”
 */

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of arguments');
} else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
