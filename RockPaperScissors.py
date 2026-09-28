import random

while True:
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    computerChoice = random.randint(1, 3)

    if choice == "1":
        print("You chose Rock.")
    elif choice == "2":
        print("You chose Paper.")
    elif choice == "3":
        print("You chose Scissors.")
    elif choice == "4":
        print("Exiting the game.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    if choice == computerChoice:
        print("It's a tie!")
    elif(choice == "1" and computerChoice == 3):
        print("You win! Rock beats Scissors.")
    elif(choice == "2" and computerChoice == 1):
        print("You win! Paper beats Rock.")
    elif(choice == "3" and computerChoice == 2):
        print("You win! Scissors beats Paper.")
    else:
        print("You lose! Better luck next time.")