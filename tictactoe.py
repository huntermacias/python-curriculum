import turtle

hunter = turtle.Turtle()
hunter.color("gray")
hunter.speed(0)
hunter.shape("turtle")

screen = turtle.Screen()
screen.colormode(255)
screen.setup(800,800)
screen.title("Tic Tac Toe")
screen.bgcolor(252, 200, 56)


def drawboard(hunter):
	hunter.hideturtle()
	hunter.penup()
	hunter.setposition(-300, -65)
	hunter.pendown()
	hunter.setposition(300, -65)
	hunter.penup()
	hunter.setposition(-300, 65)
	hunter.pendown()
	hunter.setposition(300, 65)
	hunter.penup()
	hunter.setposition(-150, 190)
	hunter.pendown()
	hunter.setposition(-150, -190)
	hunter.penup()
	hunter.setposition(150, 190)
	hunter.pendown()
	hunter.setposition(150, -190)


def draw_numbers(hunter):
	hunter.color("Blue")
	x = [-290, -130, 160]
	y = [190, 45, -95]
	z = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	for i in range(9):
		hunter.penup()
		hunter.setposition(x[i % 3], y[i//3])
		hunter.write(z[i], font=("Verdana", 15, "bold"))


def user_choice(Boxes, board, player):
	choice = int(input("Which box do you pick? [1-9] "))
	p1 = Boxes[choice - 1][0]
	p2 = Boxes[choice - 1][1]
	p3 = Boxes[choice - 1][2]
	p4 = Boxes[choice - 1][3]

	return(p1, p2, p3, p4, choice)


def drawO(p1, p2, p3, p4):
	hunter.hideturtle()
	hunter.color("red")
	hunter.penup()
	hunter.setposition(p3 - 30, p4 - 80)
	hunter.pendown()
	hunter.circle(45)


def drawX(p1, p2, p3, p4):
	hunter.hideturtle()
	hunter.color("green")
	hunter.penup()
	hunter.setposition(p1, p2)
	hunter.pendown()
	hunter.setposition(p3, p4)
	hunter.penup()
	hunter.setposition(p1, p4)
	hunter.pendown()
	hunter.setposition(p3, p2)
	

def validMove(board, row, col):
	pass #TODO

def updateBoard(board, player, choice):
	if choice == 1 :
		board[0][0] = player
	elif choice == 2:
		board[0][1] = player
	elif choice == 3:
		board[0][2] = player
	elif choice == 4:
		board[1][0] = player
	elif choice == 5:
		board[1][1] = player
	elif choice == 6:
		board[1][2] = player
	elif choice == 7:
		board[2][0] = player
	elif choice == 8:
		board[2][1] = player
	elif choice == 9:
		board[2][2] = player
	else:
		print("invalid choice")
	return board


def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j])
        print()


def checkWin(board, player):
	winningMoves = [
					[(0,0),(0,1),(0,2)],
					[(1,0), (1,1),(1,2)],
					[(2,0),(2,1),(2,2)],
					[(0,0),(1,0),(2,0)],
					[(0,1,),(1,1),(2,1)],
					[(2,0),(2,1),(2,2)],
					[(0,0),(1,1),(2,2)],
					[(0,2),(1,1),(2,0)]]
	
	
	count = 0
	for y in winningMoves: 
		for x in range(3): 
			row = y[x][0]
			col = y[x][1]
			if board[row][col] == player: 
				count += 1
			if count == 3: 
				return True
		count = 0

	return False




def main():
	Boxes = [
		[-270, 90, -200, 180],
		[-55, 90, 55, 180],
		[195, 90, 255, 155],
		[-270, -45, -200, 25],
		[-45, -30, 45, 30],
		[195, -30, 255, 30],
		[-270, -175, -200, -90],
		[-55, -175, 55, -90],
		[195, -175, 255, -90]
	]
	board = [
		[-1, -1, -1],
		[-1, -1, -1],
		[-1, -1, -1]]

	drawboard(hunter)
	draw_numbers(hunter)

	gameOver = True

	while(gameOver):
		player = 0
		p1, p2, p3, p4, choice = user_choice(Boxes, board, player)
		board = updateBoard(board, player, choice)
		drawX(p1, p2, p3, p4)
		if checkWin(board, player): 
			print(f'player {player} you win!')
			gameOver = False
			return
		
		player = 1
		p1, p2, p3, p4, choice = user_choice(Boxes, board, player)
		board = updateBoard(board, player, choice)
		drawO(p1, p2, p3, p4)
		if checkWin(board, player):
			print(f'player {player} you win!')
			gameOver = False
			
           
main()
