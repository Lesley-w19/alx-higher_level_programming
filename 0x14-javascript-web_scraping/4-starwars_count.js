#!/usr/bin/node
const req = require('/usr/lib/node_modules/request');

try {
  const url = process.argv[2];

  req(
    url,
    {
      json: true
    },
    (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const count = body.results.filter((data) => {
        return data.characters.filter((charUrl) => {
          return charUrl.includes(('18'));
        }).length;
      }).length;
      console.log(count);
    }
  );
} catch (error) {
  console.log(error);
}
