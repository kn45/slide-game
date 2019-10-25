# _*_coding:utf -8 _*_
import pygame
import sys
import random
from enum import Enum

pygame.init()

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class PuzzleNumbers(object):
    def __init__(self):
        super().__init__()
        self.puzzle_blocks = []
        self.arry_list = list(range(1, 16))
        self.arry_list.append(0)
        self.zero_row = 0
        self.zero_column = 0
        self.window = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('slide puzzle')

        self.font_obj = pygame.font.Font(None, 50)
        # 背景颜色
        self.window.fill((184, 200, 255))

        self.PuzzleInit()
        self.UpdateBlocks()

        pygame.display.flip()

# 生成数组并随机打乱
    def PuzzleInit(self):
        for row in range(4):
            self.puzzle_blocks.append([])
            for column in range(4):
                number = self.arry_list[row * 4 + column]
                self.puzzle_blocks[row].append(number)
                if number == 0:
                    self.zero_row = row
                    self.zero_column = column
        # 随机移动一下
        for i in range(500):
            random_number = random.randint(0, 3)
            self.move(Direction(random_number))

        self.UpdateBlocks()
# 画方块
    def UpdateBlocks(self):
        for i in range(4):  # row
            for j in range(4):  # column
                pygame.draw.rect(self.window, (255, 255, 255), (j * 100, i * 100, 98, 98))
                if self.puzzle_blocks[i][j] != 0:
                    # render: draw text on a new Surface
                    number_block = self.font_obj.render(str(self.puzzle_blocks[i][j]), True, (0, 0, 0))
                    # blit : draw one image onto another
                    self.window.blit(number_block, (j * 100 + 30, i * 100 + 30))
# 按键
    def KeyPressed(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                self.move(Direction.LEFT)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                self.move(Direction.RIGHT)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.move(Direction.UP)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.move(Direction.DOWN)
        self.UpdateBlocks()
        if PuzzleGame.if_success():
            print('Clear')

# 判断游戏是否成功
    def if_success(self):
        if self.puzzle_blocks[self.zero_row][self.zero_column] != (3,3):
            return False
        for row in range(4):
            for column in range(4):
                if self.puzzle_blocks[row][column] != 4 * row + column + 1:
                    return False
        return True
# 移动数字
    def move(self, direction):
        if direction == Direction.LEFT:
            if self.zero_column != 3:
                self.puzzle_blocks[self.zero_row][self.zero_column] = self.puzzle_blocks[self.zero_row][self.zero_column + 1]
                self.puzzle_blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if direction == Direction.RIGHT:
            if self.zero_column != 0:
                self.puzzle_blocks[self.zero_row][self.zero_column] = self.puzzle_blocks[self.zero_row][self.zero_column - 1]
                self.puzzle_blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1
        if direction == Direction.UP:
            if self.zero_row != 3:
                self.puzzle_blocks[self.zero_row][self.zero_column]= self.puzzle_blocks[self.zero_row + 1][self.zero_column]
                self.puzzle_blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if direction == Direction.DOWN:
            if self.zero_row != 0:
                self.puzzle_blocks[self.zero_row][self.zero_column]= self.puzzle_blocks[self.zero_row - 1][self.zero_column]
                self.puzzle_blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1

if __name__ == '__main__':
    PuzzleGame = PuzzleNumbers()
# 游戏主体循环部分
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                PuzzleGame.KeyPressed()
        pygame.display.update()


