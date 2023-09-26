#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const moviesLen = data.results.length;
    for (let i = 0; i < moviesLen; i++) {
      if (i === movieId) {
        data.results[i].characters.forEach((character) => {
          request(character, (error, response, body) => {
            if (error) {
              console.log(error);
              return;
            }
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          });
        });
      }
    }
  }
});
