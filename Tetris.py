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