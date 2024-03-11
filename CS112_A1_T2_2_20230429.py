
# File: CS112_A1_T2_2_20230429
# Purpose:
#    Number scrabble is played with the list of numbers between 1 and 9. Each player takes
#    turns picking a number from the list. Once a number has been picked, it cannot be picked
#    again. If a player has picked three numbers that add up to 15, that player wins the game.
#    However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# Author: Mohanad Mohamed Fawzy Mohamed
# ID: 20230429

# Function to check if 3 numbers in the list sum to 15
def check_sum_of_three(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 15:
                    return True
    return False
# Defining & Setting Values For The Game
player1_nums = []
player2_nums = []


numbers = list(range(1, 10))
player_turn = 1
turns = 0
# Explain Game Rules
print("Number scrabble is played with the list of numbers between 1 and 9. Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
while True:
        turns = turns + 1
        # Ensuring The Play Is Valid
        if not numbers:
            print("It's a draw!")
            break
        # Displaying Game Status 
        print("Available numbers:", numbers)
        # Show Each Player's Sum
        if player_turn == 1:
         print(f"Player {player_turn} Numbers : {player1_nums}")
        elif player_turn == 2:
         print(f"Player {player_turn} Numbers : {player2_nums}")
        # Player's Turn To Play
        try:
         selected_number = int(input(f"Player {player_turn}, select a number: "))
          # Ensuring The Play Is Valid
         if selected_number not in numbers:
            print("Enter a valid number.")
            continue
        # Updating Game Status
         numbers.remove(selected_number)
        # First Player Wins
         if player_turn == 1:
          player1_nums.append(selected_number)
          if check_sum_of_three(player1_nums) and turns >= 5:
             print("Player 1 wins")
             break
        # Second Player Wins
         elif player_turn == 2:
          player2_nums.append(selected_number)
          if check_sum_of_three(player2_nums) and turns >= 5:
             print("Player 2 wins")
             break       
        #  Updating The Variables For The Loop
         player_turn = 3 - player_turn
        except ValueError:
         print("That's not a number😡!")
# Enjoy :)
        