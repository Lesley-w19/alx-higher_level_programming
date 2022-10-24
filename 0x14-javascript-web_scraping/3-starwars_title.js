#!/usr/bin/node
// usr/lib/node_modules
const req = require('request');

try {
  const id = process.argv[2];
  req(
        `https://swapi-api.hbtn.io/api/films/${id}`,
        {
          json: true
        },
        (error, response, body) => {
          if (error) {
            console.log(error);
          }
          console.log(body.title);
        }
  );
} catch (error) {
  console.log(error);
}
