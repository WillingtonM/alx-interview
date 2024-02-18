#!/usr/bin/node
// A script that prints all characters of Star Wars movie

const request = require('request');

const movie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/';
const api_url = api + 'films/' + movie + '/';
request.get({ url: api_url }, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    char_order(chars);
  }
});

function char_order (chars) {
  if (chars.length > 0) {
    request.get({ url: chars.shift() }, function (err, res, body) {
      if (!err) {
        console.log(JSON.parse(body).name);
        char_order(chars);
      }
    });
  }
}