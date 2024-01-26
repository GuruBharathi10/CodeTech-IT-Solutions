import time

def introduction():
    print("Welcome to the Adventure Story!")
    time.sleep(1)
    print("You find yourself at a crossroads. A mysterious path lies ahead.")
    time.sleep(1)

def make_choice(options):
    while True:
        print("\nChoose your next move:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def story_branch_1():
    print("\nYou decide to take the left path.")
    time.sleep(1)
    print("As you walk, you encounter a friendly creature.")
    time.sleep(1)
    print("It offers to guide you through the enchanted forest.")
    time.sleep(1)

def story_branch_2():
    print("\nYou choose the right path.")
    time.sleep(1)
    print("The path leads you to a dark cave.")
    time.sleep(1)
    print("You can hear strange noises echoing from inside.")
    time.sleep(1)

def story_branch_3():
    print("\nYou decide to go straight ahead.")
    time.sleep(1)
    print("You find yourself on a bridge over a rushing river.")
    time.sleep(1)
    print("There's a mysterious door on the other side.")

def main():
    introduction()

    # Player makes the first choice
    choice_1 = make_choice(["Take the left path", "Take the right path", "Go straight ahead"])

    if choice_1 == 1:
        story_branch_1()
        # Player makes a choice within this branch
        choice_2 = make_choice(["Follow the creature", "Politely decline and continue alone"])
        if choice_2 == 1:
            print("\nThe creature leads you safely through the forest. You reach your destination.")
        else:
            print("\nYou continue your journey alone and face various challenges.")
    elif choice_1 == 2:
        story_branch_2()
        # Player makes a choice within this branch
        choice_3 = make_choice(["Enter the cave", "Look for another path"])
        if choice_3 == 1:
            print("\nYou enter the cave and discover hidden treasures!")
        else:
            print("\nYou decide not to enter the cave and explore other paths.")
    else:
        story_branch_3()
        # Player makes a choice within this branch
        choice_4 = make_choice(["Cross the bridge", "Explore the surroundings"])
        if choice_4 == 1:
            print("\nYou cross the bridge and find a magical realm on the other side.")
        else:
            print("\nYou explore the surroundings, finding interesting sights.")

if __name__ == "__main__":
    main()
