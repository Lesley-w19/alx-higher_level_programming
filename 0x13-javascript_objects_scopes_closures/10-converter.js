#!/usr/bin/node

/**
 * a function that converts a number from base 10 to another base passed as argument:
 * Prototype: exports.converter = function (base)
 */
let newNum;
exports.converter = function (base) {
  return function (num) {
    newNum = num.toString(base);
    return newNum;
  };
};
