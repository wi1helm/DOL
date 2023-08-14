#imports
# https://docs.google.com/document/d/1H4C8bSwiFcRXzUPvR3zuR4nN2JzMAC5nT_N1NVTRUWw/edit?usp=sharing
#https://replit.com/talk/learn/ANSI-Escape-Codes-in-sprite1Ython/22803
import sys
import subprocess
import time
import linecache
import os
import keyboard
import random
import copy

os.system("") #A command that makes the https://replit.com/talk/learn/ANSI-Escape-Codes-in-sprite1Ython/22803 work in a normal sprite1Ython terminal 
#A list to hold all weaponds/items: Id : "Weapond Name" "type" "dmg"
itemID = {
  0: ["Empty", "none", "2"],
  1: ["Healing potion", "healing", "0"],
  2: ["Magic Scroll", "magic", "3"],
  3: ["Old Map", "item", "0"],
  4: ["Old Shoe", "item", "0"],
  5: ["Gitarr", "item", "3"],
  6: ["Razor Teeth","knife","4"],
  7: ["Glowing Rock","item","1"],
  8: ["Thunder","sword","5"],
  9: ["Magical Amulet","magic","4"],
}
# A list to hold all monsters: Id : "Monster name" "monster hp" "monster dmg"
monsterID = {
  0: ["", "", ""],
  1: ["Glubb Slime", "10", "2"],
  2: ["Mutated Fish", "10", "3"],
  3: ["Troll Gang", "15", "3"],
}

# Functions =============================================================================================================

#Function that checks if the input is a number.
def isANum(inp):
  try:
    inp = int(inp)
    return True
  except ValueError:
    return False

#Function that adds spaces between words in the gui so its always even.
def addSpaces(totalLength, word):
  spaces = " "
  #Takes the input word and the total lenght of the screen and adds the amount of spaces needed to fill the screen.
  for i in range(totalLength - len(str(word))): 
    spaces += " "
  return spaces


# ==== Start Screen ====
def printLogo():
  print(
    " ____  _____ __  __    _    _   _ ____ ___ _   _  ____      ___   ____ ____    _    ____ ___ ___  _   _    _    _         _     ___ ____ _   _ _____ "
  )
  print(
    "|  _ \| ____|  \/  |  / \  | \ | |  _ \_ _| \ | |/ ___|    / _ \ / ___/ ___|  / \  / ___|_ _/ _ \| \ | |  / \  | |       | |   |_ _/ ___| | | |_   _|"
  )
  print(
    "| | | |  _| | |\/| | / _ \ |  \| | | | | ||  \| | |  _    | | | | |  | |     / _ \ \___ \| | | | |  \| | / _ \ | |       | |    | | |  _| |_| | | |"
  )
  print(
    "| |_| | |___| |  | |/ ___ \| |\  | |_| | || |\  | |_| |   | |_| | |__| |___ / ___ \ ___) | | |_| | |\  |/ ___ \| |___    | |___ | | |_| |  _  | | |"
  )
  print(
    "|____/|_____|_|  |_/_/   \_\_| \_|____/___|_| \_|\____|    \___/ \____\____/_/   \_\____/___\___/|_| \_/_/   \_\_____|   |_____|___\____|_| |_| |_| "
  )

#Creates the start menu
def startMenu():
  menuActive = True
  printLogo()
  print("Write Anything To Start")

  #print("\n||  Welcome to Demanding Occasional Light  ||")
  startWord = input()
  #Checks if the input is anything
  while menuActive == True:
    if startWord == "Anything" or startWord == "anything":
      menuActive = False
      print("\033c")
    else:
      print('I Said write "Anything":')
      startWord = "anything"  #input()


# ================================ Character creation ================================================================================================================
# A function to create the traits for the player
def characterCreation():
  #renders the background screen
  renderGameScreen()
  #For each trait it asks for an input and checks if the input is valid.
  for x in (chrTraits):
    print("\033[8;H")
    print("| || Character creation ||")
    trait = chrTraits[x]
    errorMessage1 = "Error! Input can not be longer than 8 characters."
    errorMessage2 = "Error! Input is not a valid"
    if x not in ("Name", "Primary hand"): # Checks if the trait is either not "Name" or "Primary hand" DUe to all other trait having only numbers as input
      isInputFalse = True
      while isInputFalse:
        print("\033[8;H")
        print("| || Character creation ||")
        print(f"\033[9;H")
        print(
          "| My", x,
          "is:                                                                    "
        )
        print("\033[42;H")
        trait = input()
        if len(trait) <= 8: # The input cant be longer then 8.
          isInputFalse = False
        else: #If it is show error message
          print("\033[10;H")
          print("|", errorMessage1)
        if isANum(trait): # Check if the trait is a number.
          isInputFalse = False # if its a number return that the input is valid of not not false
        else:
          isInputFalse = True # Returns that the input is not a number and counts as a invalid input.
          print("\033[10;H")
          print("| ", errorMessage2, " ", x, ".", sep="")
    else: # If the trait is either "Name" or "Primary hand"
      print("\033[9;H")
      print("| My", x,
            "is:                                                      ")
      print("\033[42;H")
      isInputFalse = True
      while isInputFalse:
        trait = input()
        if len(trait) <= 8: # The input cant be longer then 8.
          isInputFalse = False
        else:
          print("\033[10;H")
          print("| ", errorMessage1)
    #Add the valid trait the the trait list
    chrTraits[x] = trait
    renderGameScreen()


#========================  Screen renders functions ===============================================================================================================================
def renderHP(hp):
  #♥ .♥. ;♥; :♥: |♥|  # 1 2 3 4 5 |❤||❤||❤||❤||❤| ❤ ❤ ❤ ❤ ❤ .❤. ❤
  # A list of hearts that hold diffent values. Health works in the way that 5 normal & makes 5 health. If you want to add 1 hp you replace the first & with the second heart ".&.".
  #Each heart holds +1 value of the one before. Adding the values of all hearts makes the total HP
  heartList = [" -  ", " ♥  ", ".♥. ", ";♥; ", ":♥: ", "|♥| "]
  health = "HP: "
  #Check how many of each heart there should be. It starts with the highest value one and then adds the lower value hearts (if there are any) after.
  for i in range(int(round(((hp / 5) - (int(hp / 5))) * 5))):
    health += heartList[int(hp / 5) + 1]
  for i in range(int(round(((int(hp / 5) + 1) - (hp / 5)) * 5))):
    health += heartList[int(hp / 5)]
  if hp == 0:
    # If the hp is 0 it sets it to 0 hearts
    return "HP:  -    -    -    -    -   "
  else:
    return health


def renderHotBar(monster):
  # A print to move the cursor to line 37.
  print("\033[37;H\033[x")
  # Inputs the totalDmg var so it know if the player has done any damage before running this render.
  global totalDmg
  # If the monster has the id of 0, with means that there is no monster active. Set monster Hp to not show 
  if monster == 0:
    monsterhp = "  "
  # if there is a monster, shown by its iD in the function input monster. Then caluate using the renderHp function the ammount of hearts the monster has - the total damage the player has done.
  else:
    monsterhp = renderHP(int(monsterID[monster][1]) - totalDmg)
  #print the hotbar, renders the monster Name and Hp + the player and its Hp using the addSpaces function to have the end of the gui land on the same place for all inputs.
  print(
    "+-------------------------------------------------------------------------------+------------------+"
  )
  print("|   Player                                  ", monsterID[monster][0],
        addSpaces(32, monsterID[monster][0]), "| E: Exit game     |")
  print("|  ", renderHP(playerHealth),
        addSpaces(38, (renderHP(playerHealth))), monsterhp,
        addSpaces(56,
                  renderHP(playerHealth) + monsterhp), "| I: Inventory     |")
  print(
    "|                                                                               | ?: Obama.sexy    |"
  )
  print(
    "+-------------------------------------------------------------------------------+------------------+"
  )

