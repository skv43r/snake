# TODO: Создай класс Scoreboard(Turtle).
# Task 1: Определи настройки выравнивания и шрифта для текста. +
# Task 2: Установи начальный счет и настрой внешний вид счетчика.
# Task 3: Напиши метод для обновления отображаемого счета.
# Task 4: Напиши метод для отображения сообщения "GAME OVER".
# Task 5: Напиши метод для увеличения счета и его обновления на экране.

import turtle

window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('My Snake Game')

class Scoreboard(turtle.Turtle):
    def __init__(self, position=(-298, 260)):
        super().__init__()
        self.color('pink')
        self.penup()
        self.hideturtle()
        self.goto(position)

        
    def count(self, count=0, high_score=0):

        self.write(f'Score: {count}\nHigh Score: {high_score}', move=True, align='left', font=('Arial', 12, 'bold',))



#turtle.hideturtle()
#turtle.penup()
#turtle.goto(-298, 280)
#turtle.color('pink')
#turtle.write(f'Score: {count}', move=True, align='left', font=('Arial', 12, 'bold',))

score = Scoreboard()
score.count()

turtle.mainloop()  