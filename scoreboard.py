# TODO: Создай класс Scoreboard(Turtle).
# Task 1: Определи настройки выравнивания и шрифта для текста. +
# Task 2: Установи начальный счет и настрой внешний вид счетчика.
# Task 3: Напиши метод для обновления отображаемого счета.
# Task 4: Напиши метод для отображения сообщения "GAME OVER".
# Task 5: Напиши метод для увеличения счета и его обновления на экране.

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('pink')
        self.penup()
        self.hideturtle()
        self.count = 0

        
    def score(self):
        self.clear()
        self.setposition(-298, 280)
        self.write(f'Score: {self.count}', move=True, align='left', font=('Arial', 12, 'bold',))
    
    def update_count(self):
        self.count += 1

    def game_over(self):
        self.setposition(-125, 0)
        self.color('red')
        self.write(f'GAME OVER ', move=True, align='left', font=('Arial', 30, 'bold',))
