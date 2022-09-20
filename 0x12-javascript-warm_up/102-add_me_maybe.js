#!/usr/bin/node

/**
 *  a function that increments and calls a function.
 */

exports.addMeMaybe = function (num, numFunc) {
  num++;
  numFunc(num);
};
