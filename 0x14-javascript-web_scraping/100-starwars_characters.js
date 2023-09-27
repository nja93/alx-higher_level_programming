#!/usr/bin/node

// We are writing a script that prints all characters of a Star Wars movie:
// So first we need access to the request module so that we can use its methods

const requestObj = require('request');

const movieId = process.argv[2];

// construct the url that will give us access to the API

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Next we need to use our request obj to make the GET request
// to the specified URL this will make an API call for our specific movieID
// We will also check for errors and if there are no errors print the title of the movie

requestObj.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    requestObj(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
