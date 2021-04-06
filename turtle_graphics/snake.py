# built-in turtle library needed for all of turtle graphic functionality 
import turtle
import time
import random
from playsound import playsound

# create two different turtle objects - 1. our snake 2. our window that is in charge of just the screen
snake = turtle.Turtle()
food = turtle.Turtle()
window = turtle.Screen()

#CONSTANTS
WIDTH = 1000
HEIGHT = 900

# set the background of our screen 
window.bgcolor("light blue")
# set the title of the game 
window.title("Snake Game [MADE WITH TURTLE GRAPHICS]")
# set our window size 
window.setup(width=WIDTH, height=HEIGHT)
# turn off all window updates (we don't need to see anything constantly updated other than a scoreboard)
window.tracer(0)


# set the snakes shape
snake.shape("square")
# set the snakes starting pos & pickup pen because we aren't going to be drawing
snake.penup()
snake.goto(0,0)
# set the snakes speed to 0
snake.speed(0)
# set the direction of our snake to be stop because at the beginning of the game our snake shouldn't be moving until we tell it to
snake.direction = "Stop"

food.shape("circle")
food.penup()
food.goto(-150,350)
food.color("red")
food.shapesize(0.5)

scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.color("black")
scoreboard.hideturtle()

snakes_body = []

def move_up():
	snake.direction = "up"

def move_down():
	snake.direction = "down"

def move_left():
	snake.direction = "left"

def move_right():
	snake.direction = "right"

def check_out_of_bounds():
	if snake.xcor() > WIDTH/2: 
		snake.goto(-WIDTH/2, snake.ycor())
	
	if snake.xcor() < -WIDTH/2:
		snake.goto(WIDTH/2, snake.ycor())

	if snake.ycor() > HEIGHT/2: 
		snake.goto(snake.xcor(), -HEIGHT/2)

	if snake.ycor() < -HEIGHT/2: 
		snake.goto(snake.xcor(), HEIGHT/2)


def show_entire_snake():
	for i in range(len(snakes_body)-1, 0, -1):
		x = snakes_body[i-1].xcor()
		y = snakes_body[i-1].ycor()
		snakes_body[i].goto(x,y)
		if len(snakes_body) > 0: 
			x = snake.xcor() 
			y = snake.ycor() 
			snakes_body[0].goto(x, y)


def grow_snake():
	colors = ["orange", "green", "navy blue", "red", "pink"]

	new_snake = turtle.Turtle()
	new_snake.color(random.choice(colors))
	new_snake.shape("square")
	new_snake.penup()
	new_snake.speed(0)
	snakes_body.append(new_snake)
	for i in range(len(snakes_body)-1, 0, -1):
		x = snakes_body[i-1].xcor()
		y = snakes_body[i-1].ycor()
		snakes_body[i].goto(x,y)
		if len(snakes_body) > 0: 
			x = snake.xcor() 
			y = snake.ycor() 
			snakes_body[0].goto(x, y)



def move_food():
	# choose a new random x & y with our widhth and height as ranges
	random_x = random.randint(-WIDTH/2+20, WIDTH/2-20)
	random_y = random.randint(-HEIGHT/2+20, HEIGHT/2-20)
	food.goto(random_x, random_y)

def update_score(score):
	scoreboard.undo()
	scoreboard.write(score, font=("Arial", 17, "italic"))

def check_eaten(score, delay):
	# get the coordinates for both our snake and food
	food_x = food.xcor()
	food_y = food.ycor()
	snake_x = snake.xcor()
	snake_y = snake.ycor()
# 				check if our x intersects 								#check if our y intersects
	if (snake_x <= food_x + 15) and (snake_x >= food_x - 15) and (snake_y <= food_y + 15) and (snake_y >= food_y - 15): 
		score += 1
		delay -= 0.008
		grow_snake()
		move_food()
		update_score(score)

	return score, delay


def check_body_collision():
	# this might be len()-1, 1, -1 ?
	for idx in range(len(snakes_body)-1, 0, -1):
		if snakes_body[idx].distance(snake) < 15: 
			return True

def display_score(score):
	x = -WIDTH/2+50
	y = HEIGHT/2-50
	scoreboard.goto(x, y-25)
	scoreboard.write("High Score: ", font=("Arial", 17, "italic")) # change this later
	scoreboard.goto(x, y)
	scoreboard.write("Score: ", font=("Arial", 17, "italic"))
	scoreboard.goto(x+70, y)
	scoreboard.write(score, font=("Arial", 17, "italic"))

def get_highscore(score, game_data):
	high_score = max(game_data.values())
	return high_score

def update_highscore(highscore):
	x = -WIDTH/2+175
	y = HEIGHT/2-75
	scoreboard.goto(x, y)
	scoreboard.write(highscore, font=("Arial", 17, "italic"))


def move(): 

	y = snake.ycor() # this is in charge of retrieving our y coord. from our snake (up & down)
	x = snake.xcor() # this is in charge of retrieving our x coord. from our snake (left & right)
	# we're going to write conditional statements to check what direction we want to go in
	if snake.direction == "up":
		snake.sety(y+20)
	if snake.direction == "down": 
		snake.sety(y-20)
	if snake.direction == "left": 
		snake.setx(x-20)
	if snake.direction == "right":
		snake.setx(x+20)


def main():

	# list we are going to use to randomize colors in our game and increase the speeds as the snake continues to find more and more food
	speeds = [10, 20, 30, 40, 50] 
	score = 0
	highscore = 0
	run_game = True
	delay = 0.1
	game_data = {} # this is going to score all of our games data. Format will look something like this => game#:score => {1:18, 2:6, 3:20...n:n-score}
	game_count = 1
	playsound("sounds/pacman_beginning.wav")


	window.listen()
	window.onkeypress(move_up, "w")
	window.onkeypress(move_down, "s")
	window.onkeypress(move_right, "d")
	window.onkeypress(move_left, "a")

	snakes_body.append(snake)
	food.goto(-50,0) # creates our first food item

	display_score(score)

	while True:
		playsound("sounds/pacman_chomp.wav", 0)
		# main loop for our game
		while run_game: 
			window.update()
			move()
			if check_body_collision():
				run_game = False
			check_out_of_bounds()
			score, delay = check_eaten(score, delay)
			show_entire_snake()
			time.sleep(delay)

		game_data[game_count] = score
		highscore = get_highscore(score, game_data)
		update_highscore(highscore)





	#this line of code keeps our window open
	turtle.mainloop()


main()
