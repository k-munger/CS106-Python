# User Guardian, the security program will ask you if you would like to be added to the list
# Contains the ability to add and remove new and old users
# List of known users
known_users = ["Doug", "Joseph", "Benjamin", "Mike", "Peter", "Ronald", "Greg", "Harold", "Karissa"]


while True:
    print()
    print("Hi there! I'm the User Guardian.")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Name recognised. Hello there, {}!".format(name))
# If the system recognises the name, user can choose to remove name from the known_users list
# List will update if user is removed from known_users
        remove = input("Would you like to be removed from the system? (y/n)?: ").lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
            print(known_users)
            known_users.remove(name)
            print()
            print("Here is the updated list"
            print()
            print(known_users)
            
    else:
        print("We haven't met yet, pleasure to meet you {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
             known_users.append(name)
        elif add_me == "n":
            print("Right on! See you around.")
        print("Type 'End' to stop the program")

# 'End' will stop the program
