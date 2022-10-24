#!/usr/bin/node
const request = require('request');

try {
    const url = process.argv[2];
    request(
        url,
        (err, response, body) => {
            if (err) {
                console.log(err);
            }
            console.log("code:", response && response.statusCode);
        }
    );
} catch (error) {
    console.log(error);
}