# A function that prints out or renders the top base part of the GUI. It prints out the trais and calls the function renderHotBar to render the bottom part when done.
def renderGameScreen():
  #start of renderGameScreen
  print("\033c")
  printLogo()
  print(
    "\n+--------------------------------------------------------------------------------------------------+"
  )
  for i in range(7):
    print(
      "|                                                                                                  |"
    )
  print(
    "|                                                                                                  +---------Character Info--------------------+"
  )

  for x in (chrTraits):
    trait = chrTraits[x]
    print("|                                                                                                  |",addSpaces(12, x),x,": ",trait,addSpaces(21, trait),"|",)
  print(
    "|                                                                                                  +-------------------------------------------+"
  )
  for i in range(15):
    print(
      "|                                                                                                  |"
    )
  renderHotBar(0)
# Is a function that takes in a number and a itemID(if 0 no item). And returns what scene the player is on. It also defines the text varible what should be written on the page. The choices array is used to Write what
# choises the player has in any given scene. The goto array determins where the function takes the player when its called again.
# It also calls function for add item, and minigames, and tell them in which part of the story a item should be given or when a minigame should be played.
def renderScene(scene, ItemID):
  global goTo
  if scene == "restart":
    initiateGame()
  if scene == -1:
    text = "Game Over; Restart the game."
    choices = ["", "", "", ""]
  if scene == "replaceinv":
    text = "You inventory is full, what item do you want to replace. Type x if you want discard the item you picking up"
    choices = [items[0], items[1], items[2], items[3]]
  if scene == "addedItem":
    text = "You picked up a " + itemID[ItemID][0]
    choices = ["", "", "", ""]
  if scene == "empty":
    text = ""
    choices = ["", "", "", ""]
  if scene == 0:
    text = "In a far-off land, a great and powerful wizard known as the 'Wise One' had a vision of a great and terrible darkness consuming the world. \
In an effort to protect the people from this darkness, the Wise One created a powerful artifact known as the 'Light of the World. '\
This magical artifact had the power to banish the darkness and bring light to even the darkest of places. \
But the Wise One knew that the Light of the World would not be enough to defeat the darkness forever. He knew that the people of the land would need to be brave and strong to face the challenges that lay ahead. He also knew that they would need to be wise, and be willing to learn from the knowledge and experiences of those who came before them.\
Thus, the Wise One created a game, known as 'Demanding Occasional Light,' as a test for those who sought to prove their worth and protect the world from the darkness. \
The game would be filled with challenges and dangers, but also with opportunities to grow and learn. Those who could overcome these challenges and emerge victorious would be worthy of carrying the Light of the World and leading the people to victory.\
And so, the Wise One summoned all who were brave enough to take up the challenge and enter the game. He bestowed upon them a magical artifact, known as the 'Gem of the Wise,' which would allow them to communicate with him and seek his guidance throughout their journey."
    choices = ["", "", "", ""]
  if scene == 1:
    text = "You wake up in a strange and unfamiliar place, surrounded by darkness. You hear the voice of the Wise One in your head, telling you that you are in the game,\
 and that you must find the Light of the World if you hope to defeat the darkness and save the world. You stand up and take a look around. You see a small lake to your left, and a cave to your right.\
 There is also a computer in front of you, and a small pile of items next to it."
    choices = ["Go fishing in the lake.", "Explore the cave.", "Look through the computer files.", "Pick up the items and add them to your inventory."]
    goTo = [2, 3, 4, 5]
  if scene == 2:
    fishingMinigame(scene,5)
    text = "You spend some time fishing in the lake and manage to catch a few fish. However, as you are about to leave, you feel a tug on your line. \
You reel in and see that you have caught something much larger than a fish - it is a giant sea monster!\
The monster thrashes around, trying to break free of your line. You quickly realize that you won't be able to catch it on your own. You will have to fight it if you want to claim your prize."
    choices = ["Try to fight the sea monster.","Cut the line and run.","", ""]
    goTo = [6, 7]
  if scene == 3:
    text = "You decide to explore the cave and make your way inside. It is dark and cold, and you can hear the sound of dripping water and the occasional scurrying of small animals.\
As you make your way deeper into the cave, you suddenly hear a loud rumbling noise. You turn around just in time to see a massive boulder rolling towards you. You quickly jump out of the way and see that the boulder has stopped in front of a door that you hadn't noticed before."
    choices = ["Try to push the boulder out of the way.", "Look for another way around.", "", ""]
    goTo = [8,9]
  if scene == 4:
    computerExplorer(scene,"main")
    text = "As you browse through the files on the computer, you come across an old document that catches your eye. It appears to be a map of the area, with various locations marked on it. One of the locations is labeled\
 'Light of the World.' You decide to print out the map and add it to your inventory. You also find a few other useful items on the computer, such as a healing potion and a magic scroll. But your too scared to pick them up so you leave them"
    giveItem(3,scene,False)
    choices = ["Leave and move on to the next task.","Take a quiz", "", ""]
    goTo = [11,18]
  if scene == 5:
    giveItem(2,scene,False)
    text = "You decide to pick up the items and add them to your inventory. There are a few useful items, such as a magic scroll, as well as a few less useful items like a broken pen and a piece of paper with meaningless scribbles on it.\
You decide to keep the useful items and discard the rest. You now have room in your inventory for a few more items, should you find any on your journey."
    choices = ["Keep searching for more items.", "Move on to the next task", "", ""]
    goTo = [12, 13]
  if scene == 6:
    renderFightScene(1,scene,False)
    giveItem(6,scene,False)
    text = "The sea monster lets out a deafening roar and falls to the ground, defeated. You are victorious! You add the monster's giant, razor-sharp teeth to your inventory and move on to your next challenge."
    choices = ["Keep exploring the lake.", "Move on to the next task.", "", ""]
    goTo = [14,15]
  if scene == 7:
    text = "You decide to cut the line and run rather than fight the sea monster. As you make your way back to the starting point, you see that the computer is still there, as well as the cave and the lake.\
You realize that there are many paths you can take in this game, and that each decision you make will lead you down a different path. You also realize that no matter which path you choose, you will eventually have to face the darkness and find the Light of the World if you hope to save the world.\
You decide to take a moment to catch your breath and think about your next move."
    choices = ["Go fishing.", "Explore the cave.", "Search the computer for more information.", ""]
    goTo = [2,3,4]
  if scene == 8:
    text = "You decide to try and push the boulder out of the way. You put your shoulder against it and push with all your might. The boulder budges slightly, but then comes to a halt. You realize that you won't be able to move it on your own.\
You decide to look for another way around. You find a small tunnel that leads around the boulder and continues deeper into the cave. You crawl through the tunnel and emerge on the other side.\
As you continue exploring the cave, you come across a group of monsters. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to find out."
    choices = ["Fight the monsters.", "Try to sneak past them.", "", ""]
    goTo = [16,17]
  if scene == 9:
    text = "You decide to look for another way around the boulder. You find a small tunnel that leads around it and continues deeper into the cave. You crawl through the tunnel and emerge on the other side.\
As you continue exploring the cave, you come across a group of monsters. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to find out."
    choices = ["Fight the monsters.", "Try to sneak past them.", "", ""]
    goTo = [16,17]
    
  if scene == 10:
    computerExplorer(scene,"main")
    text = "You think your ready to retake the quiz"
    choices = ["Take the quiz", "", "", ""]
    goTo = [18]
  if scene == 11:
    text = "You decide to leave the computer and move on to your next task. You leave the starting point and begin your journey.\
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters.", "Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 12:
    giveItem(8,scene,False)
    text = "You decide to keep searching for more items. As you search, you come across a few more useful items, such as a magic potion and a powerful weapon known as the 'Thunder Sword.' You add these items to your inventory, but you soon realize that your inventory is full."
    choices = ["Keep searching for more items.", "Move on to the next task.", "", ""]
    goTo = [22,23]
  if scene == 13:
    text = "You decide to move on to your next task. You leave the starting point and begin your journey.\
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters.", "Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 14:
    giveItem(7,scene,False)
    text = "You decide to continue exploring the lake. As you fish, you come across a few more fish, as well as a few other strange and unusual items, such as a glowing rock and a magic amulet. A fish from the lake scares you into dropping the amulet into the lake. You add the glowing rock to your inventory."
    choices = ["Keep fishing","Move on to the next task", "", ""]
    goTo = [24,25]
  if scene == 15:
    text = "You decide to move on to your next task. You leave the starting point and begin your journey.\
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters.", "Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 16:
    renderFightScene(3,scene,False)
    text = "You are victorious! You loot the monsters for any valueble items and move on to your next challenge."
    choices = ["Keep exploring the cave.","Move on to the next task.", "", ""]
    goTo = [26,27]
  if scene == 17:
    text = "You decide to try and sneak past the monsters. You carefully and quietly make your way around them, trying not to draw attention to yourself.\
As you pass by, one of the monsters suddenly notices you and lets out a loud growl. The other monsters turn to look at you and begin to give chase.\
You quickly turn and run, your heart pounding in your chest. You can hear the monsters hot on your heels, their sharp claws and teeth glinting in the dim light of the cave.\
You manage to outrun the monsters and escape, but you know that you will have to face them again if you hope to find the Light of the World."
    choices = ["Keep exploring the cave.","Move on to the next task.", "", ""]
    goTo = [26,27]
  if scene == 18:
    outCome = quizContollPanel(scene,3)
    if outCome == "win":
      text = "The quiz is now complete, and you have successfully passed it."
      choices = ["Leave and move on to the next task.", "", "", ""]
      goTo = [11]
    if outCome == "loose":
      text = "You failed the quiz, but its not letting you go without completing it. You decide to continue searching the computer for the answers to the quiz question."
      choices = ["Keep searching the computer for more information.", "", "", ""]
      goTo = [10]
  if scene == 20:
    renderFightScene(3,scene,False)
    text = "The remaining monsters let out a deafening roar and fall to the ground, defeated. You are victorious! Feeling proud over your victory you move on to your next challenge."
    choices = ["Keep exploring the wilderness.", "Move on to the next task.", "", ""]
    goTo = [28,29]
  if scene == 21:
    text = "You decide to try and find another way around the monsters. You carefully and quietly make your way around them, trying not to draw attention to yourself.\
As you pass by, one of the monsters suddenly notices you and lets out a loud growl. The other monsters turn to look at you and begin to give chase.\
You quickly turn and run, your heart pounding in your chest. You can hear the monsters hot on your heels, as you run through a forest you can hear the struggle.\
You manage to outrun the monsters and escape, but you know that you will have to face them again if you hope to find the Light of the World."
    choices = ["Keep exploring the wilderness", "Move on to the next task", "", ""]
    goTo = [28,29]
  if scene == 22:
    text = "You find no more usefull items on you searth and decides to give up and move on."
    choices = ["Move on to the next task.","", "", ""]
    goTo = [23]
  if scene == 23:
    text = "You decide to move on to your next task. You leave the starting point and begin your journey.\
                                                                                                          \
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters", "Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 24:
    fishingMinigame(scene,10)
    giveItem(9,scene,False)
    text = "You decide to keep fishing. As you fish, you come across a few more fish, as well as a few other strange and unusual items, a magic amulet. You add these items to your inventory."
    choices = ["Move on to the next task.","", "", ""]
    goTo = [25]
  if scene == 25:
    text = "You decide to move on to your next task. You leave the starting point and begin your journey.\
                                                                                                          \
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters", "Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 26:
    text = "You decide to continue exploring the cave. As you make your way deeper into the cave, you start to hear loud rumble from the cave cealing."
    choices = ["Run further into the cave","Run back and exit the cave", "", ""]
    goTo = [30,31]
  if scene == 27:
    text = "You decide to move on to your next task. You leave the cave and begin your journey.\
As you make your way through the wilderness, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters.","Find another way around them.", "", ""]
    goTo = [20,21]
  if scene == 28:
    text = "As you explore the wilderness you get distracted by the nature, and fall down a hole. As you wake and discover the surroundings you spot a group of monsters. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to find out."
    choices = ["Fight the monsters.", "Try to sneak past them.", "", ""]
    goTo = [16,17]
  if scene == 29:
    text = "You decide to move on to your next task. You leave the wilderness and begin your journey.\
As you make your way through the dark and treacherous caves, you come across a group of monsters blocking your path. They seem to be guarding something, but you can't see what it is. You will have to fight them if you want to continue on your journey."
    choices = ["Fight the monsters.", "Try to sneak past them.", "", ""]
    goTo = [16,17]
  if scene == 30:
    stoneDogeMinigame(scene)
    text = "In the deepest parts of the cave you see a light, this light shines at you from a far grabbing your attention. Its the Light of the World, a small orb like artifact. As you come closer the the orb you hear the 'Wise one's' words\
      You have completed the quest, I now know you are worthy of carrying the Light of the World and leading the people to victory. Thank you"
    choices = ["Win","","",""]
    goTo = [32]
  if scene == 31:
    text = "As you make your way back to the starting point, you see that the computer is still there, as well as the cave and the lake.\
You realize that there are many paths you can take in this game, and that each decision you make will lead you down a different path. You also realize that no matter which path you choose, you will eventually have to face the darkness and find the Light of the World if you hope to save the world.\
You decide to take a moment to catch your breath and think about your next move."
    choices = ["Go fishing.", "Explore the cave.", "Search the computer for more information.", ""]
    goTo = [2,3,4]
  if scene == 32:
    text = "Thank you for playing this game. Its really bad and was made just for fun. Bye"
    choices = ["Restart"]
    goTo = ["restart"]
  print("\033[8;H")
  writeAnimation(text)
  writeChoices(choices)

