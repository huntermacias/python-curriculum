import turtle 
import time

snake = turtle.Turtle()
food = turtle.Turtle()
win = turtle.Screen()

# IF CAPITALIZE - DON'T CHANGE VALUES BECAUSE THEY ARE CONSTANTS
WIDTH = 500 
HEIGHT = 500
win.setup(width=WIDTH, height=HEIGHT)
win.bgcolor("black")

snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(-200, 200)
snake.direction = "stop"

food.shape("circle")
food.color("red")
food.shapesize(0.5)


def move_up():
	snake.direction = "up"

def move_down():
	snake.direction = "down"

def move_left():
	snake.direction = "left"

def move_rigth():
	snake.direction = "right"

def move():
	snake_x = snake.xcor()
	snake_y = snake.ycor()
	move_by = 20
	# check the direction of snake
	# reassign value of snake using .sety(new_y) & .setx(new_x)
	if snake.direction == "up":
		snake.sety(snake_y + move_by)
	if snake.direction == "down":
		snake.sety(snake_y - move_by)
	if snake.direction == "left":
		snake.setx(snake_x - move_by)
	if snake.direction == "right":
		snake.setx(snake_x + move_by)

	time.sleep(0.1)



def main():

	is_alive = True
	# W A S D
	win.listen()
	win.onkeypress(move_up, "w")
	win.onkeypress(move_down, "s")
	win.onkeypress(move_left, "a")
	win.onkeypress(move_rigth, "d")

	while is_alive: 
		win.update()
		move()

	

	turtle.mainloop() # keeps our window from closing

main()






