#!/usr/bin/node
const request = require("/usr/lib/node_modules/request");

try {
  const id =  process.argv[2];
  const characterUrl = "https://swapi-api.hbtn.io/api/people/";
  const charactersList = [];

  request(`https://swapi-api.hbtn.io/api/films/${id}`, { json: true }, (err, res, body) => {
    if (err) {
      return console.error(err);
    }
    body.characters.forEach((character) => {
      const character_id = character.split("/")[5];

      request(characterUrl + character_id, { json: true }, (err, res, body) => {
        if (err) {
          return console.error(err);
        }
        console.log(body.name);
        charactersList.push(body.name);
      });
    });
  });
} catch (error) {
  console.log(error);
}
