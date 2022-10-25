#!/usr/bin/node
const request = require('request');

try {
  const movieId = process.argv[2];

  request(
        `https://swapi-api.hbtn.io/api/films/${movieId}`,
        {
          json: true
        },
        async (error, response, body) => {
          if (error) {
            console.log(error);
          }
          const characters = body.characters;

          for (const element of characters) {
            const name = await new Promise((resolve, reject) => {
              request(
                element,
                {
                  json: true
                },
                (error, response, body) => {
                  if (error) {
                    return reject(error);
                  }

                  resolve(body.name);
                }
              );
            });
            if (name !== undefined) {
              console.log(name);
            }
          }
        }
  );
} catch (error) {
  console.log(error);
}
