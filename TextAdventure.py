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
		weapons = w
		money = m
		arrows = a
    
   def AddMoney(x):
		return money += x
    
   def Ammunition(x):
		return x -= 1

ammo = Ammunition(20)

name = str(input("Welcome to the text adventure! Please start by entering your name."))
residence = str(input("Okay," + name + ", where do you live in Fjordland?"))
travel = str(input("Okay," + name + ", you leave " + residence + ", and walk to Castle City. " + 
	"Someone asks you for directions. What will you do?\n Help them out\n Kill them\n"))

switch(travel):
	case("Help them out"):
		print("Nice job, you gain 500 coins for your trouble.")
		balance = 500
	case("Kill them"):
		str(input("Oh no! 2 of the king's soldiers are after you! You only have a sword and a bow and arrows. What would you like to do? \nFight them\n Surrender"))
		case("Fight them"):
		str(input("Would you like to use a sword or your arrows? You have " + ammo + " arrows. \nsword \narrows"))
		case("sword"):
		print("The soldiers have been defeated!")
