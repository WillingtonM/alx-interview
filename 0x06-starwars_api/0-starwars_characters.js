#!/usr/bin/node

const request = require('request');

const numFilm = process.argv[2] + '/';
const filmURLDATA = 'https://swapi-api.hbtn.io/api/films/';

// Makes API request to get film data
request(filmURLDATA + numFilm, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse response body to get list of character URLs
  const charactorURLList = JSON.parse(body).characters;

  // Iterare through character URLs and factor character information
  for (const charactorURL of charactorURLList) {
    await new Promise(function (resolve, reject) {
      request(charactorURL, function (err, res, body) {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});