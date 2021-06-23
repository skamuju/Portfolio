#Made by John Gamble and Saketh Kamuju
#We highly recommend that you try play this game in a different text editor than repl.
"""
This game was developed in Python and is based off of the popular IOS game color Switch. The objective of the game is to 
survive as long as possible. You can move through obstacles by matching your palyer's color. The player can be controlled
using the arrow keys and the colors can be swapped by pressing Z. At the end of the game you will recieve a score.
"""


import pygame
import sys
import time
import random

pygame.init()

#Window Settings:
FRAME_RATE = 30
win_x = 850
win_y = 850
window = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("Color Fall 24")

#Game Variables:
score = 0
x_pos = int(win_x/2)
y_pos = int(win_y/2)
rect_x1 = 0
rect_y1 = 0
rect_x2 = win_x/2
rect_y2 = 0
rect_color1 = 0
rect_color2 = 1
delta = 1
game_run = True
collide = True

#Color Variables:
White = (225, 225, 225)
Purple = (128, 0, 128)
Yellow = (255, 255, 0)
LightCoral = (240, 128, 128)
SteelBlue = (70, 130, 180)
MediumSpringGreen = (0, 250, 154)
Black = (0, 0, 0)
Blue = (0, 0, 225)
Green = (0, 225, 0)
Red = (225, 0, 0)
Colors = [White, Purple, Yellow]
Color = int(0)


class Player:

  def __init__(self, surface, color, x, y, radius, velocity):

    self.surface = surface
    self.color = color
    self.x = x
    self.y = y
    self.position = (x, y)
    self.radius = radius
    self.velocity = velocity
    self.hit = (x - radius, y-radius, 20, 20)

  def spawn(self):

    pygame.draw.rect(self.surface, Black, [
                     self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2])
    pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)


player = Player(window, Colors[Color], 600, 600, 20, 5)


class Rectangle:

  def __init__(self, surface, color, x, y, length, width):
    self.surface = surface
    self.color = color
    self.x = x
    self.y = y
    self.position = (x, y)
    self.length = length
    self.width = width
    self.dimensions = (length, width)
    self.hit = (x, y, length, width)

  def create_rect(self):
    pygame.draw.rect(self.surface, self.color, [
                     self.x, self.y, self.length, self.width])


rect1 = Rectangle(window, Colors[1], 0, 0, win_x/2, 100)
rect2 = Rectangle(window, Colors[2], win_x/2, 0, win_x/2, 100)

game_key = True

while game_key == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit

    if rect1.y <= win_y:
      rect1.y += delta
      rect2.y += delta
    else:
      if score % 5 == 0:
        delta += 1
      score += 1
      rect1.color = Colors[random.randint(0, 2)]
      rect2.color = Colors[random.randint(0, 2)]
      while rect1.color == rect2.color:
        rect2.color = Colors[random.randint(0, 2)]
      rect1.y = 0
      rect2.y = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] == True:
      game_key = False
    if keys[pygame.K_UP] == True and 20 < player.y:
      player.y -= player.velocity
    if keys[pygame.K_DOWN] == True and player.y < win_y-player.radius:
      player.y += player.velocity
    if keys[pygame.K_RIGHT] == True and player.x < win_x-player.radius:
      player.x += player.velocity
    if keys[pygame.K_LEFT] == True and 20 < player.x:
      player.x -= player.velocity
    if keys[pygame.K_z] == True:
      if Color >= 2:
        Color = 0
        player.color = Colors[Color]
      else:
        Color += 1
        player.color = Colors[Color]
      time.sleep(0.1)

    if player.x - 20 <= rect1.x + rect1.length and player.y - 20 <= rect1.y + rect1.width and player.color != rect1.color and player.y+20 > rect1.y:
      game_key = False
      print("Game Over!")
      print("Score: {}".format(score))

    if player.x-20 >= rect2.x and player.y-20 <= rect2.y + rect2.width and player.y+20 >= rect2.y and player.color != rect2.color:
      game_key = False
      print("Game Over!")
      print("Score: {}".format(score))

    window.fill(Black)
    Player.spawn(player)
    Rectangle.create_rect(rect1)
    Rectangle.create_rect(rect2)
    pygame.display.update()

pygame.quit()
