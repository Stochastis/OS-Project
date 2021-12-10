import pygame
import random

colors = [(0, 0, 0), (0, 255, 255), (255, 255, 0), (128, 0, 128),
          (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]


class Figure:
    x, y = 0, 0

    figures = [  # Contains all 7 tetrominos and their rotations.  All in a 4x4 grid.  #TODO:
        # Verify that rotations are in order (clockwise or
        # counter-clockwise) according to Tetris game development rules.
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # 'I' piece
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # 'J' piece
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # 'L' piece
        [[1, 2, 4, 5], [1, 5, 6, 10]],  # 'S' piece
        [[1, 2, 6, 7], [2, 6, 5, 9]],  # 'Z' piece
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # 'T' piece
        [[1, 2, 5, 6]],  # 'O' piece
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)

        # Set piece color appropriately:
        if self.type == 0:
            self.color = 1
        elif self.type == 1:
            self.color = 2
        elif self.type == 2:
            self.color = 3
        elif self.type == 3:
            self.color = 4
        elif self.type == 4:
            self.color = 5
        elif self.type == 5:
            self.color = 6
        elif self.type == 6:
            self.color = 7

        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


'''
Initialize game. Create field of height and width and create a new tetromino
positioned at (3,0)
'''


class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

    '''
    Check if the tetromino flying down is going to clash with anything fixed on the field.
    The for loops go through a 4x4 matrix, checking if the tetromino is out of bounds
    and if it's touching a busy game field. If there is a zero, then we're all good and the field is empty
    '''

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    '''
    Check if there are any lines that are filled that we need to destroy.
    Destroying a line goes from bottom to top
    '''

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    '''
    When a tetromino reaches the bottom, we freeze the field so that the controls are no
    longer focused on that piece and instead on a new one flying down
    '''

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j +
                                                  self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    ''' 
    The moving methods. In every method we remember the last position and if an
    intersection already exists. If there is an intersection in the tetrominoes, return to previous state
    '''

    def go_space(self, left):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation


'''
oui oui initalízê le gâme engine hoh hoh hoh
(change this later)
'''
pygame.init()

'''
définir des couleurs
'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SHOW ME WHAT YOU GOT")

'''
Boucle jusqu'à ce que l'utilisateur clique sur fermer
Loop until the user clicks the close button.
'''
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            # Clears the board and initiates a new game if you are at a gameover.
            if event.key == pygame.K_ESCAPE and game.state == "gameover":
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

    # Background of the screen
    screen.fill(BLACK)

    # Draws the grey screen border.
    pygame.draw.rect(
        screen, GRAY, [game.x, game.y + game.zoom, game.zoom * 10, game.zoom * 19], 1)

    # Draws the grid and the pieces that have already landed.
    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    # Draws the current piece that the player is moving.
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom *
                                      (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, WHITE)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
