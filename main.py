import os
import random

import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 340:
            self.setx(340)
            self.rt(60)

        if self.xcor() < -340:
            self.setx(-340)
            self.rt(60)

        if self.ycor() > 340:
            self.sety(340)
            self.rt(60)

        if self.ycor() < -340:
            self.sety(-340)
            self.rt(60)

class Player(Sprite):
    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-350, 350)
        self.pen.pendown()
        for side in range(4):
            self.pen.forward(700)
            self.pen.right(90)
        self.pen.penup()
        self.pen.ht()



game = Game()

game.draw_border()

player = Player("triangle", "white", 0, 0)

turtle.onkey(player.turn_left, "a")
turtle.onkey(player.turn_right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.decelerate, "s")
turtle.listen()


while True:
    player.move()




