import turtle 
import random
import time

def create_turtle(shape="classic", color="teal"):
	gen_turtle = turtle.Turtle()
	gen_turtle.shape(shape)
	gen_turtle.color(color)
	gen_turtle.speed(0)
	gen_turtle.pensize(4)
	return gen_turtle

def create_lines(pen, coor_x, coor_y):
	pen.penup()
	pen.goto(coor_x, coor_y) 
	pen.pendown()
	pen.goto(coor_x, -coor_y)

def set_starting_positions(x, y):
	lonely_boi.penup()
	lonely_boi.goto(x, y)
	lonely_boi.pendown()

	lonely_bois_girlfriend.penup()
	lonely_bois_girlfriend.goto(x, -y + -50)
	lonely_bois_girlfriend.pendown()

def check_winner(distance, turtle):
	if distance >= 819: 
		cap = create_turtle()
		cap.hideturtle()
		cap.penup()
		cap.goto(-265, 175)
		cap.pendown()
		if turtle == 0: 
			cap.write("CONGRATULATIONS LONELY BOIIII!", font=('Arial', 22, 'bold'))
		else: 
			cap.write("CONGRATULATIONS LONELY BOIS GF!", font=('Arial', 22, 'bold'))

def display_distances(captain):
	captain.penup()
	captain.goto(-450, 380)
	captain.write("Lonely Boi Distance Traveled: ", font=('Arial', 12, 'bold'))
	captain.goto(-450, 350)
	captain.write("Lonely Bois GF Distance Traveled: ", font=('Arial', 12, 'bold'))

def update_distances(captain, dist1, dist2):
	captain._tracer(50)
	captain.goto(-220, 380)
	captain.write(dist1, font=('Arial', 12, 'bold'))
	captain.goto(-185, 350)
	captain.write(dist2, font=('Arial', 12, 'bold'))
	time.sleep(0.5)
	if dist1 <= 820 and dist2 <= 820:
		for i in range(4):
			captain.undo()

def display_stats(d1, d2):
	cap = create_turtle()
	cap.hideturtle()
	cap.penup()
	cap.goto(-275, 170)
	cap.write("----------------------------------------------------------------------------------------------------------------", font=('Arial', '12', 'bold'))
	cap.goto(0, 150)
	cap.write("STATS:", font=('Arial', 12, 'bold'))
	cap.goto(-150, 130)
	cap.write("Lonely Boi Absolute Total Distace: " + str(d1), font=('Arial', 10, 'italic'))
	cap.goto(-150, 115)
	cap.write("Lonely Bois Girlfriend Absolute Total Distace: " + str(d2), font=('Arial', 10, 'italic'))


def create_starting_line(cap, start_x, start_y):
	dist = 15.72
	total_rows = 38
	total_sqrs = 5
	cap.penup()
	cap.goto(start_x, start_y)
	cap.pendown()
	for row in range(total_rows): # this is in charge of the total number of rows
		for sqrs in range(total_sqrs):# this is in charge of drawing 5 square in each row
			if sqrs % 2 == 0 and row % 2 == 0: 
				cap.color("white")
			else: 
				cap.color("pink")
			cap.begin_fill()
			for i in range(4): # this is in charge of actually drawing each square
				cap.forward(dist)
				cap.left(90)
			cap.end_fill()
			cap.forward(dist)
		cap.penup()
		start_y -= dist
		cap.goto(start_x, start_y)

def run():
	total_distance = 820
	lonely_boi_distance = 0
	lonely_bois_girlfriend_distance = 0

	total_distance_lb = 0
	total_distance_lbg = 0
	

	speeds = [-50, 5, 25, 50, 60, 70]
	colors = ["cadetblue1", "lavender", "coral4", "dark gray"]
	while((lonely_boi_distance < 820) and (lonely_bois_girlfriend_distance < 820)):
		update_distances(captain, lonely_boi_distance, lonely_bois_girlfriend_distance)
		lb_speed = random.choice(speeds)
		lb_color = random.choice(colors)
		lonely_boi.color(lb_color)
		lonely_boi.forward(lb_speed)
		lonely_boi_distance += lb_speed
		total_distance_lb += abs(lb_speed)
		check_winner(lonely_boi_distance, 0)

		lbg_speed = random.choice(speeds)
		lbg_color = random.choice(colors)
		lonely_bois_girlfriend.color(lbg_color)
		lonely_bois_girlfriend.forward(lbg_speed)
		lonely_bois_girlfriend_distance += lbg_speed
		total_distance_lbg += abs(lbg_speed)
		check_winner(lonely_bois_girlfriend_distance, 1)
	
	return lonely_boi_distance, lonely_bois_girlfriend_distance, total_distance_lb, total_distance_lbg
	
turtle.bgcolor("black")
turtle.bgpic("./piggy.gif")
lonely_boi = create_turtle("turtle", "green")
lonely_bois_girlfriend = create_turtle("turtle", "red")
captain = create_turtle()
turtle.delay(0)
captain.hideturtle()
create_starting_line(captain, -478, 283)
create_starting_line(captain, 400, 283)

set_starting_positions(-420, 70)
display_distances(captain)
d1, d2, d3, d4= run()
update_distances(captain, d1, d2)
display_stats(d3, d4)


turtle.mainloop()