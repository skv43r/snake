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
                color='green',
                shape='square',
                speed=100,
                position=(0, 0),
                length = 1,
                direction='Right'):
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
        if self.direction == 'Up' and y != 300 - 10 * self.size:
            self.setposition(x, y + 10)
        elif self.direction == 'Down' and y != -300 + 10 * (self.size + 1):
            self.setposition(x, y - 10)
        elif self.direction == 'Left' and x != -300 + 10 * self.size:
            self.setposition(x - 10, y)
        elif self.direction == 'Right' and x != 300 - 10 * (self.size + 1):
            self.setposition(x + 10, y)    


class SnakeGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(width=600, height=600)
        self.window.bgcolor('black')
        self.window.title('My Snake Game')
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(10):
            snake = Snake()
            self.snake.append(snake)

    def move_up(self):
        self.snake[0].direction = 'Up'

    def move_down(self):
        self.snake[0].direction = 'Down'

    def move_left(self):
        self.snake[0].direction = 'Left'

    def move_right(self):
        self.snake[0].direction = 'Right'

    def update_snake(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i-1].position())
        self.snake[0].move()
        self.window.update()
        self.window.ontimer(self.update_snake, 100)

    def start_game(self):
        self.window.onkey(self.move_up, 'w')
        self.window.onkey(self.move_down, 's')
        self.window.onkey(self.move_left, 'a')
        self.window.onkey(self.move_right, 'd')
        self.window.listen()
        self.update_snake()
        self.window.mainloop()

game = SnakeGame()
game.start_game()