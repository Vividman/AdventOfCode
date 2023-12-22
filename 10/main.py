with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\10\\input.txt") as f:
    lines = f.readlines()
# with open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\10\\test.txt") as f:
#     lines = f.readlines()

maze = []
for line in lines:
    maze.append(line.strip())

for row in maze:
    if 'S' in row:
        start = (maze.index(row), row.index('S'))

pipeline = [start]

if start[0]+1 < len(maze) and maze[start[0]+1][start[1]] in ['|', 'J', 'L']:
    next = (start[0]+1, start[1])
elif start[1]+1 < len(maze[start[0]]) and maze[start[0]][start[1]+1] in ['-', 'J', '7']:
    next = (start[0], start[1]+1)
elif start[0]-1 >= 0 and maze[start[0]-1][start[1]] in ['|', '7', 'F']:
    next = (start[0]-1, start[1])
elif start[1]-1 >= 0 and maze[start[0]][start[1]-1] in ['-', 'F', 'L']:
    next = (start[0], start[1]-1)

while next not in pipeline:
    pipeline.append(next)
    match maze[next[0]][next[1]]:
        case '|':
            # Top
            if next[0]-1 >= 0 and (next[0]-1, next[1]) not in pipeline and maze[next[0]-1][next[1]] in ['|', '7', 'F']:
                next = (next[0]-1, next[1])
            # Bottom
            elif next[0]+1 < len(maze) and (next[0]+1, next[1]) not in pipeline and maze[next[0]+1][next[1]] in ['|', 'J', 'L']:
                next = (next[0]+1, next[1])
        case '-':
            # Left
            if next[1]-1 >= 0 and (next[0], next[1]-1) not in pipeline and maze[next[0]][next[1]-1] in ['-', 'F', 'L']:
                next = (next[0], next[1]-1)
            # Right
            elif next[1]+1 < len(maze[next[0]]) and (next[0], next[1]+1) not in pipeline and maze[next[0]][next[1]+1] in ['-', 'J', '7']:
                next = (next[0], next[1]+1)
        case 'L':
            # Top
            if next[0]-1 >= 0 and (next[0]-1, next[1]) not in pipeline and maze[next[0]-1][next[1]] in ['|', '7', 'F']:
                next = (next[0]-1, next[1])
            # Right
            elif next[1]+1 < len(maze[next[0]]) and (next[0], next[1]+1) not in pipeline and maze[next[0]][next[1]+1] in ['-', 'J', '7']:
                next = (next[0], next[1]+1)
        case 'J':
            # Top
            if next[0]-1 >= 0 and (next[0]-1, next[1]) not in pipeline and maze[next[0]-1][next[1]] in ['|', '7', 'F']:
                next = (next[0]-1, next[1])
            # Left
            elif next[1]-1 >= 0 and (next[0], next[1]-1) not in pipeline and maze[next[0]][next[1]-1] in ['-', 'F', 'L']:
                next = (next[0], next[1]-1)
        case '7':
            # Left
            if next[1]-1 >= 0 and (next[0], next[1]-1) not in pipeline and maze[next[0]][next[1]-1] in ['-', 'F', 'L']:
                next = (next[0], next[1]-1)
            # Bottom
            elif next[0]+1 < len(maze) and (next[0]+1, next[1]) not in pipeline and maze[next[0]+1][next[1]] in ['|', 'J', 'L']:
                next = (next[0]+1, next[1])
        case 'F':
            # Right
            if next[1]+1 < len(maze[next[0]]) and (next[0], next[1]+1) not in pipeline and maze[next[0]][next[1]+1] in ['-', 'J', '7']:
                next = (next[0], next[1]+1)
            # Bottom
            elif next[0]+1 < len(maze) and (next[0]+1, next[1]) not in pipeline and maze[next[0]+1][next[1]] in ['|', 'J', 'L']:
                next = (next[0]+1, next[1])

print(f"Steps to farthest point: {len(pipeline)/2}")

def tuple_diff(one, two):
    return two[0]-one[0], two[1]-one[1]

def get_directions(coord):
    match coord:
        case (-1, 0):
            return 'n'
        case (1, 0):
            return 's'
        case (0, 1):
            return 'e'
        case (0, -1):
            return 'w'

def get_directional_filter(fr, to):
    match (fr, to):
        case ('n', 's'):
            return [[0, 0, 0], 
                    [-1, 0, 1], 
                    [0, 0, 0]]
        case ('s', 'n'):
            return [[0, 0, 0], 
                    [1, 0, -1], 
                    [0, 0, 0]]
        case ('e', 'w'):
            return [[0, -1, 0],
                    [0, 0, 0],
                    [0, 1, 0]]
        case ('w', 'e'):
            return [[0, 1, 0], 
                    [0, 0, 0], 
                    [0, -1, 0]]
        case ('n', 'w') | ('w', 'n'):
            return [[1, 0, 0], 
                    [0, 0, -1], 
                    [0, -1, -1]]
        case ('e', 'n') | ('n', 'e'):
            return [[0, 0, 1], 
                    [-1, 0, 0], 
                    [-1, -1, 0]]
        case ('s', 'w') | ('w', 's'):
            return [[0, -1, -1], 
                    [0, 0, -1], 
                    [1, 0, 0]]
        case ('e', 's') | ('s', 'e'):
            return [[-1, -1, 0],
                    [-1, 0, 0],
                    [0, 0, 1]]
    

direction_matrix = [[0 for _ in range(len(maze[i]))] for i in range(len(maze))]

filter = [
    [ 0,  0,  0],
    [ 0,  0,  0],
    [ 0,  0,  0]
]
prev = maze[pipeline[-1][0]][pipeline[-1][1]]
prev_coords = pipeline[-1]
current = 'S'
for i, pipe in enumerate(pipeline):
    match current:
        case 'S':
            next_coords = pipeline[1]
            next_symbol = maze[next_coords[0]][next_coords[1]]
            filter = get_directional_filter(get_directions(tuple_diff(pipe, prev_coords)), get_directions(tuple_diff(pipe, next_coords)))
            for f in filter:
                print(f)
            prev = current
            current = next_symbol

                

f = open("C:\\Users\\dn\\Desktop\\Prosjektarbeid\\AdventOfCode\\10\\no_pipe.txt", "w")

row = ""
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (i, j) in pipeline or maze[i][j] == ".":
            row += maze[i][j]
        else:
            row += " "
    row += "\n"

f.write(row)
f.close()