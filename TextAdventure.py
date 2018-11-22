class Profile():
	def __init__(self, name, residence):
		self.name = name
		self.residence = residence
    
class Inventory():
	def __init__(self, weapons, money, arrows):
		self.weapons = weapons
		self.money = money
		self.arrows = arrows
		weapons = "sword", "bow and arrows"
		money = 0

		def __init__(self, w, m, a):
			self.weapons = w
			self.money = m
			self.arrows = a

		def AddMoney(x):
			money = money + x
			return money

		def Ammunition(x):
			arrows = arrows - x
			return arrows

class Health():
	def __init__(self, hp):
		self.hp = hp

	def getHP(x):
		return x

    #calculates the damage the player receives
	def Damage(hp, x):
		return hp - x

	#calculates the amount of health (hp) restoration
	def Heal(hp, x):
		return hp + x
		

ammo = 20
health = 100

name = str(input("Welcome to the text adventure! Please start by entering your name."))
residence = str(input("Okay," + name + ", where do you live in Fjordland?"))
travel = str(input("Okay," + name + ", you leave " + residence + ", and walk to Castle City. " + 
	"Someone asks you for directions. What will you do?\n Help them out\n Kill them\n"))
if travel == "Help them out":
	print("Nice job! You gain 500 coins for your trouble.")
	balance = 500
	print("You decide to travel to the forest to take a shortcut to Orange Town to sell produce that you want to sell. On your way there, you spot a mysterious looking hideout. Curious, you venture a little too close and...")
	response = str(input("You wake up in a dark room. You are not sure where you are, and you hear strange voices. Suddenly, a person takes off your blindfold, and you are asked, 'How did you find this place?!' \nSay nothing \nI stumbled upon it and was curious."))
	if response == "Say nothing":
		print("The interrogator punches you in the face, causing you to lose 5 health. He yells, 'Answer me when I'm talking to you, scum!'")
	elif reponse == "I stumbled upon it and was curious":
		print("The man says, 'Mind your own business next time! Now leave before I kill you!' You exit quickly and arrive at Orange Town, where you see your friend. Your friend, concerned that you looked troubled asks, 'Are you okay? What's wrong?'")
		answer = str(input("You don't respond and she asks you again, '" + name + "', I'm really concerned about you. Will you please tell me? what's wrong?' \nTell her \nSay nothing"))
		if answer == "Tell her":
			report = print("You tell her what happened to you, and she frowns. 'Since I work for the kindgom, I can have them arrested for treating you like this. Do you want me to report this incident to the king's advisor?' \nyes \nno")
		elif answer == "Say nothing":
			print("'Okay,' she says, 'I won't press you on the matter. Tell me, how are you doing?' \ngood \nbad")

elif("Kill them"):
	decision = str(input("Oh no! 2 of the king's soldiers are after you! You only have a sword and a bow and arrows. What would you like to do? \nFight them\n Surrender"))
	if decision == "Fight them":
		weapon = str(input("Would you like to use a sword or your arrows? You have " + str(ammo) + " arrows. \nsword \narrows"))
		if weapon == "sword":
			print("The soldiers have been defeated!")
		elif weapon == "arrows":
			ammo = ammo - 2
			print("You have used 2 arrows. You have " + str(ammo) + " arrows remaining.")
			
friend = str(input("A man named Joe approaches you. He says, 'Hello, I saw you kill those soldiers back there. We share the same views on the kingdom. We are looking to overthrow the king and establish a republic. Would you like to help us?' \nyes \nno"))
if friend == "yes":
	print("'Thanks so much! I'll to you to our hideout in the forest.")
elif friend == "no":
	print("'That's too bad. I'll leave now. Be well!'")
