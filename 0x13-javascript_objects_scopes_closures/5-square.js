#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle { // can also be written as module.exports = class Square extends Rectangle, then exclude line 11
  constructor (size) { // constructor of square takes a single argument
    //
    super(size, size); // super used to call constructor of parent class both height and width have been set to size to make a square
  }
}
module.exports = Square; // exported so it can be used in another application
