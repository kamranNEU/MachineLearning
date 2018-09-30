import time
import matplotlib.pyplot as plt
mylist = []


def show1():
    x = step
    y = bullet
    plt.bar("Steps Taken",x, align= 'center', alpha = 0.5)
    plt.bar("Bullet Left",y,align= 'center', alpha = 0.5)
    plt.title('Terrorsit Strike:')
    plt.show()


# Store Steps///
def steps():
    global mylist
    print("****List of all the moves made in the game:**** \n")
    for i in range(len(mylist)):
        print(i + 1,".", mylist[i])


# Intoduction to game///
def gameintroduction():
    print("TERRORIST STRIKE: CONDITION ZERO BEGINS!!\n")
    time.sleep(1)
    print("TERRORIST STRIKE focuses on a battle between two teams; the terrorists and the Anti-terrorist Squad.\n")
    time.sleep(1)
    print("Player objective is to kill all the terrorists hiding in the building and safely escape all the hostages\n")
    time.sleep(1)
    print("Be very careful while opening fire as there are hostages that include small kids and ladies...\n")
    time.sleep(1)
    print("Also, the bullets are limited and you do not know how many terrorists are inside the building "
          "so be watchful and don't waste the bullets\n")
    time.sleep(1)
    print("Remember, you’re against the clock - so watch out for every step you make in the game!\n")
    time.sleep(1)
    print("Just follow the commands displayed on screen to move the player and perform action \n")
    time.sleep(1)

    startterroriststrike()


# Successful fire hit
def fire():
    global bullet
    if bullet > 0:
        print("Nice shot officer!! The bullet hit terrorist's forehead. He's dead.")
        global attackterrorist
        attackterrorist = attackterrorist - 1
        bullet = bullet - 1
        print("Bullets: " + str(bullet))
        print("Terrorists Remaining: " + str(attackterrorist))
    elif bullet == 0:
        nobullet()


# Unsuccessful hit
def misfire():
    global bullet
    if bullet > 0:
        print(" U missed the target. Take a new shot.")
        bullet = bullet - 1
        print("Bullets: " + str(bullet))
    elif bullet == 0:
        nobullet()


# Player run out of bullet\\\
def nobullet():
    print("You run out of bullets. You are dead. Please restart the game to continue.")
    startterroriststrike()

# Win Message\\\
def win():
    if attackterrorist == 0:
        print("Bravo!!!! You killed all the terrorists and safely rescued all the hostages.")
        print('''****YOU WON!!!''')
        print('''****GAME OVER.****''')
        print("\n")
        report()
        print("\n")
        print('''****OPTIONS***"
                    1. See the stats
                    2. Restart''')

        move = prompt()

        if move == "1":
            stats()
        elif move == "2":
            startterroriststrike()


# Stats to be displayed when player wins and selects to see stats
def stats():
    print("Bullets Remaining: " + str(bullet))
    print("Terrorists Remaining: " + str(attackterrorist))
    print("Total moves made: " + str(step))
    print("\n")
    steps()
    show1()
    f = open("../stepstaken.txt", "w+")
    f.write("\n".join(mylist))
    f.close()
    print("\n")
    print('''Thanks for playing the game.''')
    exit()


def prompt():
    allowed = set("12345")

    while True:
        message = input("Make your move: ")

        if message and allowed.issuperset(message):
            return message

        print("Invalid characters entered!")


def command():
    k = input("Type 'Fire' to kill the terrorist: ")
    return k


# Main menu
def startterroriststrike():

    global attackterrorist
    attackterrorist = 9
    global count
    count = 0
    global step
    step = 0
    global bullet
    bullet = 12
    global terrorist1
    terrorist1 = True
    global terrorist2
    terrorist2 = True
    global terrorist3
    terrorist3 = True
    global terrorist4
    terrorist4 = True
    global terrorist5
    terrorist5 = True
    global terrorist6
    terrorist6 = True
    global terrorist7
    terrorist7 = True
    global terrorist8
    terrorist8 = True
    global terrorist9
    terrorist9 = True

    print('''****OPTIONS***"
        1. Enter the main gate
        2. Exit''')

    move = prompt()
    if move == "1":
        entergame()

    elif move == "2":
        exitgame()

    else:
        startterroriststrike()


# Enter the game
def entergame():
    global step
    global count
    if count == 0:
        print("****************************************")
        print("Welcome to Terrorist Strike: Condition Zero")

    if count >= 0:
        print("Options:")
        print('''
           1. Pick the call from officer for further advice about the case
           2. Go to parking
           3. Take the lift
           4. Explore the building map
           5. Begin search on Ground floor''')

    count = count + 1
    step = step + 1

    move = prompt()
    if move == "1":
        mylist.append('Pick the call from officer for further advice about the case')
        pickcall()
    elif move == "2":
        mylist.append('Go to parking')
        parking()
    elif move == "3":
        mylist.append('Take the lift')
        lift()
    elif move == "4":
        mylist.append('Explore the building map')
        exploremap()
    elif move == "5":
        mylist.append('Begin search on Ground floor')
        groundfloor()
    else:
        print("Invalid characters entered!")
        entergame()


