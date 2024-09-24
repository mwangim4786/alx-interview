#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// API request to get film data
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the response body to get the list of character urls
  const charURLList = JSON.parse(body).characters;

  // Make a request to each character URL and fecth character information
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter nformation and print the character's name Resolve the promise to indicate completion
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
