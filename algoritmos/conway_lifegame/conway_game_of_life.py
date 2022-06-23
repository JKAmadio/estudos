import matplotlib.pyplot as plt
import cv2
import os

def count_neighbours_alive(matrix, coordinates):
    neighbours_alive = 0
    row_index = coordinates[0]
    column_index = coordinates[1]
    # compute 8-neighbour sum
    # check the connected neighbours
    dx = [0, 1, 0, -1, -1, 1, -1, 1]
    dy = [-1, 0, 1, 0, -1, 1, 1, -1]
    i = 0
    for i in range(len(dx)):
        if ((row_index + dx[i] >= 0 and row_index + dx[i] < len(matrix))\
                and column_index + dy[i] >= 0 and column_index + dy[i] < len(matrix[0])):
            neighbours_alive += matrix[row_index + dx[i]][column_index + dy[i]]
    return neighbours_alive

def update_cell_state(cell_state, neighbours_alive):
    if (cell_state == 1):
        if (neighbours_alive < 2 or neighbours_alive > 3):
            cell_state = 0
    else:
        if (neighbours_alive == 3):
            cell_state = 1
    return cell_state

def update_grid(matrix):
    new_generation = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print(f'matrix[{i}][{j}] = {matrix[i][j]}')
            neighbours_alive = count_neighbours_alive(matrix, [i, j])
            new_generation[i][j] = update_cell_state(matrix[i][j], neighbours_alive)
    return new_generation

def print_grid(matrix, count_generations):
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='gray')
    fig.set_facecolor('black')
    plt.savefig(f"./images/conway_{format(count_generations, '04d')}")
    # plt.show()

def record_grid_changes():
    # image_list = [img for img in os.listdir('./images/') if img.startswith('conway_)') and img.endswith('.png')]
    image_list = []
    for file in os.listdir('./images/'):
        if (file.startswith('conway_') and file.endswith('.png')):
            image_list.append(file)
    image_list.sort()
    frame = cv2.imread(f'./images/{image_list[0]}')
    height, width, layers = frame.shape
    video = cv2.VideoWriter('./images/conway_video.avi', 0, 3, (width, height))
    for image in image_list:
        video.write(cv2.imread(f"./images/{image}"))
    cv2.destroyAllWindows()
    video.release()


