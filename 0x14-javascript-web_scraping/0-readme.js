#!/usr/bin/node
const fs = require('fs');

try {
    const file = process.argv[2]
    const data = fs.readFileSync(
        file,
        {
            encoding: 'utf-8',
            flag:'r'
        }
    )
    console.log(data)
} catch (error) {
    console.log(error)
}