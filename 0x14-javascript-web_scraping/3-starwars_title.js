#!/usr/bin/node

//Import the 'request' module
const request = require('request');

// Construct the URL for the specific star war film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

//Use the ''request' to perform an HTTP GET request
request(url, function (error, response, body) {
  // log title if successful, log error if not.
  console.log(error || JSON.parse(body).title);
})
