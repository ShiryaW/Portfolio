#This is a completely normal and legit Game of Thrones title generator.

from random import choice

houses = ["Targaryen", "Lannister", "Stark", "Bolton", "Karstark", "Tully",
    "Tarly", "Mormont", "Arryn", "Baratheon", "Frey", "Trump", "Farage",
    "May", "Abbott", "Pence"]
epithets = ["Nut", "Impoverished", "Tit", "Broken", "Absolute Unit",
    "Virgin", "Memelord", "Action Star", "Agoraphobe", "Hooligan", 
    "Incorporeal", "Fleeting", "Walking Dead", "Unsung Legend", "Unfortunate"]
step3 = ["Slayer", "Winner", "Conqueror", "Bane", "Seducer", "Lover",
    "Vendor", "Connoisseur", "Whisperer", "Solicitor", "Devourer", "Heir"]
nouns = ["Fragile Masculinity", "Rodents of Unusual Size", "Sass",
    "the Concept of Linear Time", "Ingrown Hairs", "PewDiePie",
    "Republicans", "the Avengers", "Brexit", "Milkshakes", "Vintage Memes",
    "Character Development", "Vore", "Reddit", "Carbohydrates", 
    "Climate Change"]
time = ["All Eternity", "a Heartbeat", "a Little Over an Hour", "a Nanosecond",
    "Millenia", "Way Longer Than Necessary", "Too Long for Comfort",
    "the Duration of a Single Episode", "10 Sad Seconds"]

def run():
	print("Welcome to a Totally Normal Game of Thrones Title Generator.")
	print("The mutilated children working in our title mines will fetch")
	print("the most appropriate title for you in just a moment.")
	name = input("But first, what is your name? (Type q to quit)\n")
	
	if name.lower() == "q":
		return

	while True:
		print("Your scientifically accurate title is:")
		print(f"{name} the {choice(epithets)} of House {choice(houses)}, " + \
			f"{choice(step3)} of {choice(nouns)} for {choice(time)}\n")
		ui = input("Would you like to receive another one? (y/n)\n")
		if not ui.lower() == "y":
			return

if __name__ == "__main__":
	run()
