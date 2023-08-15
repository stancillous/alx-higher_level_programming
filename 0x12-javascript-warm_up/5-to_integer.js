#!/usr/bin/node
const n = process.argv[2];

if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log(n);
}
