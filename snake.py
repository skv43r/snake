# TODO: Создай класс Snake.
# Task 1: Определи начальные параметры: начальные позиции, расстояние движения и направления.
# Task 2: Создай список сегментов змейки и добавь первый сегмент как голову.
# Task 3: Напиши метод для создания змейки из нескольких сегментов.
# Task 4: Напиши метод для добавления сегмента к змейке.
# Task 5: Напиши метод для увеличения длины змейки (добавление сегмента).
# Task 6: Напиши метод для движения змейки, где каждая часть тела следует за предыдущей.
# Task 7: Напиши методы для изменения направления движения змейки (вверх, вниз, влево, вправо).

import turtle

class Snake():
    def __init__(self, position=(0, 0), length = 1, direction='Stop'):
        self.position =  position
        self.length = length
        self.direction = direction
    
    def head(self):
        head = turtle.Turtle()
        head.shape('square')
        head.color('green')
        head.penup()
        head.goto(self.position)


turtle.shape('circle')

turtle.done()