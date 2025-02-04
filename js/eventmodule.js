const EventEmitter = require('node:events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('Waterfull', () => {
  console.log('Paani ki tanki bhar gayi hai!!');
  setTimeout(() => {
    console.log('motor jaldi band kar bkl!!');
  }, 4000);
});

console.log("the script is running");
myEmitter.emit('Waterfull');
console.log("the script is still running");
myEmitter.emit('Waterfull');
