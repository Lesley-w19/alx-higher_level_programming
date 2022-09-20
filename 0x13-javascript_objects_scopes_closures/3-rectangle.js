#!/usr/bin/node

/**
 *  a class Rectangle that defines a rectangle:
 *  Create an instance method called print() that prints the rectangle using the character X
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
}

// const r1 = new Rectangle(2, 3);
// r1.print();

// const r2 = new Rectangle(10, 5);
// r2.print();

module.exports = Rectangle;
