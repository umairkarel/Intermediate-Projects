""" 
    Created on Mon March 15 2021

    @author: umairkarel
"""

import pygame
class Board:
    def __init__(self, n, width, height, screen):
        self.rows = n
        self.cols = n
        self.width = width
        self.height = height
        self.screen = screen
        self.model = [[1 for i in range(self.rows)] for j in range(self.cols)]

    def place(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width // self.rows
            x = pos[1] // gap
            y = pos[0] // gap

            c = self.model[x][y]
            self.model[x][y] = 0 if c else 1

            return True

        return False

    def draw(self):
        gap = self.width // self.rows
        color = (0,0,0)

        for i in range(self.rows+1):
            pygame.draw.line(self.screen, color, (0,i*gap), (self.width,i*gap), 1)
            pygame.draw.line(self.screen, color, (i*gap,0), (i*gap,self.height), 1)

        for x in range(self.rows):
            for y in range(self.cols):
                if self.model[x][y] == 0:
                    x1, y1 = y*gap, x*gap
                    width, height = gap, gap
                    pygame.draw.rect(self.screen, color, pygame.Rect(x1,y1,width,height))



#####################################

# import pygame
# class Board:
#     def __init__(self, n, width, height, screen):
#         self.rows = n
#         self.cols = n
#         self.width = width
#         self.height = height
#         self.screen = screen
#         self.model = [[1 for i in range(self.rows)] for j in range(self.cols)]

#     def place(self, pos):
#         if pos[0] < self.width and pos[1] < self.height:
#             gap = self.width // self.rows
#             x = pos[1] // gap
#             y = pos[0] // gap

#             c = self.model[x][y]
#             self.model[x][y] = 0 if c else 1

#             return True

#         return False

#     def draw(self):
#         gap = self.width // self.rows
#         color = (0,0,0)

#         for i in range(self.rows+1):
#             pygame.draw.line(self.screen, color, (0,i*gap), (self.width,i*gap), 1)
#             pygame.draw.line(self.screen, color, (i*gap,0), (i*gap,self.height), 1)

#         for x in range(self.rows):
#             for y in range(self.cols):
#                 if self.model[x][y] == 0:
#                     x1, y1 = y*gap, x*gap
#                     width, height = gap, gap
#                     pygame.draw.rect(self.screen, color, pygame.Rect(x1,y1,width,height))