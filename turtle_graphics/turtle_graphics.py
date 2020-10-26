import turtle
import random

#create your own turtle
hunter = turtle.Turtle()
hunter.shape("turtle")


#moving directions

hunter.speed(0)
colors = ["red", "gold", "blue", "maroon", "black", "cyan"]
hunter.speed(20)
for i in range(20):
	hunter.forward(65)
	hunter.left(43)
	hunter.color(random.choice(colors))
	hunter.left(i)

x, y = hunter.pos() 
print("x ", x)
print("y ", y)

turtle.mainloop()
