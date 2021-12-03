#Code made by Cody Dysart for CSE 20
#Assignment 10.1: Your Own Class (Basic Endless monster fighter game)
#Description:
#           The code before you is an endless monster game that holds all of the data within the randomFighter class()
# Which will first initize some important values, and uses text files to make dictionaries of dictionaries
# to hold the monsters and there stats, in where you can change the amount of enemies and there stats to any amount
# of enemies yo what there to be. (The txt file has to be in the same folder and be named Creatures.txt)
# All of the combat is held in the def Combat function where the majority of the fighting code occurs
# But every stat of monster is stemed from createDict which is then stored in creatures, and the players
# Code is hard coded in set_player_stats, which you can pull up with get_player_stats.

#importing the random function
import random

class randomFighter():
    #Constructor is right here
    def __init__ (self):
        #making sure the creature txt file will be stored no matter what
        self.orginalfile = open("Creatures.txt", 'r')
        #reads and closes it so there won't be any funny business happening
        self.cLoaded = self.orginalfile.read()
        self.orginalfile.close()
        #storing some self.varibales for later functions
        self.actualstring = str()
        self.lencLoaded = len(self.cLoaded)
        self.MainDict = dict()
        #these are specifically for the player
        self.extraHP =  random.randint(0, 20)
        self.extraAttack =  random.randint(0, 20)
        self.extraDefense =  random.randint(0, 20)
        self.enchantments = random.randint(0, 20)
    #creates a dictionary of dictionaries to store enemies    
    def createDict(self, lencLoaded, cLoaded):    
        wordCount = 0
        divided = list()
        listSize = 0
        User = str()
        #these hold intermediate values that will be stored somewhere else later
        Intermed2 = ''
        Intermed3 = ''
        Intermed4 = ''
        Intermed5 = ''
        Tester = True
        adder = 0
        #holds the main dictionary
        MainDict = dict()
        #print(Loaded.read())
        #getting the size of the list here 
        for i in range(0, lencLoaded):
            #adding another person each \n
            if cLoaded[i] == "\n":
                listSize = listSize + 1
            #
        for i in cLoaded:
            #if it was a space then word counter goes up 1
            if i ==' ':
                #going up 1 
                wordCount = wordCount + 1
        #Getting the word count and now splitting up the sentence into a list called divide with split \n
        for i in range(0, wordCount):
            divided = cLoaded.split("\n")
            #doing this x many times its been split
        for i in range(0, listSize):
            #creating an intermediate to hold a value of the word changing with every loop will be turning into there names
            intermed = str(divided[i])
            #Tester is here to get out of the loop easier
            while Tester == True:
                #User is being transfered from intermed from adder which starts at zero the first loop and adds up until it reaches a ,
                User = intermed[adder]
                #the comma stops this loop since we now have out name in intermed2
                if User == ',':
                    #will get us out of this loop
                    Tester = False
                else:
                    #storing the full name for later here
                    Intermed2 = Intermed2 + User
                    Tester = True
                    adder = adder + 1
            #reseting for the next variables we're adding in the next while loop below
            Tester = True
            self.MainDict[Intermed2] = {} 
            adder = adder + 1
            #Tester is here to get out of the loop easier
            while Tester == True:
                #getting the intermed again its now going to get email
                User = intermed[adder]
                #stops again at a comma 
                if User == ',':
                    Tester = False
                else:
                    #stores the HP in intermed3
                    Intermed3 = Intermed3 + User
                    Tester = True
                    #adding up here
                    adder = adder + 1
            #resetting for the next while loop
            Tester = True
            adder = adder + 1
            #here to make life easier in the loop
            while Tester == True:
                #using the intermediate again to keep counting up
                User = intermed[adder]
                #stops again at the comma
                if User == ',':
                    Tester = False
                else:
                    #holding the number here
                    Intermed4 = Intermed4 + User
                    Tester = True
                    adder = adder + 1
            #reseting variables
            Tester = True
            adder = adder + 1
            #makes life easier 
            while Tester == True:
                #try here so we don't go create an error while counting up we will only count until a error appears
                try:
                    #counting up
                    User = intermed[adder]
                    #holds the Defense here
                    Intermed5 = Intermed5 + User
                    Tester = True
                    adder = adder + 1
                except:
                    #once it can't count up anymore it stops
                    Tester = False
            #stores all the varibles in in the dictionary in the dictionary
            MainDict[Intermed2] = {"Health": Intermed3.strip(), "Attack": Intermed4.strip(), "Defense": Intermed5.strip()} 
            #resetting for the next full loop so we can get the next character
            adder = 0
            Intermed2 = ""
            Intermed3 = ""
            Intermed4 = ''
            Intermed5 = ''
            Tester = True
            User = ''
            #print(maindict)

            #User = intermed[i]
            #print(User)
            #print(intermed)
            pass
        #print(divided[0])
        #returnning the varible so it counts
        #print(self.MainDict)
        return MainDict     
    #this handles the main combat of the game 
    def Combat(self):
        #creating the values of the monster that will be used in the combat later in the fighting system
        #storing the monsters name
        Currentmonster = self.monstername
        #storing the health attack and defense of the monster
        self.currentHealth = int(str(list(self.creature.values())[self.whichMonster]["Health"]))
        self.currentAttack = int(str(list(self.creature.values())[self.whichMonster]["Attack"]))
        self.currentDefense = int(str(list(self.creature.values())[self.whichMonster]["Defense"]))
        #where we keep looping the combat system for attacking or running
        while True:
            #telling the player the current monster and its hp
            print("\nA " + Currentmonster + " is before you!")
            print("Monster HP:" + str(self.currentHealth))
            #giving the player the only two commands they have
            print("Do you attack, or run?")
            #geting the players input
            player = input("Please choose an option:")
            #turning there anwswer into lower so its now not case sentistive
            player = player.lower()
            #if the player attacks we continue
            if player == "attack":
                #doing a damage calculation
                damageDone = ( self.playerAttack-(self.currentDefense/2))
                #if the damage would be less than zero we let the player do 5 damage
                if damageDone < 0:
                    damageDone = 5
                #telling the amount of damage the player does to te current monster
                print("You attack the " + Currentmonster + " dealing " + str(damageDone))
                #The monster health will now change
                self.currentHealth = self.currentHealth - damageDone
                #the monster will now attack the player
                print("The " + Currentmonster + " has " + str(self.currentHealth) + " HP left\n")
                #doing the damage calculation
                damageDoneToPlayer = self.currentAttack - self.playerDefense
                #making sure the monster always does at least 1 damage
                if damageDoneToPlayer < 0:
                    damageDoneToPlayer = 1
                #checks if the player is dead
                if self.currentHealth > 0:
                    #tells the player the monster's damage
                    print("The " + Currentmonster + " attacks back dealing " + str(damageDoneToPlayer) +" damage!!!")
                    #taking away the players HP
                    self.playerHP = self.playerHP - damageDoneToPlayer
                    #tells the player how much hp is left
                    print("You have " + str(self.playerHP) + " left!!!\n")
                    #If the players hp is lower than 1 they died
                    if self.playerHP < 1:
                        #tells the player they died and exits the game
                        print("You have died! \nThis is the end of your story now, but is this the best you could have done?")
                        exit()
                #if they killed the monster before they died
                else:
                    #tells the monster they defeated and gives the player a level
                    print("You have defeated the " + Currentmonster + ". You have gained a level!!!")
                    #randomizes the monster for the next combat
                    randomFighter.set_randomize_opposing_Monster(self)
                    #adds extra hp attack and defense to the players stats for a level up
                    self.extraHP = self.extraHP + random.randint(0, 20)
                    self.extraAttack = self.extraAttack +  random.randint(0, 20)
                    self.extraDefense = self.extraDefense + random.randint(0, 20)
                    #tells the player how their stats grew
                    print("You gained an extra " +  str(self.extraHP) + " HP, " + str(self.extraAttack) + " extra attack, and " + str(self.extraDefense) + " extra defense!")
                    #setting the players stats
                    randomFighter.set_player_stats(self, self.extraHP, self.extraAttack, self.extraDefense)
                    break
            #if the player decides to run intstead of fight we will break out of the loop and go back to the main menu
            elif player == "run":
                #telling the palyer they ran
                print("You have ran away! \n")
                #options menu being shown
                print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
                #breaking out of the loop
                break
            else:
                pass
    #to see the players stats
    def get_player_stats(self):
        #getting info from set_player_stats and sets hp attack and defense for other parts of the code to see
        hp = self.playerHP
        attack = self.playerAttack
        defense = self.playerDefense
        #returns hp attack and defense
        return(hp, attack, defense)
    def set_player_stats(self, extraHp, extraAttack, extraDefense):
        #sets the players hp attack and defense with a base number, its extra(level up), and single enchant, and getplayerstats will read it later
        self.playerHP = 30 + extraHp + randomFighter.get_enchants(self)
        self.playerAttack = 8 + extraAttack + randomFighter.get_enchants(self)
        self.playerDefense = 5 + extraDefense + randomFighter.get_enchants(self)
    #checks the players enchantments to be set somewhere else
    def get_enchants(self):
        enchantment = self.enchantments
        #returning the enchantments
        return(enchantment)
    #enchats all the players stats with a number
    def set_enchants(self):
        #setting the enchanments to be random between 0 and 20
        self.enchantments = random.randint(0, 20)
    #opens the creature txt file and loads a dictionary
    def creatures(self):
        #opening the creature text file
        self.orginalfile = open("Creatures.txt", 'r')
        #reads and closes the file
        self.cLoaded = self.orginalfile.read()
        self.orginalfile.close()
        #making a string for later
        self.actualstring = str()
        #loads the file as a int
        self.lencLoaded = len(self.cLoaded)
        #getting the class
        startup = randomFighter()
        #creating a blank dict for to hold the monsters
        self.creature = dict()
        #creating the dictionary here
        self.creature = startup.createDict(self.lencLoaded, self.cLoaded)
        #returns the dictionary
        return(self.creature)
    #will randomize the monsters fighting
    def set_randomize_opposing_Monster(self):
        #picks arandom number between 0 and how many monsters there are 
        #setting the monsters number
        self.whichMonster = random.randint(0, (len(self.creature)-1))
        #setting the monsters name
        self.monstername = str(list(self.creature.keys())[self.whichMonster])
    #getting the monsters names hp attack and defense
    def get_randomize_opposing_Monster(self):
        #getting the monsters name and number from dict
        whichMonster = self.whichMonster 
        monstername = self.monstername
        #getting the health attack and defense of the monster to hold and give out at a later time
        Hp = str(list(self.creature.values())[whichMonster]["Health"])
        attack = str(list(self.creature.values())[whichMonster]["Attack"])
        defense = str(list(self.creature.values())[whichMonster]["Defense"])
        #retuns the values here
        return(monstername, Hp, attack, defense)
