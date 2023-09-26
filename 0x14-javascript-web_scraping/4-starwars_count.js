#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];

let charTotal = 0;
const charId = '18';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((item) => {
      item.characters.forEach((film) => {
        if (film.includes(charId)) {
          charTotal += 1;
        }
      });
    });
    console.log(charTotal);
  }
});
