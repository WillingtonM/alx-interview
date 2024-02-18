#!/usr/bin/nodenumFilm
// A script that prints all characters of Star Wars movie
const req = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <n>');
  process.exit(1);
}

const proc_id = process.argv[2];
if (isNaN(proc_id)) {
  console.log('<n> must be an integer');
  process.exit(1);
}

function promiseRequest (url) {
  return new Promise((resolve, reject) => {
    req.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function dispChars () {
  const endpoint = `https://swapi-api.alx-tools.com/api/films/${proc_id}`;
  try {
    const resp = await promiseRequest(endpoint);
    const char = resp.characters;
    for (const character of char) {
      const charBody = await promiseRequest(character);
      const name = charBody.name;
      console.log(name);
    }
  } catch (err) {
    console.error(err);
  }
}

dispChars();