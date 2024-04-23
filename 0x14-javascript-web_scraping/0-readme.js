#!/usr/bin/node

const fs = require('fs');
//Import 'fs' module

fs.readFile(process.argv[2], 'utf8', function (error, content){
  //fs.readFile) is used to read the content of a line
  //'utf8' specifies the encding of the file to be read

  if (error) {
    // error parameter if error occurs during the read operation
    console.error('Error reading the file:', error);

    } else {
      // Print the content of the parameter if the file is proerly read
      console.log(content);
    }
  });
