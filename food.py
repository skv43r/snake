# TODO: Создай класс Food(Turtle).
# Task 1: Установи форму еды в круг, уменьшай размер до половины, установи цвет и скорость. +
# Task 2: Напиши метод для случайного перемещения еды на новое место. +
import turtle
import random

class Food(turtle.Turtle):

    def __init__(self, size=1.5, color='red', shape='circle', speed=0):
        super().__init__()
        self.initial_size = size
        self.current_size = size
        self.shapesize(size)
        self.color(color)
        self.shape(shape)
        self.speed(speed)
        self.penup()
        
        
    def move_to_new_position(self):
        self.current_size /= 2
        if self.current_size < 0.5:  
            self.current_size = 0.5
        self.shapesize(self.current_size)

        radius = int(10 * self.current_size / 2)  
        new_x = random.randint(-300 + radius, 300 - radius)
        new_y = random.randint(-300 + radius, 300 - radius)

        while (new_x, new_y) == (self.xcor(), self.ycor()):
            new_x = random.randint(-300 + radius, 300 - radius)
            new_y = random.randint(-300 + radius, 300 - radius)

        self.goto(new_x, new_y)
            

window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('My Snake Game')
food = Food()

food.move_to_new_position()
food.move_to_new_position()
food.move_to_new_position()
food.move_to_new_position()
food.move_to_new_position()
food.move_to_new_position()


turtle.mainloop()  
