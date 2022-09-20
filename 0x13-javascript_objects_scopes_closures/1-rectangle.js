#!/usr/bin/node

/**
 * Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
 */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
// const r1 = new Rectangle(2, 3);
// console.log(r1);
// console.log(r1.width);
// console.log(r1.height);

// const r3 = new Rectangle(2);
// console.log(r3);
// console.log(r3.width);
// console.log(r3.height);

module.exports = Rectangle;