# Exit game
def exitgame():
    print("Thanks for playing the game!!! Hope to see you again.")
    exit()


# Pick officer call
def pickcall():
    global bullet
    global step
    print('''********
    Officer: "Information is that some terrorists are hiding on the first floor lift, Please begin your search there. 
       I REPEAT FIRST FLOOR-LIFT AREA. 
              Over and Out!!!."

    1. Directly go to lift as instructed on call
    2. Skip the instructions and go to rest room
    3. Wait for the terrorist to come out
    4. Enter the front gate
    5. Go back to entrance
    ''')

    step = step + 1

    move = prompt()
    if move == "1":
        mylist.append('Directly go to lift as instructed on call')
        lift()
    elif move == "2":
        mylist.append('Skip the instructions and go to rest room')
        restroom()

    elif move == "3":
        mylist.append('Wait for the terrorist to come out')
        wait()
    elif move == "4":
        mylist.append('Enter the front gate')
        frontdoor()
    elif move == "5":
        mylist.append('Enter the front gate')
        entergame()
    else:
        pickcall()


# Enter parking
def parking():
    global step
    global terrorist1
    print("***************PARKING ZONE*********************")
    print("****Be Careful****")
    print("Options:")
    print('''
          1. Approach and kill the terrorist and navigate to Ground floor
          2. Exit parking
          3. Go left and take the stairs up
          4. Go right and enter the door towards rest room
          5. Go back to entrance''')

    step = step + 1

    move = prompt()
    if move == "1" and terrorist1 is True:
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Approached and killed the terrorist and navigate to Ground floor')
            terrorist1 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            parking()
            return
        groundfloor()

    elif move == "1" and terrorist1 is False:
        dead()
        mylist.append('Exit parking')
        parking()

    elif move == "2":
        entergame()
    elif move == "3":
        mylist.append('Went left and took the stairs up')
        firstfloor()
    elif move == "4":
        mylist.append('Went right and entered the door towards rest room')
        restroom()
    elif move == "5":
        mylist.append('Went back to entrance')
        entergame()
    else:
        parking()


# Enter Parking
def lift():
    global step
    global terrorist2, terrorist3, terrorist4
    print("**************IN LIFT**********************")
    print("****GET READY WITH YOUR GUN****")
    print("Options:")
    print('''
              1. Kill the terrorist in the lift and come out
              2. Kill the terrorist in the lift and continue Left
              3. Kill the terrorist in the lift and continue Right
              4. Go back to entrance
              5. Run away''')

    step = step + 1

    move = prompt()
    if move == "1"and terrorist2 is True:
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist in the lift and came out')
            terrorist2 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            lift()
            return
        parking()

    elif move == "1" and terrorist2 is False:
        dead()
        lift()

    elif move == "2" and terrorist3 is True:
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist in the lift and continued Left')
            terrorist3 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            lift()
            return
        restroom()

    elif move == "2" and terrorist3 is False:
        dead()
        lift()

    elif move == "3" and terrorist4 is True:
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist in the lift and continued right')
            terrorist4 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            lift()
            return
        groundfloor()

    elif move == "3" and terrorist4 is False:
        dead()
        lift()

    elif move == "4":
        mylist.append('Go back to entrance')
        entergame()
    else:
        mylist.append('Ran away')
        exitgame()


# Map explore
def exploremap():
    global step
    print("**************EXPLORE MAP**********************")
    print("Options:")
    print('''
            1. Continue to fight terrorists
            2. Exit the game''')

    step = step + 1
    move = prompt()
    if move == "1":
        mylist.append('Continued to fight terrorists')
        entergame()
    elif move == "2":
        mylist.append('Exit the game')
        exitgame()
    else:
        exploremap()

# Navigate to Ground floor
def groundfloor():
    global step
    global terrorist5
    print("**************SEARCH GROUND FLOOR**********************")
    print("****GET READY WITH YOUR GUN****")
    print("Options:")
    print('''
                1. Approach and kill the terrorist and move to First floor
                2. Continue towards first floor
                3. Run away
                4. Navigate towards parking
                5. Go back to entrance''')

    step = step + 1
    move = prompt()
    if move == "1" and terrorist5 is True:
        global attackterrorist
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Approached and killed the terrorist and moved to First floor')
            terrorist5 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            groundfloor()
            return
        firstfloor()

    elif move == "1" and terrorist5 is False:
        dead()
        groundfloor()

    elif move == "2":
        mylist.append('Continued towards first floor')
        firstfloor()
    elif move == "3":
        mylist.append('Ran away')
        exitgame()
    elif move == "4":
        mylist.append('Navigated towards parking')
        parking()
    elif move == "5":
        mylist.append('Went back to entrance')
        entergame()
    else:
        groundfloor()