# This function takes the text varible as input and slowly prints it out on the the screen. This makes the effect that the text is writen as you read.
def writeAnimation(text):
  printLetter = "|      "
  line = 10
  n = 0
  Time = 0.05
  for i in range(len(text)):
    if n == 80:
      if " " in (text[i - 1], text[i]):
        printLetter += "\n"
      else:
        printLetter += "-\n"
    if n == 81:
      line += 1
      printLetter = "|      " + text[i - 1]
      n = 0
    printLetter += text[i]
    print(f"\033[{line};H")
    print(printLetter)
    if inventoryOpen == False and closeInventory == False: # if the inventory is not open then the write animation should be played.
      if keyboard.is_pressed("space"):
        Time = 0
      time.sleep(Time)
    if inventoryOpen == True or closeInventory == True: # If the inventory is open the player should be able to close it without the slow animation running everytime.
      time.sleep(0)
    n += 1

# This function prints out the 1 to 4 diffrent choises on the screen and what they are.
def writeChoices(array):
  print("\033[29;H\033[x")
  for i in range(len(array)):
    if array[i] == "":
      break
    print("|     ",str(i+1),":",array[i] + addSpaces(86,array[i]),"|")
    print("|",addSpaces(95,""),"|")
  print("\033[42H")

# This function renders the inventory and show the player what items the player has.
def renderInventory():
  print("\033[26;H\033[x")
  print(
    "\n|        +----Inventory-------------------------------------------------------X: Close----+ "
  )
  for i in range(4):
    print(
      "|        |                                                                                |"
    )
    print("|        |                  Slot", i + 1, "-", items[i],
          addSpaces(50, items[i]), "|")
  print(
    "|        |                                                                                |"
  )
  print(
    "|--------+--------------------------------------------------------------------------------+-"
  )
  print("\033[42H")
