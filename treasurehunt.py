import random
import turtle
import time

def generate_map(size=7):
    # Criar um grid com paredes na primeira e última linha
    grid = [['#' for _ in range(size)] for _ in range(size)]
    
    # Preencher o meio com espaços vazios
    for i in range(1, size - 1):
        grid[i] = ['#'] + ['.' for _ in range(size - 2)] + ['#']
    
    # Adicionar paredes aleatórias dentro do espaço permitido
    num_walls = random.randint(8, 15)
    for _ in range(num_walls):
        x, y = random.randint(1, size-2), random.randint(1, size-2)
        grid[x][y] = '#'
    
    # Definir a posição inicial do caçador de tesouros
    start_x, start_y = random.randint(1, size-2), random.randint(1, size-2)
    while grid[start_x][start_y] == '#':
        start_x, start_y = random.randint(1, size-2), random.randint(1, size-2)
    grid[start_x][start_y] = 'S'
    
    # Definir a posição do tesouro
    treasure_x, treasure_y = random.randint(1, size-2), random.randint(1, size-2)
    while grid[treasure_x][treasure_y] in ['#', 'S']:
        treasure_x, treasure_y = random.randint(1, size-2), random.randint(1, size-2)
    grid[treasure_x][treasure_y] = 'T'
    
    return grid, start_x, start_y, treasure_x, treasure_y

def draw_map(grid, size=7, cell_size=40):
    turtle.speed(0)
    turtle.penup()
    start_x, start_y = -size * cell_size // 2, size * cell_size // 2
    colors = {'#': 'black', '.': 'white', 'S': 'blue', 'T': 'gold'}
    
    for i in range(size):
        for j in range(size):
            x, y = start_x + j * cell_size, start_y - i * cell_size
            turtle.goto(x, y)
            turtle.pendown()
            turtle.fillcolor(colors[grid[i][j]])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(cell_size)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()

def move_hunter(grid, start_x, start_y, treasure_x, treasure_y, size=7, cell_size=40):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Direções: direita, baixo, esquerda, cima
    x, y = start_x, start_y
    path_stack = [(x, y)]
    visited = set()
    
    turtle.speed(1)
    turtle.shape("circle")
    
    while path_stack:
        x, y = path_stack[-1]
        pixel_x = -size * cell_size // 2 + y * cell_size + cell_size // 2
        pixel_y = size * cell_size // 2 - x * cell_size - cell_size // 2
        
        turtle.goto(pixel_x, pixel_y)
        turtle.fillcolor("blue")
        time.sleep(0.5)
        visited.add((x, y))
        
        if (x, y) == (treasure_x, treasure_y):
            turtle.fillcolor("green")
            break
        
        moved = False
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < size and 0 <= new_y < size and grid[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                path_stack.append((new_x, new_y))
                moved = True
                break
        
        if not moved:
            turtle.fillcolor("red")
            path_stack.pop()
            time.sleep(0.3)
    
    turtle.done()

# Gerar e exibir o mapa
mapa, start_x, start_y, treasure_x, treasure_y = generate_map()
draw_map(mapa)
move_hunter(mapa, start_x, start_y, treasure_x, treasure_y)
