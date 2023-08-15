#!/usr/bin/node
const num = Number(process.argv[2]);
const fact = factorial(num);
console.log(fact);

function factorial (n) {
  if (isNaN(n) || a <= 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}
