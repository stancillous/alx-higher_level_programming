#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];

const mydict = {};

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);

    data.forEach((item) => {
      if (item.completed) {
        if (!mydict[item.userId]) { // key not present
          mydict[item.userId] = 1;
        } else { // key present
          mydict[item.userId] += 1;
        }
      }
    });
    console.log(mydict);
  }
});
