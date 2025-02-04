const path = require('node:path');

const a1 = path.basename('C:/Users/HP/Desktop/Nodejs/pathmodules.js');
console.log(a1);

const a2 = path.dirname('C:/Users/HP/Desktop/Nodejs/pathmodules.js');
console.log(a2);

const a3 = path.extname('C:/Users/HP/Desktop/Nodejs/pathmodules.js');
console.log(a3);
//go through the documentation to learn more about the path module and the function it provides