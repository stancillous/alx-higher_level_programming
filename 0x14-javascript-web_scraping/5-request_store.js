#!/usr/bin/node
const request = require('request')
const process = require('process')
const fs = require('fs')
const url = process.argv[2]
const filename = process.argv[3]

request(url, (error, response, body) => {
    if (error){
        console.log(error)
    }
    else {
        fs.writeFile(filename, body, encoding="utf-8", (err) => {
            if (err) {
                console.log(err)
            }
        })
    }
})
