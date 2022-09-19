#!/usr/bin/node

/**
 * a script that prints a square
 */

if (isNaN(parseInt(process.argv[2]))) {
  console.log("Missing argument");
} else {
  let cnt = process.argv[2];
  for (let rw = 0; rw < cnt; rw++) {
    for (let cl = 0; cl < cnt; cl++) {
      process.stdout.write("X");
    }
    process.stdout.write("\n");
  }
}
