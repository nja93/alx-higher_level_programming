#!/usr/bin/node

// So first we need access to the request module so that we can use its methods
const request = require('request');

// Next, we need to access the process.argv[] array

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  characters = data.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
