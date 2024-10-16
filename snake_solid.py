# TODO: Создай класс Snake.
# Task 1: Определи начальные параметры: начальные позиции, расстояние движения и направления. +
# Task 2: Создай список сегментов змейки и добавь первый сегмент как голову. +
# Task 3: Напиши метод для создания змейки из нескольких сегментов. +
# Task 4: Напиши метод для добавления сегмента к змейке. +
# Task 5: Напиши метод для увеличения длины змейки (добавление сегмента). +
# Task 6: Напиши метод для движения змейки, где каждая часть тела следует за предыдущей. +
# Task 7: Напиши методы для изменения направления движения змейки (вверх, вниз, влево, вправо). +

from turtle import Turtle

class Direction:
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'


class Segment(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.shapesize(1)
        self.speed(0)
        self.penup()


class Snake:
    def __init__(self,
                size=1,
                length = 2):
        self.size = size
        self.body = []
        self.direction = Direction.RIGHT
        self.create_snake(length)

    def create_snake(self, length):
        for i in range(length):
            self.add_segment((-i, 0))

    def add_segment(self, position):
        segmaent = Segment()
        segmaent.setposition(position)
        self.body.append(segmaent)

    def extend(self):
        self.add_segment(self.body[-1].position())
        
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].setposition(self.body[i - 1].position())
        self.body[0].forward(10)

    def change_direction(self, new_direction):
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction
            self.body[0].setheading(self._direction_to_angle(new_direction))
    
    def _direction_to_angle(self, direction):
        return {
            Direction.UP: 90,
            Direction.DOWN: 270,
            Direction.LEFT: 180,
            Direction.RIGHT: 0
        }.get(direction, 0)    

    def move_up(self):
        self.change_direction(Direction.UP)

    def move_down(self):
        self.change_direction(Direction.DOWN)

    def move_left(self):
        self.change_direction(Direction.LEFT)

    def move_right(self):
        self.change_direction(Direction.RIGHT) 


class CollisionDetector:
    def __init__(self, snake) -> None:
        self.snake = snake

    def check_collision_with_walls(self):
        head = self.snake.body[0]
        x, y = head.position()
        return (x < -290 or x > 280 or y < -280 or y > 290)

    def check_collision_with_self(self):
        head = self.snake.body[0]
        for segment in self.snake.body[2:]:
            if head.distance(segment) < 10:
                return True
        return False
  