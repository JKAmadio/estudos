'''
                    1 - 2
minigraph ==>       | \ |
                    0   3

                              2  4
                                \|
                        1        3 -- 5
                      /   \      |    |
graph    ==>        0       8 -- 7 -- 6
                      \   /     /  \
                        9     10   11

'''
minigraph = {
    0: {
        'connections': [1],
        'visited': False
    },
    1: {
        'connections': [0, 2, 3],
        'visited': False
    },
    2: {
        'connections': [1, 3],
        'visited': False
    },
    3: {
        'connections': [1],
        'visited': False
    },
}
graph = {
    0: {
        'connections': [1, 9],
        'visited': False
    },
    1: {
        'connections': [0, 8],
        'visited': False
    },
    2: {
        'connections': [3],
        'visited': False
    },
    3: {
        'connections': [2, 4, 5, 7],
        'visited': False
    },
      4: {
        'connections': [3],
        'visited': False
    },
    5: {
        'connections': [3, 6],
        'visited': False
    },
    6: {
        'connections': [5, 7],
        'visited': False
    },
    7: {
        'connections': [3, 6, 8, 10, 11],
        'visited': False
    },
    8: {
        'connections': [1, 7, 9],
        'visited': False
    },
    9: {
        'connections': [0, 8],
        'visited': False
    },
    10: {
        'connections': [7, 11],
        'visited': False
    },
    11: {
        'connections': [7, 10],
        'visited': False
    },
    12: {
        'connections': [],
        'visited': False
    }
}

def depth_first_search(graph, initial_node):
    stack = []
    stack.append(initial_node)
    graph[initial_node]['visited'] = True
    while len(stack) > 0:
        current = stack.pop()
        for item in graph[current]['connections']:
            if (graph[item]['visited'] is False):
                stack.append(item)
                graph[item]['visited'] = True

depth_first_search(graph, 2)
