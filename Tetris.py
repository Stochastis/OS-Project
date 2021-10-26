class Figure:
    figures = [ #Contains all 7 tetrominos and their rotations. All in a 4x4 grid.
        [[1, 5, 9, 13], [4, 5, 6, 7]], #'I' piece
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], #'L' piece
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], #'J' piece
        [[1, 2, 4, 5], [1, 5, 6, 10]], #'S' piece
        [[1, 2, 6, 7], [2, 6, 5, 9]], #'Z' piece
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #'T' piece
        [[1, 2, 5, 6]], #'O' piece
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0