

const express = require('express');
//const React = require('react');

const app = express();


app.listen(3000, () => {
    console.log('Now listening on port 3000'); 
});


module.exports = { app };
