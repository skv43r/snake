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
    def __init__(self,
                size=1,
                position=(0, 0),
                length = 2,
                direction='Right'):
        super().__init__()
        self.size = size
        self.setposition(position)
        self.direction = direction
        self.body = []
        self.create_snake(length)

    def move(self):
        x, y = self.position()
        if self.direction == 'Up' and y != 300 - 10 * self.size:
            self.setposition(x, y + 10)
        elif self.direction == 'Down' and y != -300 + 10 * (self.size + 1):
            self.setposition(x, y - 10)
        elif self.direction == 'Left' and x != -300 + 10 * self.size:
            self.setposition(x - 10, y)
        elif self.direction == 'Right' and x != 300 - 10 * (self.size + 1):
            self.setposition(x + 10, y)


    def create_snake(self, length):
        start_x = 0
        for i in range(length):
            segment = turtle.Turtle()
            segment.shape('square')
            segment.color('green')
            segment.shapesize(1)
            segment.speed(0)
            segment.penup()
            segment.setposition(start_x - i * (10 * (self.size + 1)), 0)
            self.body.append(segment)


    def update_snake(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].setposition(self.body[i-1].position())
            self.body[0].setposition(self.position())
        self.move()
        turtle.update()
        turtle.ontimer(self.update_snake, 100)        


    def change_direction(self, direction):
        self.direction = direction         

    def move_up(self):
        self.change_direction('Up')

    def move_down(self):
        self.change_direction('Down')

    def move_left(self):
        self.change_direction('Left')

    def move_right(self):
        self.change_direction('Right')     



window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Моя игра Змейка')

snake = Snake()


window.onkey(snake.move_up, 'Up')
window.onkey(snake.move_down, 'Down')
window.onkey(snake.move_left, 'Left')
window.onkey(snake.move_right, 'Right')
window.listen()

snake.update_snake()
window.mainloop()