#!/usr/bin/node

/**
 * a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
 * you must use the class notation for defining your class and extends
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (side) {
    super(side, side);
  }
}

// const s1 = new Square(4);
// s1.print();
// s1.double();
// s1.print();

module.exports = Square;
