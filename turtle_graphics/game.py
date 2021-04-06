import turtle
import random


turtle.bgcolor("gold")
hunter = turtle.Turtle()
hunters_other_friend = turtle.Turtle()

hunter.speed(0)  #0-10  
hunters_other_friend.speed(0)

hunter.pensize(4)
hunters_other_friend.pensize(6)

hunter.shape("turtle")
hunters_other_friend.shape("turtle")


dist = 6
angle = 82
colors = ["purple", "coral", "brown", "pink", "AliceBlue", "violet", "spring green", "maroon"]
rot = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


message = "My Playground"
hunter.penup()
hunter.goto(-200, -350)
hunter.color("beige")
hunter.write(message, font=("Arial", 48, "italic"))
hunter.hideturtle()	


#Recap: 

'''
How to Move? 
goto(x, y), forward(#), backward(#), left(angle), right(angle)

How to change colors? 
turtlesname.color(insert_color_here)

#How to pick up/down pen
penup()
pendown()

#How to increase size of turtle 
pensize(1-10)

#How to speed up/slow turtle down
turtlesname.speed(0-10) 

#How to hide turtle 
hunter.hideturtle()

#How to write a message
.write(message, font=(fontname, fontsize, fontstyle))

#how to change turtle shape
.shape("turte")

'''



turtle.mainloop()