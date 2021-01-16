import turtle
import random

#create your own turtle
hunter = turtle.Turtle()
hunter.shape("turtle")

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

x = turtle.Screen()
x.bgcolor("green")
x.title("Turtle Graphics Race")

#moving directions

hunter.speed(0)
colors = ["red", "gold", "blue", "maroon", "black", "cyan"]
hunter.speed(20)
t.penup()
t.setposition(-100, -250)
t.pendown()
for i in range(110):
	hunter.forward(65)
	hunter.left(43)
	hunter.color(random.choice(colors))
	hunter.left(i)
	t.forward(62)
	t.left(71)
	t.color(random.choice(colors))
	t.left(i + random.randint(10,20))


	


x, y = hunter.pos() 
print("x ", x)
print("y ", y)

turtle.mainloop()
