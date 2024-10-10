# TODO: Создай класс Food(Turtle).
# Task 1: Установи форму еды в круг, уменьшай размер до половины, установи цвет и скорость. +
# Task 2: Напиши метод для случайного перемещения еды на новое место. +
from  turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, size=1.5, color='red', shape='circle', speed=0):
        super().__init__()
        self.initial_size = size
        self.current_size = size
        self.shapesize(size)
        self.color(color)
        self.shape(shape)
        self.speed(speed)
        self.penup()
        self.move_to_new_position()
        
        
    def move_to_new_position(self):
        self.current_size /= 2
        if self.current_size < 0.5:  
            self.current_size = 0.5
        self.shapesize(self.current_size)

        radius = int(10 * self.current_size / 2)  
        new_x = randint(-280 + radius, 280 - radius)
        new_y = randint(-280 + radius, 280 - radius)

        while (new_x, new_y) == (self.xcor(), self.ycor()):
            new_x = randint(-280 + radius, 280 - radius)
            new_y = randint(-280 + radius, 280 - radius)

        self.setposition(new_x, new_y)  
 
