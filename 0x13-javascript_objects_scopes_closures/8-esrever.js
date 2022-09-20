#!/usr/bin/node

/**
 *  a function that returns the reversed version of a list:
 *  Prototype: exports.esrever = function (list)
 */

exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    // console.log(list[i]);
    reversedList.push(list[i]);
  }
  return reversedList;
};
