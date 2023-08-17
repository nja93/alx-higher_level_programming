#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () { // switch width and height
    [this.height, this.width] = [this.width, this.height];
  }

  double () { // doubles size of height and width
    this.width *= 2;
    this.height *= 2;
  }
};
