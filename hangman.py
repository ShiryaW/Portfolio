#This is a game of hangman. That's pretty much it.

from random import choice

classes = ["warrior", "priest", "archer", "acolyte", "wizard", "alchemist",
    "paladin", "rogue", "thief", "assassin", "hunter", "sharpshooter",
    "monk", "berserker", "knight", "merchant", "mage"]
    
animals = ["giraffe", "hippopotamus", "zebra", "horse", "tortoise",
    "armadillo", "echidna", "pangolin", "butterfly", "moose", "reindeer",
    "leopard", "tiger", "crane", "pigeon", "rhinoceros", "bumblebee",
    "octopus"]
    
bands = ["metallica", "nirvana", "queen", "aerosmith", "radiohead",
    "evanescence", "halestorm", "delain", "scorpions", "slipknot"]
    
gameModes = {"classes": classes, "animals": animals, "bands": bands}

def drawWord(w, guessed):
	"""Prints a _ for every character in the current word that has not
	been guessed, otherwise prints the given character. The characters
	are separated by spaces for better legibility."""
	string = ""
	for char in w:
		if char in guessed:
			string += char
		else:
			string += "_"
	print(" ".join(string))
	print()
	
def drawSkelly(s):
	"""Prints the hangman at a stage determined by s."""
	steps = ["  |\n", "  O\n", " /", "|", "\\\n", " /", " \\\n"]
	skelly = "".join([step for step in steps[:s]])
	print(skelly)
	print("\n" * (4 - len(skelly.split("\n"))))
	
def checkWin(w, guessed):
	"""Checks whether the game has been won by verifying that all chars
	of the word have been guessed. If one or more have not been guessed,
	returns False."""
	isWin = True
	for char in w:
		if char not in guessed:
			isWin = False
	return isWin

def run():
	print("Welcome to a thrilling game of Hangman. A word is being randomly")
	print("selected for your gaming pleasure. Guess the word by guessing")
	print("characters one at a time. (Type q to quit or / to list guesses.)")
	print()
	print("But first, what types of words would you like us to choose from?")
	print("(Type 'classes' for fantasy MMO classes, 'bands' for famous bands")
	print("and 'animals' for... animals.)")
	gameType = input()
	print()

	if gameType in gameModes.keys():
		current = choice(gameModes[gameType])
	else:
		print("I have no idea what you said, sorry. Aborting mission now.")
		return
	
	#initialize variables for 1 round
	guessed = []    #the letters that have been guessed
	steps = 0       #what step the hangman is at (0 = "full health")
	drawSkelly(steps)

    #main game loop
	while True:
		drawWord(current, guessed)
		
		if checkWin(current, guessed):
			print("You win!")
			ui = input("Would you like to play again? (y/n)\n")
			if ui.lower() == "y":
				current = choice(gameModes[gameType])
				guessed = []
				steps = 0
				continue
			else:
				break
				
		guess = input("What is your next guess?\n")
		print()
		
		#validate input
		if guess.lower() == "q":
			break
		elif guess.lower() == "/":
			print(sorted(guessed))
			continue
		elif len(guess) != 1:
			print("You can only guess one letter at a time.")
			continue
		elif guess.lower() in guessed:
			print("You have already guessed that letter.")
			continue
		
		#input OK, process and draw the hangman	
		if guess not in current:
			steps += 1
		
		guessed.append(guess)
		drawSkelly(steps)
		
		#lose game if steps >= 7
		if steps >= 7:
			print("You lose! Better luck next time!")
			break

run()
