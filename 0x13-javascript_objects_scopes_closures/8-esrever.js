#!/usr/bin/node
// func to reverse a list
exports.esrever = function (list) {
  const newList = [];
  const n = (list.length) - 1;
  let i = 0;

  for (let j = n; j >= 0; j--) {
    newList[i++] = list[j];
  }
  return (newList);
};