# A function that is the master of the other render function. It makes it so you only have to call 1 function instead of 3 Its called when you want a complete GUI with or without the inventory renderd.
def renderGame(scene, inventory, ItemID):
  renderGameScreen()
  renderScene(scene, ItemID)
  if inventory == True:
    renderInventory()


#=============================================FightScene====================================================================================================
# Renders the fightscene a player is in. It takes in a monsterID so it knows what monster it should render. A scene so that for everyscene it only happens once. A value if this fightscene is a fishing drop since
# it should not only be player once but everytime you fish up a monster.
def renderFightScene(monster, scene,fishUp): 
  global totalDmg, playerHealth, fightSceneHasDone

  def renderAttacks():

    def attack(slot): # renders the diffrent attacks the player can do. It also checks the type of the weapond / item as it has to make a diffrent prompt for each type of weapond.
      for i in range(len(itemID)):
        if items[slot-1] == itemID[i][0]:
          if itemID[i][1] == "none":
            return "Punch " + monsterID[monster][0]
            
          if itemID[i][1] == "item":
            return "Give " + monsterID[monster][0] + " a " + itemID[i][0]
            
          elif itemID[i][1] == "knife":
            return "Stab " + monsterID[monster][0] + " with " + itemID[i][0]
            
          elif itemID[i][1] == "sword":
            return "Attack " + monsterID[monster][0] + " with " + itemID[i][0]
          elif itemID[i][1] == "magic":
            return "Use " + itemID[i][0] + "to cast magic at " + monsterID[monster][0]
          elif itemID[i][1] == "healing":
            return "Heal" + monsterID[monster][0] + "With healing potion"
  # Prints out the GUI
    print("\033[1F")
    for i in range(4):
      print("| ",str(i+1),": ", attack(i+1), addSpaces(69, attack(i+1)), "|")
      print(
            "|                                                                               |"
           )
    print(
      "+-------------------------------------------------------------------------------+"
    )
# Returns the item damage value from the items dictionary to calculate how much damage the player did. 
  def attackDamageCalc(slot):
    for i in range(len(itemID)):
      if items[slot - 1] == itemID[i][0]:
        return int(itemID[i][2])
# A varible to check if the player is in a fight
  inFight = True
  if not scene in fightSceneHasDone or fishUp == True: # Checks if the current scene / storyNumber already have played this fight.
    fightSceneHasDone.append(scene)

    while inFight == True:
      if int(monsterID[monster][1]) <= totalDmg: # checks if the monster is dead. By comparing the total dmg to the hp of the monster.
        inFight = False
        renderGame("empty", False, 0) # Renders an empty background.
      elif playerHealth <= 0:
        renderGame("empty", False, 0)
        initiateGame()
        inFight = False
      else: # If the monster is not killed play the fight.
        print("\033[6;H\033[x")
        for i in range(36): # Take a line from the txt file for the monster to render an image of the fight scene. The image is 36 rows and starts in the second line of the file.
          print(linecache.getline("fightscene/" + monsterID[monster][0] + '.txt', i + 2)) # takes the name of the monster and uses the linecache module to import the line
          print(f"\033[{i+7};H") # Moves the line 1 row up due to the linecache function having a enter after each print
        renderHotBar(monster) # renders the hotbar with the correct monster and HP
        renderAttacks() # Renders the types of attacks the player can do.
        action = input().lower() # Takes an input and continues acording to that input.
        if action == "i": # Does nothing if the action is i or x
          print("")
        elif action == "x":
          print("")
        elif action in ["1", "2", "3", "4"]:
          totalDmg += attackDamageCalc(int(action)) 
          playerHealth -= int(monsterID[monster][2])
          for i in range(len(itemID)):
            if items[int(action)-1] == itemID[i][0]:
              if itemID[i][1] == "healing":
                totalDmg -= 4
        elif action == "e":
          initiateGame() # Exits the game


#==================================== Minigames renderer ===================================================================================================

global sprites
maxHight = 29  #max hight of the screen
maxWidth = 98  #max widht of the screen
        
   
sprites = {0 : ["player",[7, 22],[5, 5]]} #Sprite ID : [Sprite name, [Sprite x, Sprite y], [Sprite width, sprite height]]  sprites[spriteID][0-2][0-1]

global timer
timer = 0 # A varible for a timer that makes it so it does not render a new frame everytime the code runs.
# A function that renders the minigame and all its sprites
def renderMinigameFrame(renderGraf,minigame):
  print("\033[8;H\033[x") # Start at line 8
  def spriteRender(x, y, spriteID,renderGraf,minigame):
    # Define varibles from other functions that are needed to draw the sprites
    global whereLineHitsWater ,fishingRodRenderDelay, grafY, amountOfFish, fishGoal
    fishGoalY = 1 # What y level the fishing goal text is at
    fishGoalX = 20 # What x level the text is
    fishAmountY = 1
    fishAmountX = 18
    sprite_name = sprites[spriteID][0]
    sprite_x = sprites[spriteID][1][0]
    sprite_y = sprites[spriteID][1][1]
    sprite_width = sprites[spriteID][2][0]
    sprite_height = sprites[spriteID][2][1]
    # Checks if the fishing minigame is active.
    if x == fishGoalX and y == fishGoalY and minigame == "fishing":
      return str(fishGoal)
    if x == fishAmountX and y == fishAmountY and minigame == "fishing":
      return str(amountOfFish)

