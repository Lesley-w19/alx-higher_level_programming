#!/usr/bin/node
const request = require('request');

try {
  const movieId = process.argv[2];

  request(
        `https://swapi-api.hbtn.io/api/films/${movieId}`,
        {
          json: true
        },
        (error, response, body) => {
          if (error) {
            console.log(error);
          }
          const characters = body.characters;

          characters.forEach(element => {
            request(
              element,
              {
                json: true
              },
              (error, response, body) => {
                if (error) {
                  console.log(error);
                }
                console.log(body.name);
              }
            );
          });
        }
  );
} catch (error) {
  console.log(error);
}
