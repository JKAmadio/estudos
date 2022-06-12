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
import matplotlib.pyplot as plt
import cv2
import os

maze = [
    [0, 0, 0, -10, 0, 0, 0],
    [0, -10, 0, 0, 0, -10, 0],
    [0, -10, 0, 0, 0, 0, 0],
    [0, 0, -10, -10, 0, 0, 0],
    [-10, 0, -10, 0, 0, -10, 0]
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
image_list = []

def base():
    # print_maze()
    bfs_2d([0,0], [4,3])
    record_maze_changes()

def print_maze():
    fig, ax = plt.subplots()
    image = ax.imshow(maze, cmap='bone')
    image_list.append([image])
    plt.savefig(f'./dungeon_path/dungeon_{move_count}')
    # plt.show(block=True)

def record_maze_changes():
    image_list = [img for img in os.listdir('./dungeon_path/') if img.startswith('dungeon_') and img.endswith('.png')]
    image_list.sort()
    frame = cv2.imread(f'./dungeon_path/{image_list[0]}')
    height, width, layers = frame.shape
    video = cv2.VideoWriter('./dungeon_path/dungeon_video.avi', 0, 3, (width, height))
    for image in image_list:
        video.write(cv2.imread(f'./dungeon_path/{image}'))
    cv2.destroyAllWindows()
    video.release()

def bfs_2d(start, end):
    global nodes_left_in_layer
    global nodes_in_next_layer
    global move_count
    queue.insert(0, start)
    maze[start[0]][start[1]] = 10
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
        if maze[rr][cc] == -10: continue
        # não é vizinho válido se já foi visitado
        if visited[rr][cc] == True: continue
        queue.insert(0, [rr, cc])
        visited[rr][cc] = True
        maze[rr][cc] = move_count + 10
        nodes_in_next_layer = nodes_in_next_layer + 1

base()
