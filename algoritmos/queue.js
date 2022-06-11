// FILAS: seguem a política First in, first out

export function Queue() {
  var items = [];

  // add an element to the queue (at the first spot)
  this.push = (element) => {
    items.unshift(element);
  };

  // remove an element of the queue (the last one)
  this.pop = () => {
    items.pop();
  };

  // return the last element of the queue
  this.peek = () => {
    return items[items.length - 1];
  };

  // check if the queue is empty
  this.isEmpty = () => {
    return items.length === 0;
  };

  // returns how many elements the queue has
  this.size = () => {
    return items.length;
  };

  // remove all queue's elements
  this.clear = () => {
    items = [];
  };

  // print the elements of the queue
  this.print = () => {
    console.log(items.toString());
  };
}

var queue = new Queue();

console.log(queue.isEmpty());

queue.push(5);
queue.push(0);
queue.push(1);
queue.push(4);
queue.push(4);
queue.push(4);
queue.push(4);
queue.push(6);

queue.print();
console.log(`the last element is: ${queue.peek()}`);
console.log(`the queue size is: ${queue.size()}`);

queue.pop();
queue.pop();
queue.pop();

console.log(`the last element is: ${queue.peek()}`);
console.log(`the queue size is: ${queue.size()}`);
queue.print();

