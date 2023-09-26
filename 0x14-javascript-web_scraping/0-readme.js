#!/usr/bin/node

// imports built in 'file system' module' fs which enables interactions with file
const fs = require('fs');

// check if number of arguments on command line are 3
// script name,'node' and file path
if (process.argv.length !== 3) {
  console.error(error);
}
// Get the file path from the command-line arguments
const filePath = process.argv[2];
// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
