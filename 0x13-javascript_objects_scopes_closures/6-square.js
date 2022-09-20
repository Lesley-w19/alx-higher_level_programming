#!/usr/bin/node

/**
 * a class Square that defines a square and inherits from Square of 5-square.js:
 * ou must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const BSquare = require("./5-square");

class Square extends BSquare {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let r = 0; r < this.height; r++) {
        for (let cl = 0; cl < this.width; cl++) {
          process.stdout.write(c);
        }
        process.stdout.write("\n");
      }
    }
  }
}

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

module.exports = Square;
