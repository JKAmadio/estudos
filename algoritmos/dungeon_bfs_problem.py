'''

You are trapped in a 2D dungeon and need to find the quickest way out!
The dungeon is composed of unit cubes which may or may not be filled
with rock. It takes one minute to move one unit north, south, east, west.
You cannot move diagonally and the maze is surrounded by solid rock on all
sides.

Is an escape possible? If yes, how long will it take?

    0   1   2   3   4   5   6
  -----------------------------
0 | S |   |   | # |   |   |   |
  -----------------------------
1 |   | # |   |   |   | # |   |
  -----------------------------
2 |   | # |   |   |   |   |   |
  -----------------------------
3 |   |   | # | # |   |   |   |
  -----------------------------
4 | # |   | # | E |   | # |   |
  -----------------------------

'''
maze = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0]
]

visited = [
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
]

queue = []
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

def base():
    print_maze()
    bfs_2d([0,0], [4,3])

def print_maze():
    for i in range(len(maze)):
        print(maze[i])
    print('\n')

def bfs_2d(start, end):
    global nodes_left_in_layer
    global nodes_in_next_layer
    global move_count
    queue.insert(0, start)
    maze[start[0]][start[1]] = 2
    visited[start[0]][start[1]] = True
    while len(queue) > 0:
        current = queue.pop()
        explore_neighbours(current[0], current[1])
        nodes_left_in_layer = nodes_left_in_layer - 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count = move_count + 1
            print_maze()
        if current == end:
            print(f'moves needed to reach exit: { move_count }')
            break

def explore_neighbours(row, column):
    global nodes_in_next_layer
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    i = 0
    for i in range(4):
        rr = row + dr[i]
        cc = column + dc[i]
        # não é vizinho válido se for out of bound do array
        if (rr < 0 or rr >= len(maze) or (cc < 0 or cc >= len(maze[0]))): continue
        # não é vizinho válido se for pedra
        if maze[rr][cc] == 1: continue
        # não é vizinho válido se já foi visitado
        if visited[rr][cc] == True: continue
        queue.insert(0, [rr, cc])
        visited[rr][cc] = True
        maze[rr][cc] = 2
        nodes_in_next_layer = nodes_in_next_layer + 1

base()
