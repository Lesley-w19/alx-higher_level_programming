#!/usr/bin/node
const fs = require("fs");

try {
    const file  = process.argv[2];
    const content = process.argv[3];

    fs.writeFileSync(
        file, content,
        {
            encoding: 'utf8',
            flag: 'w'
        },
        err =>{
            console.log(err);
        }
    )
} catch (error) {
    console.log(error);
}