# Checks the x and y cordinate from parameter and checks if the cordinate exists between the top left most point of a sprite and the bottom right most part of the sprite. 
    if sprite_x <= x <= sprite_x + sprite_width and sprite_y <= y <= sprite_y + sprite_height:
      #If the x and y exists within the sprite it loops through x and y to find the exact cordinate.
      for sy in range(sprite_height): 
        for sx in range(sprite_width):
          if x == sprite_x + sx and y == sprite_y + sy: # It checks the sprite_y and sprite_x which are the cords for the top left corner plus some value from 0 to the width and height of the sprite.
            spritePixel = list(linecache.getline("sprites/" + minigame + "/" + sprite_name + '.txt', sy + 1)) # When it find the exact position of the cordinate x and y within the sprite its
            #collect and return what chracater/letter/number should be at that x and y. By taking the correct line form the sprite txt file and making it into a list.
            return spritePixel[sx] # Then it return the value at the index sx. If you get error index out of range, make sure the width and height is the same as the widht and height in the txt file or check filename for diffrences. Including spaces
            # because there will be an error if the width and height dont match the file, and the code will try to grab something that does not exist.
            
            # An example: 555  This sprite is 3x3 and contains letters/numbers. This sprite has an x and y, and a width(3) and height(3). All codinates within a sprite can be calculated by adding
            #             5g5  a number bewteen 0 and the width for x and y = a number between 0 and height. This addon x and y is called sx and sy.
            #             555  The value at that cordinate is then returned to the main function

      return "" # If the cords x and y is not within the sprite there is no need to loop throught the sprite and that x and y value for now will have a space.
    elif renderGraf == True: # If the function should render the graf of the fishing rod.
      if 35 < x < 35 + fishingRodRenderDelay: #This limits the function to only be drawn between x=35 and x = 35 + varible. The varible is so that the graf can be drawn in steps to mimic the line of a fishing rod being cast.
        grafX = x - 35 #Puts x = 0 for the graf at x = 35
        a = (8/((int(whereLineHitsWater)+1)**2)) # Defines a "a" value to ax^2 so that the graf intersects at x + whereLineHitsWater
        grafY = round(a*grafX**2 + 8) # It then calculated the quadradic and prints that.
        if y == grafY: # If the y cordinate is the same then return a 1. 
          return "1"
        else: # If not make it a space
          return ""
      else:
        return ""
    else:
      return ""



  line = "|" # This makes it so for each row the first char will always be the same.
  for y in range(maxHight): # Defines how many rows there should be in the renderd image
    for x in range(maxWidth): # Defines how many characters there should be in each row.
      for spriteID in range(len(sprites)): # Loops through each sprite to compare if that x and y is the same for any cordinate in a sprite and then render that sprite at the correct pos.
        if spriteRender(x, y, spriteID,renderGraf,minigame) != "": # Checks if the x and y contains a sprite
          line += spriteRender(x, y, spriteID,renderGraf,minigame) # Ads the part of the sprite to the line.
          break # Breaks the loop so no more sprites are compared, due too only 1 sprite can be drawn at any given x and y
      if spriteRender(x, y, spriteID,renderGraf,minigame) == "": # If that x and y is empty return a space
        line += " "
    line += "|" # After all x cordinates are loopt through add the end char.
    print(line) # Print that line
    line = "|" # Set line to the default.


def collide(sprites1,sprites2):
  global sprites
  for spriteID1 in sprites1:
    for spriteID2 in sprites2:
      sprite1_height = sprites[spriteID1][2][1]
      sprite1_width = sprites[spriteID1][2][0]
      sprite2_height = sprites[spriteID2][2][1]
      sprite2_width = sprites[spriteID2][2][0]
      for sy1 in range(sprite1_height):
        for sx1 in range(sprite1_width):
          for sy2 in range(sprite2_height):
            for sx2 in range(sprite2_width):
              sprite1Y = sprites[spriteID1][1][1] + sy1
              sprite1X = sprites[spriteID1][1][0] + sx1
              sprite2Y = sprites[spriteID2][1][1] + sy2
              sprite2X = sprites[spriteID2][1][0] + sx2
              if sprite1X == sprite2X and sprite1Y == sprite2Y:
                return True
            
  return False
#=============================================================================Minigames
def quizContollPanel(scene,amountOfQuestions):
  global sprites, updateFrame, questionsAnswerdCorrect, totalQuestionsAnswerd, questionList
  def resetSprites(): # Defines all the sprites used in the quiz controll panel minigame.
    global sprites
    sprites = {
      0 : ["question1",[-60,10],[27,1]],
      1 : ["question2",[-60,10],[33,1]],
      2 : ["question3",[-60,10],[12,1]],
      3 : ["question4",[-60,10],[54,1]],
      4 : ["answer1",[-60,14],[19,1]],
      5 : ["answer2",[-60,14],[24,1]],
      6 : ["answer3",[-60,14],[16,1]],
      7 : ["answer4",[-60,14],[23,1]],
      8 : ["answerwrong",[-60,12],[11,1]],
      9 : ["answerright",[-60,12],[13,1]],
      10 : ["background",[0,0],[98,29]],
              }
  resetSprites()
  if not scene in quizHasDone: # Checks if the quiz has already been done on this specific scene
    quizHasDone.append(scene) # If not add the scene to a list.
    # define the default state of all varibles
    questionsAnswerdCorrect = 0 
    totalQuestionsAnswerd = 0
    inQuiz = True
    frameUpdatetimer = 0
    updateFrame = 0
    # The index number coresponds to the question ID In correct list "obama" has index number 0 it corrispondents to the value in questionlist index number 0
    questionList = [0,1,2,3] # Sprite ID for the questions
    answerList = [4,5,6,7] # Sprite ID for the answers
    correctList = ["obama","obama.sexy","19","joe obama"] # The correct answer to the questions
    answerWrongID = 8 
    answerRightID = 9
    def askQuestion(): # A function that askes the questions
      resetSprites() # Reset all sprites to outside the windows exept the background
      global questionList, questionsAnswerdCorrect, totalQuestionsAnswerd
      if len(questionList) == 1:
        questionNumber = questionList[0]
      else:
        questionNumber = random.randrange(0,len(questionList)) # pick a random question
      questionList.pop(questionNumber)
      sprites[questionNumber][1][0] = 20 # move the question text to a visible place on the sceen.
      renderMinigameFrame(False,"quiz") #Render the question
      answer = input("Answer: ") # Ask for a answer
      if answer == correctList[questionNumber]: # If the answer is correct, move the "You where right text" to the screen
        sprites[answerRightID][1][0] = 20
        questionsAnswerdCorrect += 1 # adds how many questions that have been answerd correctly
        totalQuestionsAnswerd += 1 # Add a 1 to the total questions answerd
      else: # If wrong
        sprites[answerWrongID][1][0] = 20 #Move the "You where wrong text" to the screen
        totalQuestionsAnswerd += 1 # add total questions +1
      answerSpriteNumber = answerList[questionNumber] # Get the id for the sprite
      sprites[answerSpriteNumber][1][0] = 20 # Move the right answer to the screen
      renderMinigameFrame(False,"quiz") # render the screen
      time.sleep(2) # Wait to seconds before continuing





    def update(): # A function that updates everything in the minigame
      global updateFrame
      if updateFrame > 1: # A varible to slow down how fast the screen is renderd
        print("\033[8;H") # Moves the cursor to the 8 row
        renderMinigameFrame(False,"quiz") #renders the screen
        askQuestion() # ask question
        updateFrame = 0
      updateFrame += 1
    renderGame("empty", False, 0) # When staring the quiz render a blank background
    while inQuiz == True: # While in quiz
      frameUpdatetimer += 1
      if questionsAnswerdCorrect >= amountOfQuestions: # if the amount of questions answerd correctly is the same as the amount of questions needed the player wins
        keyboard.send("enter")
        renderGame("empty", False, 0)
        inQuiz = False
        return "win"
      if totalQuestionsAnswerd >= amountOfQuestions: # If the amount of questions is not the same then the player lost.
        keyboard.send("enter")
        renderGame("empty", False, 0)
        inQuiz = False
        return "loose"
      if frameUpdatetimer == 100000: # Even bigger timer that slows down the rate that the update function is called
        update()
        frameUpdatetimer = 0

