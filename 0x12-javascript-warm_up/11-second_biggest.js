#!/usr/bin/node
// finds the second biggest integer in the cmd line arguments.

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else if (args.length == 4) {
  Number(args[2]) > Number(args[3]) ? console.log(args[3]) : console.log(args[2]);
} else {
  const arr = args.slice(2).map(Number);
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
