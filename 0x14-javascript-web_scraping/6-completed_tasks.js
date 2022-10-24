#!/usr/bin/node
const request = require('request');

try {
  const url = process.argv[2];
  const users = {};

  request(
    url,
    (error, response, body) => {
      if (error) {
        console.log(error);
      }
      JSON.parse(body).forEach(el => {
        if (el.completed === true) {
          if (el.userId in users) {
            users[el.userId] += 1;
          } else {
            users[el.userId] = 1;
          }
        }
      });
      console.log(users);
    }
  );
} catch (error) {
  console.log(error);
}
