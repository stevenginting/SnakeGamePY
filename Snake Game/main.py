# Main Game File
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from papanboard import Papanboard
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Inisialisasi objek
snake = Snake()
food = Food()
papan = Papanboard()

# Setup kontrol
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Game loop
game_mulai = True
while game_mulai:
    time.sleep(0.1)  # Snake bergerak lebih pelan
    screen.update()
    snake.move()

    # Mendeteksi makanan
    if snake.head.distance(food) < 15:
        food.refresh()
        papan.Tambah_score()

        # Jika skor lebih dari 3, ekor ular lebih cepat bertambah
        if papan.score > 3:
            snake.memperpanjang()
            snake.memperpanjang()  # Tambahkan ekor dua kali lebih cepat
        else:
            snake.memperpanjang()

    # Mendeteksi tabrakan dengan dinding
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        papan.Kurangi_strike()
        if papan.strike == 0:
            game_mulai = False
            papan.papan_kalah()

    # Mendeteksi tabrakan dengan tubuh sendiri
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            papan.Kurangi_strike()
            if papan.strike == 0:
                game_mulai = False
                papan.papan_kalah()

screen.exitonclick()