#!/usr/bin/node
const fs = require('fs')
const process = require('process')
const filename = process.argv[2]

fs.readFile(filename, encoding="utf-8", (error, data) => {
    if (error) {
        console.log(error)
    }
    else {
        console.log(data)
    }
})