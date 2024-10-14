# TODO: Создай класс Scoreboard(Turtle).
# Task 1: Определи настройки выравнивания и шрифта для текста. +
# Task 2: Установи начальный счет и настрой внешний вид счетчика.
# Task 3: Напиши метод для обновления отображаемого счета.
# Task 4: Напиши метод для отображения сообщения "GAME OVER".
# Task 5: Напиши метод для увеличения счета и его обновления на экране.

from turtle import Turtle
import csv

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('pink')
        self.penup()
        self.hideturtle()
        self.count = 0


    def read_high_score(self):
        high_score = 0
        try:
            with open('high_score.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = [int(row[0]) for row in reader]
                if rows:
                    high_score = max(rows)
        except ValueError:
            pass  
        return high_score

        
    def score(self):
        self.clear()
        self.setposition(-298, 270)
        self.high_score = self.read_high_score()
        self.write(f'Score: {self.count}\nHigh score: {self.high_score}', move=True, align='left', font=('Arial', 12, 'bold',))
    

    def write_hight_score(self, score):
        with open('high_score.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([score])


    def update_count(self):
        self.count += 1
        if self.count > self.high_score:
            self.high_score = self.count
            self.write_hight_score(self.high_score)
        self.score()


    def game_over(self):
        self.setposition(-125, 0)
        self.color('red')
        self.write(f'GAME OVER ', move=True, align='left', font=('Arial', 30, 'bold',))
