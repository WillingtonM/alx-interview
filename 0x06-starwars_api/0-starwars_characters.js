#!/usr/bin/node
// A script that prints all characters of Star Wars movie

const util = require('util');
const request = util.promisify(require('request'));
const movieID = process.argv[2];

async function starwarsCharacters (movieID) {
  const endpnt = 'https://swapi-api.hbtn.io/api/films/' + movieID;
  let resp = await (await request(endpnt)).body;
  resp = JSON.parse(resp);
  const chars = resp.characters;

  for (let x = 0; x < chars.length; x++) {
    const urlCharacter = chars[x];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(movieID);