const http = require('http');

const port = process.env.PORT || 3000;;
 
const server = http.createServer((req, res) => {
    console.log(req);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end('<h1>absolute ludicrous tomfoolery</h1> <p> what the fuck does that mean </p>');
})

server.listen(port, ()=> {
    console.log(`server is listening on port ${port}`);
})