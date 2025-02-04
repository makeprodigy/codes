const fs = require('node:fs');

// fs.readFile('file.txt', 'utf-8', (err, data) => {
//     console.log(err, data);
// })
// console.log('finished reading file');

// const a = fs.readFileSync('file.txt')
// console.log(a.toString());


// fs.writeFile('file.txt', 'if this world was mine', (err) => {
//     console.log('written');
// })
const b = fs.writeFileSync('file.txt', 'if this world was mine');
console.log(b);
console.log('written');