# Navigate to First floor
def firstfloor():
    global count
    global step
    global terrorist6
    print("**************SEARCH FIRST FLOOR**********************")
    print("****GET READY WITH YOUR GUN****")
    print("Options:")
    print('''
            1. Approach and kill the terrorist
            2. Go to ground floor
            3. Go to Parking
            4. Go back to entrance''')

    step = step + 1

    move = prompt()
    if move == "1" and terrorist6 is True:
        global attackterrorist
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Approached and killed the terrorist')
            terrorist6 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            firstfloor()
            return
        lift()

    elif move == "1" and terrorist6 is False:
        dead()
        firstfloor()

    elif move == "2":
        mylist.append('Went to ground floor')
        groundfloor()
    elif move == "3":
        mylist.append('Went to Parking')
        parking()
    elif move == "4":
        mylist.append('Went back to entrance')
        entergame()
    else:
        firstfloor()


def wait():
    global step
    print("**************Wait for any further instructions**********************")

    step = step + 1
    pickcall()


# Navigate to Front door
def frontdoor():
    global step
    global terrorist7, terrorist8
    print("**************ENTER FRONT DOOR**********************")
    print("****GET READY WITH YOUR GUN****")
    print("Options:")
    print('''
            1. Kill the terrorist and navigate towards Parking
            2. Kill the terrorist and navigate towards rest room
            3. Go to first floor
            4. Go to lift
            5. Go back to entrance''')

    step = step + 1

    move = prompt()
    if move == "1" and terrorist7 is True:
        global attackterrorist
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist and navigated towards Parking')
            terrorist7 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            frontdoor()
            return
        parking()

    elif move == "1" and terrorist7 is False:
        dead()
        frontdoor()

    elif move == "2" and terrorist8 is True:
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist and navigated towards rest room')
            terrorist8 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        restroom()

    elif move == "2" and terrorist8 is False:
        dead()
        frontdoor()

    elif move == "3":
        mylist.append('Went to first floor')
        firstfloor()
    elif move == "4":
        mylist.append('Went to lift')
        lift()
    elif move == "5":
        mylist.append('Went back to entrance')
        entergame()
    else:
        frontdoor()


# Navigate to restroom
def restroom():
    global step
    global terrorist9
    print("**************IN RESTROOM**********************")
    print("Options:")
    print('''
                1. Use services
                2. Kill the terrorist and continue hunt on ground floor
                3. Go to first floor
                4. Go to lift
                5. Go back to entrance''')

    step = step + 1

    move = prompt()
    if move == "1":
        print("Be alert while using the restroom services, the terrorists can be anywhere and might attack from back")
        mylist.append('Used restroom services')
        restroom()
    elif move == "2" and terrorist9 is True:
        global attackterrorist
        hit = command()
        if hit == "Fire" and bullet > 0:
            fire()
            mylist.append('Killed the terrorist and continued hunt on ground floor')
            terrorist9 = False
            win()
        elif bullet == 0:
            nobullet()
            return
        elif hit != "Fire" and bullet > 0:
            misfire()
            restroom()
            return
        groundfloor()

    elif move == "2" and terrorist9 is False:
        dead()
        restroom()

    elif move == "3":
        mylist.append('Went to first floor')
        firstfloor()
    elif move == "4":
        mylist.append('Went to lift')
        lift()
    elif move == "5":
        mylist.append('Went back to entrance')
        entergame()
    else:
        restroom()


# Enter report
def report():
    print('''As a commanding officer of ATS who lead his team to glory, you are required to fill and submit below report
    based on the concluded operation to US Department of State\n''')
    print('''****Counter Terrorist Operation Report****\n''')
    name = input("Name of the Commanding Officer: \n")
    print("Well done!", name, ", country is proud to have officers like you.\n")
    age = input("Age of the Commanding Officer: \n")
    print("At the age of just", str(age), "you lead such a major operation. Bravo lad!\n")
    terroristkilled = input("How many total terrorists you killed in the operation: \n")
    terroristkilled = int(terroristkilled)
    print("Total terrorists killed in last 15 operations", terroristkilled + 100, "\n")
    submit = input("That's it. We are done. Press '1' to submit the report \n")
    while submit != "1":
        input("Invalid choice. Please enter '1' to submit the report \n")
        if submit == "1":
            break
    print("Submitting...")
    time.sleep(3)
    print("Submitted. Thanks for playing the game.")
    return


# If a terrorist is already dead
def dead():
    print("\n")
    print("You already killed this terrorist. Please move on and select another move. ")
    print("\n")


gameintroduction()