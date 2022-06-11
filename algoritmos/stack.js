// PILHAS:arrays que seguem a política last in, first out

function Stack() {
  var items = [];

  // add an element to the stack (at the last spot)
  this.push = (element) => {
    items.push(element);
  };

  // remove an element of the stack (the last one)
  this.pop = () => {
    items.pop();
  };

  // return the last element of the stack
  this.peek = () => {
    return items[items.length - 1];
  };

  // check if the stack is empty
  this.isEmpty = () => {
    return items.length === 0;
  };

  // return how many elements the stack has
  this.size = () => {
    return items.length;
  };

  // remove all stack's elements
  this.clear = () => {
    items = [];
  };

  // print all the stack's elements
  this.print = () => {
    console.log(items.toString());
  };
}

var stack = new Stack();

console.log(stack.isEmpty());

stack.push(5);
stack.push(0);
stack.push(1);
stack.push(4);
stack.push(4);
stack.push(4);
stack.push(4);
stack.push(6);

console.log(`the last element is: ${stack.peek()}`);
console.log(`the stack size is: ${stack.size()}`);
stack.print();

stack.pop();
stack.pop();
stack.pop();

console.log(`the last element is: ${stack.peek()}`);
console.log(`the stack size is: ${stack.size()}`);
stack.print();

