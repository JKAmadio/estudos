/*
 Implementar o algoritmo para DepthFirst 

  conceitos usados:
    POP -> retira o último elemento de um array
    PUSH -> insere um novo elemento no final do array
*/
function dfs(graph, initialNode) {
  let stack = [];
  stack.push(initialNode);
  graph[initialNode]['visited'] = true;
  while (stack.length > 0){
    current = stack.pop();
    console.log(current)
    graph[current]['connections'].map(item => {
      if (!graph[item]['visited']) {
        stack.push(item);
        graph[item]['visited'] = true; //na vdd ainda nao foi visitado, apenas inserido, ver se funfa
      }
    })
  }
}

const minigraph = {
  0: {
    connections: [1],
    visited: false
  },
  1: {
    connections: [0, 2, 3],
    visited: false
  },
  2: {
    connections: [1, 3],
    visited: false
  },
  3: {
    connections: [1],
    visited: false
  },
}
console.log(minigraph);
dfs(minigraph, 0);

const graph = {
  0: {
    connections: [1, 9],
    visited: false
  },
  1: {
    connections: [0, 8],
    visited: false
  },
  2: {
    connections: [3],
    visited: false
  },
  3: {
    connections: [2, 4, 5, 7],
    visited: false
  },
  4: {
    connections: [3],
    visited: false
  },
  5: {
    connections: [3, 6],
    visited: false
  },
  6: {
    connections: [5, 7],
    visited: false
  },
  7: {
    connections: [3, 6, 8, 10, 11],
    visited: false
  },
  8: {
    connections: [1, 7, 9],
    visited: false
  },
  9: {
    connections: [0, 8],
    visited: false
  },
  10: {
    connections: [7, 11],
    visited: false
  },
  11: {
    connections: [7, 10],
    visited: false
  },
  12: {
    connections: [],
    visited: false
  }
}

console.log(graph)
dfs(graph, 0);


