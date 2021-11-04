class Figure:
    figures = [ #Contains all 7 tetrominos and their rotations. All in a 4x4 grid.
                #TODO: Verify that rotations are in order (clockwise or counter-clockwise) according to Tetris game development rules.
        [[1, 5, 9, 13], [4, 5, 6, 7]], #'I' piece
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], #'J' piece
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], #'L' piece
        [[1, 2, 4, 5], [1, 5, 6, 10]], #'S' piece
        [[1, 2, 6, 7], [2, 6, 5, 9]], #'Z' piece
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #'T' piece
        [[1, 2, 5, 6]], #'O' piece
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1) #Instead of randomizing colors, change this to the specific color for each tetromino.
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

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
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def intersects(self): #Checks to see if a figure is intersecting with an edge of the map.
        intersection = False
        for i in range(4):
            for j in range(4):
                if i*4+j in self.figure.image():
                    if i+self.figure.y > self.height-1 or \
                        j+self.figure.x > self.width - 1 or \
                        j+self.figure.x < 0 or \
                        self.field[i+self.figure.y][j+self.figure.x] > 0:
                        intersection = True
        return intersection