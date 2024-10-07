# TODO: Создай игру "Змейка".
# Task 1: Создай окно игры с размером 600x600, черным фоном и названием "My Snake Game".
# Task 2: Отключи анимацию экрана, чтобы управлять обновлением вручную.
# Task 3: Создай объект змейки, еды и счетчика очков.
# Task 4: Настрой управление: привяжи стрелки клавиатуры к методам управления змейкой.
# Task 5: Запусти игровой цикл.
    # Task 5.1: Обнови экран и добавь задержку для плавного движения.
    # Task 5.2: Определи, произошло ли столкновение с едой. Если да, перемести еду, увеличь змейку и увеличь счет.
    # Task 5.3: Проверь, столкнулась ли змейка со стеной. Если да, останови игру и покажи сообщение "GAME OVER".
    # Task 5.4: Проверь, столкнулась ли змейка с собственным хвостом. Если да, останови игру и покажи сообщение "GAME OVER".
# Task 6: Заверши работу программы, когда пользователь закроет окно.

import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def main():

    window = turtle.Screen()
    window.setup(width=600, height=600)
    window.bgcolor('black')
    window.title('Моя игра Змейка')

    turtle.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    scoreboard.score()

    turtle.update()

    window.listen()
    window.onkey(snake.move_up, 'Up')
    window.onkey(snake.move_down, 'Down')
    window.onkey(snake.move_left, 'Left')
    window.onkey(snake.move_right, 'Right')
    turtle.tracer(0) 


    def check_collision_with_food():
        if snake.body[0].distance(food) < 15:
            snake.add_segment()
            food.move_to_new_position()
            scoreboard.update_count()
            scoreboard.score()


    def update():
        try:
            if snake.check_collision_with_self():
                scoreboard.game_over()
                turtle.done()
            turtle.update()
            check_collision_with_food()
            
            snake.update_snake()
            window.ontimer(update, 100)  
        except turtle.Terminator:
            pass
                 
    update()
    window.mainloop()


if __name__ == "__main__":
    main()