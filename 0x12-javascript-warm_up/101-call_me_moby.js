#!/usr/bin/node
/**
 * a function that executes x times a function.
 */

exports.callMeMoby = function (args, argFunction) {
  let i;
  for (i = 0; i < args; i++) {
    argFunction();
  }
};