def fishingMinigame(scene,goal): # A function to render the fishing minigame
  global castingRod, sprites, fishingRodRenderDelay, reelInLine, hookInWater, amountOfFish, fishingMinigameHasDone, castTime, waitTime, giveLoot, ableToCatchFish, grafY, fishGoal
  fishGoal = goal
  # Define and place all the sprites used in the fishing minigame
  sprites = {0 : ["fishingrod",[28,8],[7,11]],
             1 : ["fisherman",[21,10],[11,16]],
             2 : ["dock",[0,18],[26,10]],
             3 : ["water",[0,28],[98,1]],
             4 : ["fishinggamecontrolls",[55,1],[42,2]],
             5 : ["fishonhook",[-20,0],[15,1]],
             6 : ["amountoffish",[3,1],[19,1]]
            }
  if not scene in fishingMinigameHasDone: # Checks if this fishing minigame has been played before.
    fishingMinigameHasDone.append(scene) # if not add the scene to a list.
    # Define all starting values for the fishing minigame
    giveLoot = False
    inFishingMinigame = True
    frameUpdatetimer = 0
    amountOfFish = 0  
    castingRod = False
    reelInLine = False
    hookInWater = False
    castTime = 0
    waitTime = 0
    fishingRodRenderDelay = 0
    ableToCatchFish = False
    def loot(): # A function that chooses what loot to give the player when reeling in the fishing rod.
      global amountOfFish
      loot = random.randrange(0,15)
      if loot <= 2:
        keyboard.send("enter")
        renderFightScene(2,-1,True) # Chance to start a fight scene
      elif 3 >= loot > 2:
        keyboard.send("enter")
        lootTable = [1,4,5]
        item = lootTable[random.randrange(0,(len(lootTable)-1))]
        giveItem(item,-1,True) # Chance to get an item
      elif loot >= 4:
        amountOfFish += 1 # Chance to fish up a fish
      
    def fishingLine(): # A function to controll the fishing line.
      global fishingRodRenderDelay, whereLineHitsWater, castingRod, spaceUp, reelInLine, hookInWater, castTime, waitTime, giveLoot, ableToCatchFish
      def hookInWaterCheck(): # A check to see if the fishing hook is in the water or not.
        if grafY < 29:
          return False
        else:
          return True

      if hookInWater:
        if waitTime == 0:
          waitTime = random.randrange(100,200) # Choose a random number that the player will have to wait before a fish will appear on the hook

        if castTime > waitTime and ableToCatchFish == False: # If the timer has passed, move a text to tell the player to reel in. 
          sprites[5][1][0] = 80
          sprites[5][1][1] = 10
          ableToCatchFish = True # Now the player is able to get a fish
          castTime = 0
        castTime += 1

      if castTime < 50 and hookInWater == False and ableToCatchFish == True: # If the has reeled in his fishing rod before a new timer has passed. The player get loot.
        sprites[5][1][0] = -40
        sprites[5][1][1] = -10
        ableToCatchFish = False
        waitTime = 0
        castTime = 0
        giveLoot = True

      elif castTime > 50 and ableToCatchFish == True: # If the player has reeled in his fishingrod but to late he is not given any loot.
        sprites[5][1][0] = -40
        sprites[5][1][1] = -10
        ableToCatchFish = False
        waitTime = 0
        castTime = 0
        giveLoot = False

      if giveLoot: # Gives the player loot
        loot()
        giveLoot = False

      if reelInLine: # If the plater reeled in the line.
        whereLineHitsWater -= 1 # This makes the graf shorter and gives the illusion that the fishing line is reeled in.
        fishingRodRenderDelay -= 2 # Removes how much of the graf that is visible to the player. Making it so it lookes reeled in.
        if fishingRodRenderDelay < -1: # If the fishing line is all the way in. 
          reelInLine = False
          castingRod = False
          whereLineHitsWater = 10
          fishingRodRenderDelay = 0
        hookInWater = hookInWaterCheck()
      if castingRod == True and reelInLine == False: # If the player casts the rod, the varible that controlls how much of the graf is shown gets bigger
        if grafY < 29: # If the hook is in the water stop adding to the graf.
          fishingRodRenderDelay += 4
        hookInWater = hookInWaterCheck() # check if the hook is in water
      if keyboard.is_pressed("space"):
        if castingRod == True and spaceUp == False and reelInLine == False and fishingRodRenderDelay > 10: # If the player is able to reel in and presses space then reel in.
          reelInLine = True
        if castingRod == False: # If the player holds space make it so the point where the line hits the water is further away from the dock.
          whereLineHitsWater += 1
          spaceUp = True
          if whereLineHitsWater > 35: # A maximum lenght away from the dock.
            castingRod = True
      else:
        if whereLineHitsWater > 10: # If the player stop pressing space and whereLineHitsWater is big enought cast the rod.
          castingRod = True
        spaceUp = False

    def update():
      global updateFrame
      if updateFrame > 1:
        print("\033[8;H")
        renderMinigameFrame(castingRod,"fishing")
        fishingLine()
        updateFrame = 0
      updateFrame += 1
    renderGame("empty", False, 0)
    while inFishingMinigame == True:
      frameUpdatetimer += 1
      if frameUpdatetimer == 100000:
        if amountOfFish >= goal: # If the fish goal is meet take the player back to the story
          keyboard.send("enter")
          renderGame("empty", False, 0)
          inFishingMinigame = False

        update()
        frameUpdatetimer = 0
    

def stoneDogeMinigame(scene): # A function for the stone minigame
  global sprites
  def resetSprites():
    global sprites
    sprites = {0 : ["ground",[0,27],[98,2]],
               1 : ["player_walk1",[7, 10],[5, 8]],
               2 : ["smallstone",[110,23],[8,4]],
               3 : ["tallstone",[120,21],[8,6]],
               4 : ["gameovertext",[-20,0],[9,1]],
               5 : ["controlls",[4,2],[16,1]]
              }
  resetSprites()
  global stoneDogeMinigameHasDone
  if not scene in stoneDogeMinigameHasDone:
    stoneDogeMinigameHasDone.append(scene)

    def controllRocks():
      global spawnRock ,sprites, rockType
      if spawnRock:
        rockType = random.randrange(2,4)
        spawnRock = False
      sprites[rockType][1][0] -= random.randrange(1,4)
      if sprites[rockType][1][0] < -5:
        sprites[rockType][1][0] = 120
        spawnRock = True
    def playerJump(onGround): # A function that allowes the player to jump
      def swapSprite(): # Swap the sprites look based on previous frame
        global activeSprite
        global sprites
        if onGround == False:
          sprites[1][0] = "player_jump"
          activeSprite = 3
        if onGround == True:
          if activeSprite == 3:
            sprites[1][0] = "player_walk1"
            activeSprite = 1
          elif activeSprite == 1:
            sprites[1][0] = "player_walk1"
            activeSprite = 2
          elif activeSprite == 2:
            sprites[1][0] = "player_walk2"
            activeSprite = 1


      global activeSprite, jumpUpdateTimer, gravity, jump_height, y_velocity,jumping, timer
      if onGround:
        if activeSprite == 3:
          activeSprite = 1
        if timer > 10:
          swapSprite()
          timer = 0
        timer += 1
        jumping = False
        y_velocity = jump_height
        if keyboard.is_pressed("space"):
          jumping = True

      if jumping == True:
        swapSprite()
        if jumpUpdateTimer >= 2:
          sprites[1][1][1] -= y_velocity #The volocity of the player up when jumping.
          y_velocity -= gravity # Decreses over time when gravity affects the player
          jumpUpdateTimer = 0
        jumpUpdateTimer += 1
      if onGround == False and jumping == False:
        sprites[1][1][1] += gravity
        swapSprite()

    def collition():
  
      global onGround
      player = [1]
      ground = [0]
      rocks = [2,3] #id that will collide with the player and kill it
      if collide(player,rocks) == True: # Check if the player is colliding with any rocks.
        killPlayer()
      if collide(player,ground) == True:# Check if the player is standing on the ground
        onGround = True
      else:
        onGround = False
    def killPlayer(): # Show the game over text and reset everything.
      global sprites, jump_height, y_velocity, jumping
      sprites[4][1] = [47,12]
      renderMinigameFrame(False,"stonedoge")
      time.sleep(2)
      jumping = False
      y_velocity = jump_height
      resetSprites()

    def update():
      global onGround
      print("\033[8;H")
      renderMinigameFrame(False,"stonedoge")
      collition()
      controllRocks()
      playerJump(onGround)
    instoneDogeMinigame = True
    global jumpUpdateTimer, updateFrameTimer, activeSprite, spawnRock, rockType
    rockType = None
    spawnRock = True
    jumpUpdateTimer = 0
    updateFrameTimer = 0
    distance = 0
    renderGame("empty", False, 0)
    activeSprite = 1
    while instoneDogeMinigame == True:
      update()
      if distance > 1000: # How long the player has to run to win. If the distance run is larger den the goal then the player win and can continue.
        renderGame("empty", False, 0)
        instoneDogeMinigame = False
        distance = 0
      distance += 1
