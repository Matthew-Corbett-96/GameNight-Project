const express = require('express');
const serveStatic = require('serve-static');
const path = require('path');

const app = express();

// Serve static files from the dist directory
app.use('/', serveStatic(path.join(__dirname, '/dist')));

// Catch all routes and redirect to the index file
app.get('*', function (req, res) {
  res.sendFile(__dirname + '/dist/index.html');
});

// Start server
const port = process.env.PORT || 5000;
app.listen(port);
console.log('Server started on port ' + port);