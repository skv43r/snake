# TODO: Создай класс Snake.
# Task 1: Определи начальные параметры: начальные позиции, расстояние движения и направления. +
# Task 2: Создай список сегментов змейки и добавь первый сегмент как голову. +
# Task 3: Напиши метод для создания змейки из нескольких сегментов. +
# Task 4: Напиши метод для добавления сегмента к змейке. +
# Task 5: Напиши метод для увеличения длины змейки (добавление сегмента). +
# Task 6: Напиши метод для движения змейки, где каждая часть тела следует за предыдущей. +
# Task 7: Напиши методы для изменения направления движения змейки (вверх, вниз, влево, вправо). +

from turtle import Turtle
import turtle


class Snake(Turtle):
    def __init__(self,
                size=1,
                length = 2,
                direction='Right'):
        super().__init__()
        self.size = size
        self.direction = direction
        self.body = []
        self.start_snake(length)


    def create_segment(self):
        segment = Turtle()
        segment.shape('square')
        segment.color('green')
        segment.shapesize(1)
        segment.speed(0)
        segment.penup()
        self.body.append(segment)
        return segment


    def start_snake(self, length):
        start_x = 0
        for i in range(length):
            block = self.create_segment()
            block.setposition(start_x - i * (10 * (self.size + 1)), 0)
            self.body.append(block)
        self.body[0] = self


    def add_segment(self):
        new_segment = self.create_segment()
        new_segment.setposition(self.body[-1].position())
        self.body.append(new_segment)   


    def move(self):
        x, y = self.position()
        if self.direction == 'Up' and y < 300 - 10 * self.size:
            self.setposition(x, y + 10)
        elif self.direction == 'Down' and y > -300 + 10 * (self.size + 1):
            self.setposition(x, y - 10)
        elif self.direction == 'Left' and x > -300 + 10 * self.size:
            self.setposition(x - 10, y)
        elif self.direction == 'Right' and x < 300 - 10 * (self.size + 1):
            self.setposition(x + 10, y)


    def check_collision_with_walls(self):
        x, y = self.position()
        if self.is_collision_with_wall(x,y):
            return True
        else:
            self.move()
            return False

    
    def is_collision_with_wall(self, x, y):
        if self.direction == 'Up' and y == 300:
            return True
        elif self.direction == 'Down' and y == -300:
            return True
        elif self.direction == 'Left' and x == -300:
            return True
        elif self.direction == 'Right' and x == 300:
            return True
        return False


    def check_collision_with_self(self):
        head = self.body[0]
        for segment in self.body[2:]:
            if head.distance(segment) < 10:
                return True
        return False


    def update_snake(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].setposition(self.body[i - 1].position())
        self.body[0].move()  
    

    def change_direction(self, direction):
        self.direction = direction         

    def move_up(self):
        if self.direction != 'Down':
            self.change_direction('Up')

    def move_down(self):
        if self.direction != 'Up':
            self.change_direction('Down')

    def move_left(self):
        if self.direction != 'Right':
            self.change_direction('Left')

    def move_right(self):
        if self.direction != 'Left':
            self.change_direction('Right')     
