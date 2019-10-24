# _*_coding:utf -8 _*_
import pygame
import sys
pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('slide puzzle')


window.fill((184, 200, 255))
pygame.draw.rect(window, (255,255,255), (0, 0, 98, 98))
pygame.display.flip()

#
#
# class PuzzleNumbers(object):
#     def __init__(self):
#         self.puzzle_blocks = []
#         self.arry_list = list(range(1, 16))
#         self.arry_list.append(0)
#         self.zero_row = 0
#         self.zero_column = 0
# # 生成数组
#     def PuzzleInit(self):
#         for row in range(4):
#             self.puzzle_blocks.append([])
#             for column in range(4):
#                 number = self.arry_list[row * 4 + column]
#                 self.puzzle_blocks[row].append(number)
#                 if number == 0:
#                     self.zero_row = row
#                     self.zero_column = column
#
# # 按键
#     def KeyPress(self, event):
#         if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_d:
#                 self.move('LEFT')
#             if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
#                 self.move('RIGHT')
#             if event.key == pygame.K_UP or event.key == pygame.K_w:
#                 self.move('UP')
#             if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#                 self.move('DOWN')
# #判断游戏是否成功
#     def if_success(self):
#         if self.puzzle_blocks[self.zero_row][self.zero_column] != [3][3]:
#             return False
#         for row in range(4):
#             for column in range(4):
#                 if self.puzzle_blocks[row][column] != 4 * row + column + 1:
#                     return False
#         return True
# # 移动数字
#     def move(self, direction):
#         if direction == 'LEFT':
#             if self.zero_column != 3:
#                 self.puzzle_blocks[self.zero_row][self.zero_column] = self.puzzle_blocks[self.zero_row][self.zero_column + 1]
#                 self.puzzle_blocks[self.zero_row][self.zero_column + 1] = 0
#                 self.zero_column += 1
#         if direction == 'RIGHT':
#             if self.zero_column != 0:
#                 self.puzzle_blocks[self.zero_row][self.zero_column] = self.puzzle_blocks[self.zero_row][self.zero_column - 1]
#                 self.puzzle_blocks[self.zero_row][self.zero_column - 1] = 0
#                 self.zero_column -= 1
#         if direction == 'UP':
#             if self.zero_row != 3:
#                 self.puzzle_blocks[self.zero_row][self.zero_column]= self.puzzle_blocks[self.zero_row + 1][self.zero_column]
#                 self.puzzle_blocks[self.zero_row +1][self.zero_column] = 0
#                 self.zero_row += 1
#         if direction == 'DOWN':
#             if self.zero_row != 0:
#                 self.puzzle_blocks[self.zero_row][self.zero_column]= self.puzzle_blocks[self.zero_row - 1][self.zero_column]
#                 self.puzzle_blocks[self.zero_row - 1][self.zero_column] = 0
#                 self.zero_row -= 1

# 游戏主体循环部分
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
