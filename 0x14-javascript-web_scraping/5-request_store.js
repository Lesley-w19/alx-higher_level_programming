#!/usr/bin/node
const req = require('request');
const fs = require('fs');

try {
  const url = process.argv[2];
  const file = process.argv[3];

  req(
    url,
    {
      json: true
    },
    (error, response, body) => {
      if (error) {
        console.log(error);
      }
      fs.writeFileSync(
        file,
        body,
        {
          encoding: 'utf8',
          flag: 'w'
        }
      );
    }
  );
} catch (error) {
  console.log(error);
}
