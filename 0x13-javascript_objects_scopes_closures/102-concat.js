#!/usr/bin/node

// script that concats 2 files.

// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// he third argument is the file path of the destination

const fs = require('fs');
const src1 = fs.readFileSync(process.argv[2], 'utf8');
const src2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], src1 + src2);
