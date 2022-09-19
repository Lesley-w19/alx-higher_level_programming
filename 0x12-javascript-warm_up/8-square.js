#!/usr/bin/node

/**
 * a script that prints a square
 */

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing argument');
} else {
  const x = parseInt(process.argv[2]);
  for (let rw = 0; rw < x; rw++) {
    for (let cl = 0; cl < x; cl++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
