#!/usr/bin/node
const fs = require('fs');

// script name,'node' and file path
// file path is the third argument
const filePath = process.argv[2];
// The second argument is the string to write
const newstring = process.argv[3];

fs.writeFile(filePath, newstring, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