#=============================================================================Interactible Objects================
def computerExplorer(scene,start):

  global sprites, computerHasDone, window, filePath, inComputer
  # Define and place all the sprites used in the computer.
  def resetSprites(): 
    global sprites
    sprites = {0 : ["answerstextfile",[-100,-100],[72,1]],
              1 : ["glubbslimetextfile",[-100,-100],[72,1]],
              2 : ["gtextfile",[-100,-100],[72,1]],
              3 : ["liferanttextfile",[-100,-100],[72,1]],
              4 : ["moneyfolder",[-100,-100],[72,1]],
              5 : ["monsterfolder",[-100,-100],[72,1]],
              6 : ["mutadedfishtextfile",[-100,-100],[72,1]],
              7 : ["navbar",[-100,-100],[72,1]],
              8 : ["newquestionstextfile",[-100,-100],[72,1]],
              9 : ["personalfolder",[-100,-100],[72,1]],
              10 : ["problemstextfile",[-100,-100],[72,1]],
              11 : ["quizfolder",[-100,-100],[72,1]],
              12 : ["taxestextfile",[-100,-100],[72,1]],
              13 : ["arrow",[-100,-100],[1,1]],
              14 : ["background1",[0,0],[98,4]],
              15 : ["background2",[0,4],[13,25]],
              }
  if not scene in computerHasDone: # Checks if this computer has been interacted before.
    computerHasDone.append(scene) # if not add the scene to a list.
    resetSprites()
    global selectorActive
    selectorActive = True
    def spriteLocation(folder): # Instead of editing indevidual cordinated we use a function to define all sprites needed and thier cordinates.
      global sprites, keyIsPressed, selectorActive
      keyIsPressed = False
      resetSprites()
      # each if statement corresponds to a folder or file.
      if folder == "main":
        selectorActive = True
        sprites = {0 : ["navbar",[17,4],[72,1]],
                   1 : ["arrow",[15,6],[1,1]],
                   2 : ["moneyfolder",[17,6],[72,1]],
                   3 : ["monsterfolder",[17,8],[72,1]],
                   4 : ["personalfolder",[17,10],[72,1]],
                   5 : ["liferanttextfile",[17,12],[72,1]],
                   6 : ["background1",[0,0],[98,4]],
                   7 : ["background2",[0,4],[13,25]],  
                  }
      elif folder == "money":
        selectorActive = True
        sprites = {0 : ["navbar",[17,4],[72,1]],
                   1 : ["arrow",[15,6],[1,1]],
                   2 : ["problemstextfile",[17,6],[72,1]],
                   3 : ["taxestextfile",[17,8],[72,1]],
                   4 : ["background1",[0,0],[98,4]],
                   5 : ["background2",[0,4],[13,25]],
                  }
      elif folder == "monster":
        selectorActive = True
        sprites = {0 : ["navbar",[17,4],[72,1]],
                   1 : ["arrow",[15,6],[1,1]],
                   2 : ["glubbslimetextfile",[17,6],[72,1]],
                   3 : ["mutadedfishtextfile",[17,8],[72,1]],
                   4 : ["background1",[0,0],[98,4]],
                   5 : ["background2",[0,4],[13,25]],
                  }
      elif folder == "personal":
        selectorActive = True
        sprites = {0 : ["navbar",[17,4],[72,1]],
                   1 : ["arrow",[15,6],[1,1]],
                   2 : ["quizfolder",[17,6],[72,1]],
                   3 : ["gtextfile",[17,8],[72,1]],
                   4 : ["snakefile",[17,10],[72,1]],
                   5 : ["background1",[0,0],[98,4]],
                   6 : ["background2",[0,4],[13,25]],
                  }
      elif folder == "quiz":
        selectorActive = True
        sprites = {0 : ["navbar",[17,4],[72,1]],
                   1 : ["arrow",[15,6],[1,1]],
                   2 : ["answerstextfile",[17,6],[72,1]],
                   3 : ["newquestionstextfile",[17,8],[72,1]],
                   4 : ["background1",[0,0],[98,4]],
                   5 : ["background2",[0,4],[13,25]],
                  }
      elif folder == "liferanttext":
        sprites = {0: ["liferanttext",[2,1],[95,12]]}
        selectorActive = False
      elif folder == "problemstext":
        sprites = {0: ["problemstext",[2,1],[95,18]]}
        selectorActive = False
      elif folder == "taxestext":
        sprites = {0: ["taxestext",[2,1],[95,17]]}
        selectorActive = False
      elif folder == "glubbslimetext":
        sprites = {0: ["glubbslimetext",[2,1],[93,19]]}
        selectorActive = False
      elif folder == "mutadedfishtext":
        sprites = {0: ["mutadedfishtext",[2,1],[95,19]]}
        selectorActive = False
      elif folder == "gtext":
        sprites = {0: ["gtext",[2,1],[96,11]]}
        selectorActive = False
      elif folder == "answerstext":
        sprites = {0: ["answerstext",[2,1],[66,7]]}
        selectorActive = False
      elif folder == "newquestionstext":
        sprites = {0: ["newquestionstext",[2,1],[26,1]]}
        selectorActive = False
      elif folder == "snake":
        snakeGame()
        if len(filePath) > 1:
          filePath.pop(-1) 
        spriteLocation(filePath[-1]) 

      else:
        resetSprites()
    def moveSelector(): # A function that allows the player to move the selector up and down. But also entering a file or folder and exiting back. 
      global selectorActive
      if selectorActive == True:
        arrowSprite = 1
        topFolder = sprites[2][1][1] # The first folder/file the selector can select
        bottomFolder = topFolder + ((len(sprites)-5) * 2) # The last folder/file the selector can select
      global keyIsPressed, window, filePath, inComputer
      # KeyisPressed needed so a button cant be pressed multiple times.
      if keyboard.is_pressed("d"):
        if keyIsPressed == False and selectorActive == True:
          # ((sprites[arrowSprite][1][1]-10)/2) + 1 gets what spriteID the selector is selecting. And the rest removes folder and file from the sprite name. So i can be used in the Spritelocation function
          window = sprites[((sprites[arrowSprite][1][1]-4)/2) + 1][0].replace("file","folder").replace("folder","")
          filePath.append(window)
          spriteLocation(window)
          
        keyIsPressed = True
      elif keyboard.is_pressed("a"):
        if keyIsPressed == False:
          if len(filePath) > 1:
            filePath.pop(-1) 
          spriteLocation(filePath[-1]) 
          
        keyIsPressed = True
       # If selector cords is within the first and last file it can move up and down
      elif keyboard.is_pressed("s"):
        if keyIsPressed == False and selectorActive == True and topFolder-1 < sprites[arrowSprite][1][1] < bottomFolder:
          sprites[arrowSprite][1][1] += 2
          
        keyIsPressed = True
      elif keyboard.is_pressed("w") and selectorActive == True and topFolder < sprites[arrowSprite][1][1] < bottomFolder+1:
        if keyIsPressed == False:
          sprites[arrowSprite][1][1] -= 2
        keyIsPressed = True
      elif keyboard.is_pressed("e"):
        if keyIsPressed == False:
          inComputer = False
          keyboard.send("enter")
        keyIsPressed = True
      else:
        keyIsPressed = False
    def update():
      global window, updateFrameTimer
      moveSelector()
      renderMinigameFrame(False,"computer")
    inComputer = True
    timer = 0
    renderGame("empty", False, 0)
    # Defualt window
    window = start
    filePath = [window]
    spriteLocation(window)
    renderMinigameFrame(False,"computer")
    while inComputer == True:
      if timer == 1:
        update()
        timer = 0
      timer += 1

