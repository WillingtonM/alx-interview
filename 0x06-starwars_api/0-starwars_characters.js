#!/usr/bin/nodenumFilm
// A script that prints all characters of Star Wars movie
const request = require('request');

const numFilm = process.argv[2] + '/';
const endpoint = 'https://swapi-api.hbtn.io/api/films/';

// Makes API request to get film information
request(endpoint + numFilm, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});