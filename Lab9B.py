# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Lab: Lab 9B

print("[Friend List]")

friends = []

while True:
    print()
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")

    selection = int(input("Make your selection: "))

    if selection == 1:
        name = input("\nEnter your friend's name: ")
        age = input("Enter your friend's age: ")

        friend = (name, age)
        friends.append(friend)
        print("Friend added")

    elif selection == 2:
        print()
        for friend in friends:
            print(f"Name: {friend[0]}, Age: {friend[1]}")

    elif selection == 3:
        print("\nShutting down...")
        break