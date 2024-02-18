#!/usr/bin/nodenumFilm
// A script that prints all characters of Star Wars movie

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  charsOrder(chars, 0);
});
const charsOrder = (chars, y) => {
  if (y === chars.length) return;
  request(chars[y], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    charsOrder(chars, y + 1);
  });
};