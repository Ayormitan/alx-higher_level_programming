#!/usr/bin/node

const fs = require('fs');
// Import 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // using fs.writefile to write data into a file.
  // The data writen is taken from fourth command line (process.aargv[3]).
  if (error) {
    // Print error parameter if error occurs gduring the write operation.
    console.error(error);
  }
});

