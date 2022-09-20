#!/usr/bin/node

/**
 * Write a script that concats 2 files.
 */

 const fs = require('fs');
 
 if (process.argv.length > 4) {
   const fileA = fs.readFileSync(process.argv[2], { encoding: 'utf-8' });
   const fileB = fs.readFileSync(process.argv[3], { encoding: 'utf-8' });
   fs.writeFile(process.argv[4], fileA + fileB, function (errMsg) {
     if (errMsg) {
       return console.log(errMsg);
     }
   });
 } else {
   console.log('Right format/ Usage: ./102-concat.js <filePathToSourceFile1> <filePathToSourceFile2> <filePathToDestinationFile>');
 }