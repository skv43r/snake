# TODO: Создай класс Snake.
# Task 1: Определи начальные параметры: начальные позиции, расстояние движения и направления.
# Task 2: Создай список сегментов змейки и добавь первый сегмент как голову.
# Task 3: Напиши метод для создания змейки из нескольких сегментов.
# Task 4: Напиши метод для добавления сегмента к змейке.
# Task 5: Напиши метод для увеличения длины змейки (добавление сегмента).
# Task 6: Напиши метод для движения змейки, где каждая часть тела следует за предыдущей.
# Task 7: Напиши методы для изменения направления движения змейки (вверх, вниз, влево, вправо).

import turtle

class Snake(turtle.Turtle):
    def __init__(self, size=1, color='green', shape='square', speed=1, position=(0, 0), length = 1, direction='Right'):
        super().__init__()
        self.size = size
        self.shapesize(size)
        self.color(color)
        self.shape(shape)
        self.speed(speed)
        self.penup()
        self.setposition(position)
        self.direction = direction

    def move(self):
        x, y = self.position()
        if self.direction == 'Up' and y != 300 - int(10 * self.size):
            self.setposition(x, y + 10)
            print(self.pos())
        elif self.direction == 'Down' and y != - 300 + int(15 * self.size):
            self.setposition(x, y - 10)
            print(self.pos())
        elif self.direction == 'Left':
            self.setposition(x - 10, y)
        elif self.direction == 'Right':
            self.setposition(x + 10, y)    


        


window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('My Snake Game')


back = Snake()
snake = [back]

def move_up():
    back.direction = 'Up'
    back.move()
    window.update()


def move_down():
    back.direction = 'Down'
    back.move()
    window.update()


def move_left():
    back.direction = 'Left'
    back.move()
    window.update()


def move_right():
    back.direction = 'Right'
    back.move()
    window.update()        
    

def update_snake():
    back.move()
    window.update()
    window.ontimer(update_snake, 100)
            
window.onkey(move_up, 'w')
window.onkey(move_down, 's') 
window.onkey(move_left, 'a') 
window.onkey(move_right, 'd')


window.listen()
update_snake()
window.tracer(25, 0)
window.mainloop()