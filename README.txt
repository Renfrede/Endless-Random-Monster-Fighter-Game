This code was created by Cody Dysart. (Anyone can use it as they see fit)

Git hub: https://github.com/Renfrede/Endless-Random-Monster-Fighter-Game/tree/main

Desciption of Class:

Class randomFighter - Contains the a constructor, a dictionary of dictionary creator(extracts it from the creature.txt file), and other various functions within it to go and create
		   a text based combat system. That will go and allow the player to face any monsters held in the creature.txt file, enchant, level up, change current enemy with a random one,
		   to go and create a combat system that will constantly have the player level up to face the next random monster. In which they can only escape or flee from battle.

Description of Functions/Methods:

def __init__ (self): - Holds self. variables that will be reference throughout other functions, and holds the orginalfile used to open creatures.txt/closes creatures.txt.
		    Which allows code to be reference far in advance so no random errors appear.

def createDict(self, lencLoaded, cLoaded): - Creates a dictionary of dictionaries, that hold all the enemies in the creatures.txt file. Each enemy has its own dictionary where its name,
					    Hp, attack, and defense is stored. And requires to have the read file (cLoaded), and length of the dictionary(lencLoaded), as inputs along with
					    self from the class to get the initized variables.

def Combat(self): - Holds the main combat portion of the code creating the loop in which the player and monster fight one another until either the player kill/dies the monster, or flees.
		   Holds the main combat in a while loop, and constantly references other functions with self., and calling them directly to get players, and monsters stats. 

def get_player_stats(self): - Allow you to get the players stats after they been set. Holding the hp attack and defense of the player and won't affect the set values.

def set_player_stats(self, extraHp, extraAttack, extraDefense): - Allows you to set the players stats requring you to add extra hp, attack, and defense. Which has to be set at either
								0, or 1 before you call it. As well as it gets the enchants the player gets from def get_enchant as a bonus to it's stats

def get_enchants(self): - Gets the players enchants holding them for set_player_stats to retrieve to create the stats of the player. And can be called upon to see the current
			enchantment

def set_enchants(self): - Sets the player enchantment as a random int between 0 and 20 to all stats. The get enchants will use it to add on all the stats

def creatures(self): - Creates the dictionary of dictionary of the monsters and stores, and returns the value. Making sure as well to open the txt, and close it as well.

def set_randomize_opposing_Monster(self): - Randomizes the the opposing monster betwen 0 and the amount of monsters there are. setting the number, and name of the monster

def get_randomize_opposing_Monster(self): - Stores the randomized number to be used in combat function. As well as getting the health attack, and defense of the monster. Returning it
					to whatever called the function.

def main(): - Holds the test code in which it creates the basic game layout, giving the player commands, and allow the player to go into combat, reset monster, get player and monster stats
	As well as giving a help menu, enchantments, and exit to the game

Important Variables:
self.extraHP =  random.randint(0, 20)
self.extraAttack =  random.randint(0, 20)
self.extraDefense =  random.randint(0, 20)
self.enchantments = random.randint(0, 20) - These all all holding the player character's stats in the constructor so no errors occur later when they're called upon. And can be called anywhere.

self.orginalfile - Holds the creatures.txt file name in which it will be read from

MainDict = Will hold the main dictionary in the createdict function and is also what gets returned from it.

currentmonster - holds the monsters name which will be used in combat function to get the health attack adn defense by using the value of it by using the name as a key.


damageDoneToPlayer - what damage hits the player
damageDone - what damage is done to the monster
enchantment = is the current enchant that is being held from the set_enchantments
whichMonster = holds the monster number
monstername = Holds the monsters name

Demo Program Documentation:
	
Desciption of the demo program:

	The demo program holds a simple game, that allows a player to keep leveling up each monster that is deafeated. As well as doing a random enchant before each battle, checking out the
	current monster that they will face, checking there own stats, the monster stats, etc. This all leads to a game in which the player has to decide if they want to face the monster in
	front of them or risk there luck on a different random monster. As well as allowing, the monster to be changed with creatures.txt being changed with a monsters name first, followed 
	by its hp, attack, and defense. Which all have to be on different lines, and seperated by comma's with after defense not having a comma. Which can be expanded to however large, the 
	player want it by editing the txt file.

How to run the demo program:
	To run the demo program first you want to add your monster to the creatures.txt file that you have to keep in the same folder as your randomFighter.py file. To add a new monster you 
	write:
		Monster, HP, Attack, Defense         (Then new line, and save once you added all the monsters you wanted)

	Then you just run it in visual studio code, command shell, or any other coding software. And it will then prompt you with commands for the game. The game is not case sensitive 
	so write down any command you want to start the game. 
