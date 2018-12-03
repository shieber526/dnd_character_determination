#Get more money roll checks. 
import random

def main():
    print("Hello adventurer...")
    print("Welcome to the world of Dungeons and Dragons..")
    print(" ")
    
    your_character = "y"
    
    while your_character == "y" or your_character == "Y":
        input("Let us see what fate has in store for you...")
        print(" ")
        your_race()
        print(" ")
        input("Now we know what you are...we need your class...")
        input("What has fate chosen for you now?")
        your_class()
        print(" ")
        input("Excellent new traveler!!")
        print("Now we need your skill numbers")
        input("Here's your first number: ")
        ability_scores()
        print(" ")
        input("Here's your second number: ")
        ability_scores()
        print(" ")
        input("Here's your third number: ")
        ability_scores()
        print(" ")
        input("Here's your fourth number: ")
        ability_scores()
        print(" ")
        input("Here's your fifth number: ")
        ability_scores()
        print(" ")
        input("Here's your sixth and final number: ")
        ability_scores()
        print(" ")
        your_character = input("Don't like it? Want to try again? ")
def your_race():
    race = random.randint(1,12)
    if race == 1:
        print("Congratulations! You are now a Dragonborn!")
    elif race == 2:
        print("Congratulations! You are now a Dwarf!")
    elif race == 3:
        print("Congratulations! You are now an Elf!")
    elif race == 4:
        print("Congratulations! You are now a Gnome!")
    elif race == 5:
        print("Congratulations! You are now a Half-Elf!")
    elif race == 6:
        print("Congratulations! You are now a Half-Orc!")
    elif race == 7:
        print("Congratulations! You are now a Halfling!")
    elif race == 8:
        print("Congratulations! You are now a Human!")
    else:
        print("Congratulations! You are now a Tiefling!")
def your_class():
    your_class = random.randint(1,12)
    if your_class == 1:
        print("Your class is Wizard.")
        money = wealth_generation(4, 4) * 10
        print("You have", money, "pieces.")        
    elif your_class == 2:
        print("Your class is Warlock.")
        money = wealth_generation(4, 4) * 10
        print("You have", money, "pieces.")        
    elif your_class == 3:
        print("Your class is Sorcerer")
        money = wealth_generation(4, 3) * 10
        print("You have", money, "pieces.")        
    elif your_class == 4:
        print("Your class is Rouge")
        money = wealth_generation(4, 4) * 10
        print("You have", money, "pieces.")        
    elif your_class == 5:
        print("Your class is Ranger")
        money = wealth_generation(4, 4) * 10
        print("You have", money, "pieces.")        
    elif your_class == 6:
        print("Your class is Paladin")
        money = wealth_generation(4, 5) * 10
        print("You have", money, "pieces.")        
    elif your_class == 7:
        print("Your class is Monk")
        money = wealth_generation(4, 5) * 10
        print("You have", money, "pieces.")        
    elif your_class == 8:
        print("Your class is Fighter")
        money = wealth_generation(4, 4) * 10
        print("You have", money, "pieces.")        
    elif your_class == 9:
        print("Your class is Druid")
        money = wealth_generation(4, 2) * 10
        print("You have", money, "pieces.")        
    elif your_class == 10:
        print("Your class is Cleric")
        money = wealth_generation(4, 5) * 10
        print("You have", money, "pieces.")        
    elif your_class == 11:
        print("Your class is Bard")
        money = wealth_generation(4, 5) * 10
        print("You have", money, "pieces.")        
    else:
        print("Your class is Barbarian!")
        money = wealth_generation(2, 4) * 10
        print("You have", money, "pieces.")        
def ability_scores():
    scores = random.randint(1,20)
    print(scores)
def wealth_generation(x, y):
    total = 0
    for i in range(y):
        #x is the dice
        #y is the number of dice
        total += random.randint(1, x)
    return total    
main()
    