#!/usr/bin/node

//Import the built in node.js fs module
const fs = require('fs');

const request = require('request');
// Import the 'request' module

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
// Perform an HTTP GET request to the url
