#!/usr/bin/node

/**
 * print messages depending on the number of arguments
 */

if (process.argv.length === 3) {
  console.log("Argument found");
} else if (process.argv.length > 3) {
  console.log("Arguments found");
} else {
  console.log("No argument");
}
