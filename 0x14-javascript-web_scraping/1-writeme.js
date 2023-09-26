#!/usr/bin/node
const fs = require('fs')
const process = require('process')

filename = process.argv[2]
data = process.argv[3]

fs.writeFile(filename, data, encoding="utf-8", (error) => {
    if (error) {
        console.log(error)
    }
})