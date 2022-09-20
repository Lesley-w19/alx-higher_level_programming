#!/usr/bin/node

/**
 * a class Rectangle that defines a rectangle:
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle using the character X
 * Create an instance method called rotate() that exchanges the width and the height of the rectangle
 * Create an instance method called double() that multiples the width and the height of the rectangle by 2

 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    (this.width) *= 2;
    (this.height) *= 2;
  }
}

// const r1 = new Rectangle(2, 3);
// console.log("Normal:");
// r1.print();

// console.log("Double:");
// r1.double();
// r1.print();

// console.log("Rotate:");
// r1.rotate();
// r1.print();

module.exports = Rectangle;
