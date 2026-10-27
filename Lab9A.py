# Class: CSE 1321L
# Section: 16B
# Term: Fall 2026
# Instructor: Rubaina Roshan
# Name: Abiegail Raymond
# Lab: Lab 9A

print("[Mailing List]")

emails = []
while True:
    print()
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")

    selection = int(input("Make your selection: "))
    print()

    if selection == 1:
        email = input("\nEnter the email to be added: ")
        emails.append(email)
        print("\nEmail added to mailing list.")

    elif selection == 2:
        email = input("\nEnter the email to be removed: ")
        if email in emails:
            emails.remove(email)
            print(f"\n{email} has been removed from the mailing list.")
        else:
            print(f"No such email in mailing list: {email}")

    elif selection == 3:
        print()
        for email in emails:
            print(email)

    elif selection == 4:
        print("\nShutting down...")
        break
