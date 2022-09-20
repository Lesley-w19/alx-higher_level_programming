#!/usr/bin/node

/**
 * a function that returns the number of occurrences in a list:
 * Prototype: exports.nbOccurences = function (list, searchElement)
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let e = 0; e < list.length; e++) {
    if (searchElement === list[e]) {
      count++;
    }
  }

  return count;
};
