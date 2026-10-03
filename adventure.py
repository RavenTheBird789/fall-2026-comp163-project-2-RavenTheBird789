# Name: Raven Jones
# Date: Oct 2, 2026
# Course: COMP 163
# Project 2: Text Adventure Game

health = 10
print("Health: 10")

first = input("Two tunnels are in the cave ahead. Which way will you go? (left or right): ")

if first == "left":
    health = health - 2
    print("A jagged rock scratches you as you enter the left tunnel.")
    print("Health:", health)
    second = input("A goblin guards a chest. Type fight or sneak: ")

    if second == "fight":
        health = health - 3
        print("You win the brawl, but you are bruised.")
        print("Health:", health)
        third = input("The chest is open. Type take or leave: ")

        if third == "take":
            health = health + 4
            print("You drink a healing potion from the chest.")
            print("Health:", health)
            if health > 5 and health <= 10:
                print("You walk out of the cave with the treasure.")
                print("=== YOU WIN ===")
        elif third == "leave":
            health = health - 5
            print("A collapsing tunnel catches you on the way out.")
            print("Health:", health)
            print("=== GAME OVER ===")
        else:
            print("Invalid choice.")

    elif second == "sneak":
        health = health - 8
        print("You step on a hidden trap.")
        print("Health:", health)
        print("=== GAME OVER ===")
    else:
        print("Invalid choice.")

elif first == "right":
    health = health - 4
    print("Spiders drop on you in the right tunnel.")
    print("Health:", health)
    second = input("Something is chasing you. Type run or hide: ")

    if second == "run":
        health = health - 3
        print("You sprint and trip over a root.")
        print("Health:", health)
        third = input("You reach a ledge. Type leave or climb: ")

        if third == "leave":
            health = health - 3
            print("You turn back and the beast catches you.")
            print("Health:", health)
            print("=== GAME OVER ===")
        elif third == "climb":
            health = health + 2
            print("You scramble up and find a hidden exit.")
            print("Health:", health)
            print("=== YOU WIN ===")
        else:
            print("Invalid choice.")

    elif second == "hide":
        health = health + 1
        print("You rest quietly until the danger passes.")
        print("Health:", health)
        print("=== YOU WIN ===")
    else:
        print("Invalid choice.")

else:
    print("Invalid choice.")