def main():

    #holds the class
    startup = randomFighter()
    #sets the players level
    startup.set_player_stats(1,1,1)
    #makes the starting dict
    currentStats = startup.creatures()
    #randomizes the monster that will fight the player
    startup.set_randomize_opposing_Monster()
    #print(startup.set_randomize_opposing_Monster())
    #introduces the player the the game and commands
    print("Welcome challenger to a game of wit and luck")
    print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
    while True:
        #now asking the player for input on what they want to do
        player = input("Please choose an option:")
        #turning there anwswer into lower so its now not case sentistive
        player = player.lower()
        print(player)
        #if elif, else statement machine on if what option they choose for when they start facing monsters
        #plays the next combat against a random monster
        if player == "next_fight":
            startup.Combat()
        #checks the player stats
        elif player == "stats":
            #gets the player stats
            stats = startup.get_player_stats()
            #tells the player there stats so they can see what they have to work with
            print("You have HP:" + str(stats[0]) + " Attack:" + str(stats[1]) + " Defense:" + str(stats[2]) + "\n")
            #tells the player the options again
            print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
        #will tell the player what the opposing monster is at the moment
        elif player == "opposing_monster":
            #gets the opposing monsters name and stats
            monsterstats = startup.get_randomize_opposing_Monster()
            #tells the monster name and stats and brins you back to the start menu
            print("\n" +str(monsterstats[0]))
            print("HP:" + str(monsterstats[1]) + " Attack:" + str(monsterstats[2]) + " Defense:" + str(monsterstats[3]) + "\n")
            print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
        #will enchant the player stats
        elif player == "enchant":
            #setting the player stats to add a level to them
            startup.set_enchants()
            #giving feedback that they have gotten an enchantment
            print("You feel a mysterious enchatment come upon you! \n")
            #returning back to the base menu
            print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
        #will get a different monster
        elif player == "fight_different_monster":   
            #randomizes the opposing monster
            startup.set_randomize_opposing_Monster()
            print("A random monster has appeared! \n")
            #going back to the base menu
            print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
        #giving out the options they have in the game
        elif player == "help":
            print("Commands: Next_Fight, Stats, Opposing_Monster, Enchant , Fight_Different_Monster, Help ")
        #tells the player they need to pick a different option
        else:
            print("Sorry that isn't an option")
if __name__ == "__main__":
    main()