def snakeGame():
  global sprites, inSnakeGame, direction, moveSnakeTimer, score, amountOfTailsAdded
  def resetSprites():
      global sprites
      sprites = {
               0 : ["wall_up",[0,0],[98,2]],
               1 : ["wall_down",[0,27],[98,2]],
               2 : ["wall_left",[1,2],[2,25]],
               3 : ["wall_right",[96,2],[2,25]],
               4 : ["food",[30,6],[1,1]],
               5 : ["snake_head_up",[20,10],[1,1]],
               }

  def tail():
      global score
      global sprites
      global amountOfTailsAdded
      for i in range(score-amountOfTailsAdded):
         sprites[i+6] = ["snake_tail",[-10,-10],[1,1]]
         amountOfTailsAdded += 1
      sprites1 = copy.deepcopy(sprites)
      for i in range((len(sprites1)-1), 5, -1):
         sprites[i][1] = sprites1[i-1][1]

  def playerMovement():
      global moveSnakeTimer
      global sprites
      global direction
      snake_head = 5
      if moveSnakeTimer >= 5:
        if direction == "up":
          sprites[snake_head][0] = "snake_head_up"
          sprites[snake_head][1][1] -= 1
          
        elif direction == "down":
          sprites[snake_head][0] = "snake_head_down"
          sprites[snake_head][1][1] += 1
          
        elif direction == "left":
          sprites[snake_head][0] = "snake_head_left"
          sprites[snake_head][1][0] -= 2
          
        elif direction == "right":
          sprites[snake_head][0] = "snake_head_right"
          sprites[snake_head][1][0] += 2
          
        tail()
        moveSnakeTimer = 0
      moveSnakeTimer += 1
      if keyboard.is_pressed("up") and direction not in ["down","up"]:
        direction = "up"
        
      elif keyboard.is_pressed("down") and direction not in ["down","up"]:
        direction = "down"
        
      elif keyboard.is_pressed("left") and direction not in ["right","left"]:
        direction = "left"
         
      elif keyboard.is_pressed("right") and direction not in ["right","left"]:
        direction = "right"
  def foodMove():
    global sprites, score
    food_x = random.randrange(2,95)
    food_y = random.randrange(2,24)
    sprites[4][1] = [food_x,food_y]
    score += 1
  def collition():
    global inSnakeGame
    snake_head = [5]
    walls = [0,1,2,3]
    tail = []
    food = [4]
    for i in range(len(sprites)-1):
      tail.append(i+5)
    if collide(snake_head,walls) == True:
      inSnakeGame = False
    if collide(snake_head,food) == True:
      foodMove()
  direction = "up"  
  resetSprites()
  amountOfTailsAdded = 0
  inSnakeGame = True
  moveSnakeTimer = 0
  snakeUpdateSpeed = 0
  score = 20
  while inSnakeGame:
    if snakeUpdateSpeed >= 100000:
      collition()
      playerMovement()
      renderMinigameFrame(False,"snake")
      snakeUpdateSpeed = 0
    snakeUpdateSpeed += 1

#Functions for gameplay=====================================================================================================================================


def giveItem(ItemID, scene,fishup):
  global sceneHasDone
  if not scene in sceneHasDone or fishup == True:
    sceneHasDone.append(scene)
    renderGame("addedItem", False, ItemID)
    time.sleep(1)
    for i in range(0, 4): # Checks if the inventory is full. If not put the item at a avaible slot.
      if items[i] == itemID[0][0]:
        items[i] = itemID[ItemID][0]
        full = False
        break
      if i == 3: # All slot are full
        full = True
    if full == True: # If inventory is full
      renderGame("replaceinv", False, 0)
      action = input().lower() #allow the player do discard the item or replace another item
      if action == "x":
        renderGameScreen()
      elif action == "1" or action == "2" or action == "3" or action == "4":
        items[int(action)-1] = itemID[ItemID][0]
    renderGameScreen()
def useItem(slot):
  global inventoryOpen
  global playerHealth
  for i in range(len(itemID)):
    if items[int(slot)-1] == itemID[i][0]:
      if itemID[i][1] == "healing":
        playerHealth += 4
        items[int(slot)-1] = itemID[0][0]
  

def initiateGame():
  global computerHasDone, spawnRock, jumping, gravity, jump_height, y_velocity, playerUpdateTimer, gameRunning, inventoryOpen, closeInventory, storyNumber
  global choice, choices, goTo, text, chrTraits, playerHealth, items, sceneHasDone, fightSceneHasDone, totalDmg, rockType, stoneDogeMinigameHasDone, fishingMinigameHasDone
  global whereLineHitsWater, fishingRodRenderDelay, updateFrame, ableToCatchFishTimer, grafY, quizHasDone, updateFrameTimer
  updateFrameTimer = 0
  computerHasDone = []
  quizHasDone = []
  grafY = 0
  ableToCatchFishTimer = 0
  updateFrame = 0
  fishingRodRenderDelay = 0
  whereLineHitsWater = 10
  rockType = 3
  spawnRock = True
  jumping = False
  gravity = 1
  jump_height = 5
  y_velocity = jump_height
  playerUpdateTimer = 0
  totalDmg = 0
  fightSceneHasDone = []
  sceneHasDone = []
  stoneDogeMinigameHasDone = []
  fishingMinigameHasDone = []
  gameRunning = False
  inventoryOpen = False
  closeInventory = False
  storyNumber = 1
  choice = 0
  choices = ["", "", "", ""]
  goTo = [0, 0, 0, 0]
  text = ""
  saveCode = ""
  chrTraits = {
    "Name": "",
    "Age": "",
    "Length": "",
    "Witdh": "",
    "IQ": "",
    "Primary hand": ""
  }

  playerHealth = 10
  items = [itemID[0][0], itemID[0][0], itemID[0][0], itemID[0][0]]

  print("\033c")
  startMenu()
  characterCreation()
  renderGame(0, False, 0)
  time.sleep(2)
  gameRunning = True


initiateGame()
while gameRunning == True: #The main code that runa everything else.
  renderGame(storyNumber, inventoryOpen, 0) # Renders the right scene and if the inventory is open
  action = input().lower() # A input so the player can choose action
  if action == "i": # If action is i open the inventory
    inventoryOpen = True
  elif action == "x": # if inventory is open, close inventory
    closeInventory = True
    inventoryOpen = False
  elif action == "e": # If player want to exit game exit game
    initiateGame()
  elif inventoryOpen == False:
    if action == "1" or action == "2" or action == "3" or action == "4": # Choose which choice.
      storyNumber = goTo[int(action) - 1]
  elif inventoryOpen == True:
    if action == "1" or action == "2" or action == "3" or action == "4": # Choose what item to use when inventory is open.
      useItem(action)
