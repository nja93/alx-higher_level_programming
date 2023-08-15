#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const numb = parseInt(firstArg);

function calcFactorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * calcFactorial(x - 1);
  }
}

if (!isNaN(numb)) {
  console.log(calcFactorial(numb));
} else {
  console.log('1');
}
