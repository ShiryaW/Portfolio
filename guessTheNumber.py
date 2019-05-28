from random import randint

def validateInput(ui):
	try:
		if not int(ui) > 0 or not int(ui) < 101:
			return False, "The number has to be between 1 and 100 (inclusive)."
		else:
			return True, "Input OK"
	except ValueError:
		return False, "Please input only numerical characters."
	

guessCap = 5

print("I'm thinking of a number between 1-100. Guess the number and see")
print(f"if you are right. If you don't get it right within {guessCap} guesses,")
print("you lose!")

answer = randint(1,100)
numGuesses = 0
guess = ""

while guess != answer:
	guess = input("\nWhat's your guess?\n")
	isValid, msg = validateInput(guess)
	
	if not isValid:
		print(msg)
		continue
	
	if int(guess) == answer:
		print("You got me! That's the number!")
		break
		
	elif numGuesses >= guessCap:
		print(f"Sorry, that was {numGuesses} guesses!")
		print(f"The number was actually {answer}. Better luck next time!")
		break
		
	elif int(guess) > answer:
		print("The number is lower than that.")
	
	elif int(guess) < answer:
		print("The number is higher than that.")
		
	numGuesses += 1
