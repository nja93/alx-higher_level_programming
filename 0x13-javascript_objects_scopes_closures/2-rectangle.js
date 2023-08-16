#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object
    if (w > 0 && h > 0) { // if statement to check that both w and h > 0
      this.width = w;
      this.height = h;
    }
  }
}; // An empty object is not explicitly created if the conditions are not met.
// In this code, if the conditions (h > 0 && w > 0) are not satisfied,
// the constructor will not initialize the width and height properties
// Instead, the created object will not have these properties at all.
