import enum
import os
import pygame
import random
import sys
import time

pygame.init()


class MOVE(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Board():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        # init layout
        self.layout = []
        for nr in range(self.height):
            row = list(range(1+nr*self.width, 1+(nr+1)*self.width))
            self.layout.append(row)
        self.hole_value = (self.height) * (self.width)
        self.hole_pos = (self.height-1, self.width-1)

        self.shuffle()

    def shuffle(self, times=10000):
        for _ in range(times):
            move = MOVE(random.randint(0, len(MOVE)-1))
            if self.is_valid_move(move):
                self.move(move)

    def is_valid_move(self, move: MOVE):
        if move == MOVE.UP and self.hole_pos[0] >= self.height-1:
            return False
        if move == MOVE.DOWN and self.hole_pos[0] <= 0:
            return False
        if move == MOVE.LEFT and self.hole_pos[1] >= self.width-1:
            return False
        if move == MOVE.RIGHT and self.hole_pos[1] <= 0:
            return False
        return True

    def move(self, move):
        # NOT SAFE MOVE!!! USE AFTER VALIDITY CHECK!!!
        i1, j1 = self.hole_pos
        i2, j2 = i1, j1
        if move == MOVE.UP:
            i2 = i1 + 1
            j2 = j1
        if move == MOVE.DOWN:
            i2 = i1 - 1
            j2 = j1
        if move == MOVE.LEFT:
            i2 = i1
            j2 = j1 + 1
        if move == MOVE.RIGHT:
            i2 = i1
            j2 = j1 - 1
        # swap
        self[i1][j1], self[i2][j2] = self[i2][j2], self[i1][j1]
        self.hole_pos = (i2, j2)

    def is_ordered(self):
        for i in range(self.height):
            for j in range(self.width):
                if self[i][j] != i*self.width+j+1:
                    return False
        return True

    def __str__(self):
        str_repr = ''
        for row in self.layout:
            str_repr += '  '.join(map(lambda x: '%02d' % x if x != self.hole_value else '  ', row))
            str_repr += '\n'
        return str_repr[:-1]

    def __getitem__(self, nr):
        return self.layout[nr]


class GameGUI():
    def __init__(self, board):
        self.board = board

    def draw_initial_game(self):
        raise NotImplementedError

    def draw_move(self, move):
        raise NotImplementedError

    def draw_win(self):
        raise NotImplementedError


class GUIPygame(GameGUI):
    def __init__(self, board):
        super().__init__(board)

        self.window = pygame.display.set_mode((400, 400))
        self.font_obj = pygame.font.Font(None, 50)

    def draw_initial_game(self):
        pygame.display.set_caption('slide puzzle')
        self.window.fill((184, 200, 255))
        self._redraw_all()

    def draw_move(self, move):
        self._redraw_all()

    def draw_win(self):
        pass

    def _redraw_all(self):
        for i in range(self.board.height):  # row
            for j in range(self.board.width):  # column
                pygame.draw.rect(self.window, (255, 255, 255), (j * 100, i * 100, 98, 98))
                if self.board[i][j] != self.board.hole_value:
                    # render: draw text on a new Surface
                    number_block = self.font_obj.render(str(self.board[i][j]), True, (0, 0, 0))
                    # blit : draw one image onto another
                    self.window.blit(number_block, (j * 100 + 30, i * 100 + 30))
        pygame.display.update()
        pygame.event.pump()


class GUICLI(GameGUI):
    def __init__(self, board):
        super().__init__(board)

    def draw_initial_game(self):
        os.system("clear")
        print(self.board)

    def draw_move(self, move):
        os.system("clear")
        print(game.board)

    def draw_win(self):
        print('Game Win')


class SlidePuzzle():
    def __init__(self, height=4, width=4):
        self.board = Board(height, width)
        # self.gui = GUIPygame(self.board)
        self.gui = GUICLI(self.board)

    def is_win(self):
        return self.board.is_ordered()

    def init(self):
        self.gui.draw_initial_game()

    def do_move(self, move):
        if move is None:
            sys.exit(0)
        self.board.move(move)
        self.gui.draw_move(move)

    def do_win(self):
        self.gui.draw_win()


class Player():
    def __init__(self, game):
        self.game = game

    def choose_move(self) -> MOVE:
        raise NotImplementedError


class PlayerPygameKB(Player):
    def __init__(self, game):
        super().__init__(game)

    def choose_move(self) -> MOVE:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = MOVE.UP
                elif event.key == pygame.K_DOWN:
                    move = MOVE.DOWN
                elif event.key == pygame.K_LEFT:
                    move = MOVE.LEFT
                elif event.key == pygame.K_RIGHT:
                    move = MOVE.RIGHT
                else:
                    continue
                if self.game.board.is_valid_move(move):
                    return move


class PlayerCLI(Player):
    def __init__(self, game):
        super().__init__(game)

    def choose_move(self) -> MOVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        while True:
            try:
                inp = input('Input position (0-UP 1-DOWN 2-LEFT 3-RIGHT 9-EXIT): \n')
                if inp == '9':
                    return None
                move = MOVE(int(inp))
                if not self.game.board.is_valid_move(move):
                    raise Exception()
                return move
            except:
                print('WRONG INPUT!')


class PlayerRandom(Player):
    def __init__(self, game):
        super().__init__(game)

    def choose_move(self) -> MOVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        time.sleep(1)
        while True:
            move = MOVE(random.randint(0, len(MOVE)-1))
            if self.game.board.is_valid_move(move):
                return move


if __name__ == '__main__':
    game = SlidePuzzle()
    game.init()
    # player = PlayerPygameKB(game)
    player = PlayerRandom(game)
    # player = PlayerCLI(game)
    while not game.is_win():
        move = player.choose_move()
        game.do_move(move)
        pass
    game.do_win()
