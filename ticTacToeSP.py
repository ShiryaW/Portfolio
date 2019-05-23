from random import randint

#dictionary to store values of occupied tiles on the game board
tiles = {}

#helper functions
def validateInput(ui):
	"""Checks whether the input is in range 1-9 and the tile is not 
	already taken by another symbol.
	Returns True if input is valid, otherwise returns False and an
	error message."""
	try:
		if int(ui) < 1 or int(ui) > 9:
			return False, "You can only use numbers 1-9."
		elif tuplifyInput(int(ui)) in tiles.keys():
			return False, "Tile no. %s is already occupied." % ui
		else:
			return True, "Input OK"
	except ValueError:
		return False, "Could not parse input. Use only numerical characters."
		
def printBoard():
	"""Prints the game board using a dictionary that stores values
	of occupied tiles (either O or X shape). If there is no value for a given
	tile in the dictionary, an empty tile is printed."""
	print()
	for i in range(1,4):
		count = {}
		print("#" * 19)
		for j in range(1,4):
			if (i,j) in tiles.keys():
				count[(i,j)] = 1
		for k in range(1,4):
			for l in range(1,4):
				if count.get((i,l)) is not None:
					if count[(i,l)] == 1 or count[(i,l)] == 3:
						if tiles[(i,l)] == "X":
							print("# X X ", end="")
						else:
							print("#  O  ", end="")
					elif count[(i,l)] == 2:
						if tiles[(i,l)] == "X":
							print("#  X  ", end="")
						else:
							print("# O O ", end="")
					count[(i,l)] += 1
				else:
					print("#     ", end="")
				if l == 3:
					print("#")
	print("#" * 19)
	print()
		
#UNUSED FUNCTION
def printBoardBasic():
	"""Simple version of the printBoard() function which doesn't draw 
	shapes but only single X or O characters."""
	print()
	for i in range(1,4):
		print("#" * 13)
		print("#   " * 3, end="#\n")
		for j in range(1,4):
			if (i,j) in tiles.keys():
				print("# %s " % tiles[(i,j)], end="")
			else:
				print("#   ", end="")
		print("#")
		print("#   " * 3, end="#\n")
	print("#" * 13)
	print()
	
def tuplifyInput(ui):
	"""Converts user input into a tuple of (row, column)."""
	if ui < 4:
		return (1, ui)
	elif ui < 7:
		return (2, ui - 3)
	else:
		return (3, ui - 6)

def checkForWin():
	"""Checks whether or not the board has entered a win state."""
	gameOver = False
	msg = "The game continues."
	
	#tie check
	movesLeft = False
	for i in range(10):
		if validateInput(i)[0]:
			movesLeft = True
			break
	if not movesLeft:
		gameOver, msg = True, "It's a tie!"
	
	#win check
	for i in range(1,4):
		if tiles.get((i,1)) == tiles.get((i,2)) == tiles.get((i,3)) and tiles.get((i,1)) is not None:
			gameOver, winSymbol = True, tiles[(i,1)]
		elif tiles.get((1,i)) == tiles.get((2,i)) == tiles.get((3,i)) and tiles.get((1,i)) is not None:
			gameOver, winSymbol = True, tiles[(1,i)]
	if tiles.get((1,1)) == tiles.get((2,2)) == tiles.get((3,3)) and tiles.get((1,1)) is not None:
		gameOver, winSymbol = True, tiles[(i,1)]
	elif tiles.get((1,3)) == tiles.get((2,2)) == tiles.get((3,1)) and tiles.get((1,3)) is not None:
		gameOver, winSymbol = True, tiles[(i,1)]
		
	#check which player wins
	if gameOver:
		msg = "You win!" if winSymbol == "O" else "You lose!"
		
	return gameOver, msg

def reset():
	tiles.clear()
	printBoard()
	isPlayerOne = True

#main program loop
print("Welcome to  A Boring Game of Tic Tac Toe!")
print("The game is designed for two players.")
print("Type a number from 1 to 9 to select the square you want to mark,\n" + \
    "1 being the top left and 9 the bottom right corner.")
print("(Type q to quit.)")
isPlayerOne = True
printBoard()

while True:
	if isPlayerOne:
		#get user input
		turn = input("Type your move: ")
	
		if turn.lower() == "q":
			break
			
		success, message = validateInput(turn)
		if not success:
			print(message)
			continue
			
	else:
		#get AI input
		print("The computer is thinking...")
		turn = randint(1,9)
		while not validateInput(turn)[0]:
			turn = randint(1,9)
	
	#input OK, time to update and print the board
	formattedInput = tuplifyInput(int(turn))
	tiles[formattedInput] = "O" if isPlayerOne else "X"
	printBoard()
		
	#announce win or tie and ask if the player wants to go again	
	status, msg = checkForWin()
	if status:
		print(msg)
		print()
		newGame = input("Play again? (y/n) ")
		
		#reset everything to default and start a new game if yes
		if newGame.lower() == "y":
			reset()
			continue
		else:
			break
	
	#switch turns	
	isPlayerOne = not isPlayerOne
	
print("Thanks for playing!")
