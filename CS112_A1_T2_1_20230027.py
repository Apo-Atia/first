# File: CS112_A1_T2_1_20230027.py
"""Purpose: It is a game between two players start from 0 and alternatively add
an integer number from 1 to 10 to the sum The player who reaches 100 and not exceeds it first wins."""
# Author: Ahmed Attia Abouzaid
# ID: 20230027

def display_status(current_sum):
    print("Current sum is:", current_sum)

current_sum = 0  #Initialize sum to add numbers to it
last_player = 2  # Initialize to 2, so that Player 1 can play first
print("Welcome to the 100 game")   #let's start the game
while True:
    display_status(current_sum)   #display the sum after every addition
#If the sum is 91 or above the numbers you can choose is limited 
    if current_sum >= 91:
        #I made list of the possible numbers the player can use from so sum value doesn't exceed 100
        num_list = [i for i in range(1, 11 - (current_sum % 10))]
        print("Available numbers to choose from:", num_list)

        while True:
            try:
                if last_player != 1:
                    player1 = int(input("Player 1, choose a number from the list: "))

                    if player1 not in num_list:
                        print("Invalid choice. Please select a number from the available list.")
                    else:
                        last_player = 1
                        break  # Break out of the loop if input is in the list              
            except ValueError:
                print("ERROR! Please enter a valid integer from the list.")

        if current_sum == 100:
            print("Player 1 wins!")
            break

    # Player 1 turn
    while True:
        try:
            if last_player != 1:
                player1 = int(input('Player 1, enter an integer number between 1 and 10: '))

                if 1 <= player1 <= 10 : #check the input validity
                    last_player = 1 #change the last player value so player2 can play
                    break  # Break out of the loop if a valid input is provided
                else:
                    print("ERROR! Please enter an integer between 1 and 10.")
            else:
                break
        except ValueError:
            print("ERROR! Please enter a valid integer.")

    current_sum += player1
    if current_sum == 100:#check the sum value and the winner
        print("Player 1 wins!")
        break

    display_status(current_sum)
    if current_sum >= 91:
        num_list = [i for i in range(1, 11 - (current_sum % 10))]
        print("Available numbers to choose from:", num_list)

        while True:
            try:
                if last_player != 2:
                    player2 = int(input("Player 2, choose a number from the list: "))

                    if player2 not in num_list:
                        print("Invalid choice. Please select a number from the available list.")
                    else:
                        last_player = 2
                        break                
                      # Break out of the loop if a valid input is provided

            except ValueError:
                print("ERROR! Please enter a valid integer from the list.")
    # Player 2 turn
    while True:
        try:
            if last_player != 2:
                player2 = int(input('Player 2, enter an integer number between 1 and 10: '))

                if 1 <= player2 <= 10 :
                    last_player = 2
                    break  # Break out of the loop if a valid input is provided
                else:
                    print("ERROR! Please enter an integer between 1 and 10.")
            else:
                break
        except ValueError:
            print("ERROR! Please enter a valid integer.")

    current_sum += player2
    if current_sum == 100:
        print("Player 2 wins!")
        break