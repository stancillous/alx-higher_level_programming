#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(Number(a) + Number(b));
}
