import random
import os
import sys
import tty
import termios


class Board():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        # init layout
        self.layout = []
        for nr in range(self.height):
            row = list(range(1+nr*self.width, 1+(nr+1)*self.width))
            self.layout.append(row)
        self.layout[self.height-1][self.width-1] = 0
        self.hole = (self.height-1, self.width-1)

        self.shuffle()

    def shuffle(self, times=10000):
        for _ in range(times):
            direction = int(random.random() * 4)
            if direction > 3:
                direction = 3
            self.move(direction)

    def move(self, direction: int) -> bool:
        # direction: 0-UP, 1-DOWN, 2-LEFT, 3-RIGHT
        # return: True-valid, False-invalid
        if self._valid_direction(direction):
            self._move(direction)
            return True
        else:
            return False

    def _valid_direction(self, direction: int):
        if direction > 3 or direction < 0:
            return False
        if direction == 0 and self.hole[0] >= self.height-1:
            return False
        if direction == 1 and self.hole[0] <= 0:
            return False
        if direction == 2 and self.hole[1] >= self.width-1:
            return False
        if direction == 3 and self.hole[1] <= 0:
            return False
        return True

    def _move(self, direction):
        i1, j1 = self.hole
        i2, j2 = i1, j1
        if direction == 0:
            i2 = i1 + 1
            j2 = j1
        if direction == 1:
            i2 = i1 - 1
            j2 = j1
        if direction == 2:
            i2 = i1
            j2 = j1 + 1
        if direction == 3:
            i2 = i1
            j2 = j1 - 1
        # swap
        self.layout[i1][j1], self.layout[i2][j2] = self.layout[i2][j2], self.layout[i1][j1]
        self.hole = (i2, j2)

    def is_ordered(self):
        if self.hole != (self.height-1, self.width-1):
            return False
        for i in range(self.height):
            for j in range(self.width):
                if self.layout[i][j] != 0 and self.layout[i][j] != i*self.width+j+1:
                    return False
        return True

    def __str__(self):
        str_repr = ''
        for row in self.layout:
            str_repr += '  '.join(map(lambda x: '%02d' % x if x != 0 else '  ', row))
            str_repr += '\n'
        return str_repr[:-1]


class SlidePuzzle():
    def __init__(self, height=4, width=4):
        self.board = Board(height, width)

    def is_win(self):
        return self.board.is_ordered()

    def move(self, direction):
        return self.board.move(direction)

    def get_direction_from_keyboard(self):
        while True:
            key = getch()
            if key == '\x1b[A':
                return 0
            if key == '\x1b[B':
                return 1
            if key == '\x1b[D':
                return 2
            if key == '\x1b[C':
                return 3

    def get_direction_from_keyboard(self):

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == '__main__':
    game = SlidePuzzle()
    os.system("clear")
    print(game.board)
    while not game.is_win():
        # direction = int(input('Input position (0-UP 1-DOWN 2-LEFT 3-RIGHT): \n'))
        direction = game.get_direction_from_keyboard()
        if direction == -1:
            print('direction -1')
            sys.exit(0)
        if not game.move(direction):
            continue
        os.system("clear")
        print(game.board)
    print('Game Win')
