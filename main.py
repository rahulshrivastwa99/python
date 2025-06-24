# import random

# def get_choices():
#     player_choice = input("Enter a choice (Bat, Ball, Wicket): ")
#     options = ["Bat", "Ball", "Wicket"]
#     if player_choice not in options:
#         print("Invalid choice!")
#         return None
#     computer_choice = random.choice(options)
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices

# def check_win(player, computer):
#     print(f"\nYou chose {player}, computer chose {computer}")
#     if player == computer:
#         return "It's a tie!"
#     elif (player == "Bat" and computer == "Ball") or \
#          (player == "Ball" and computer == "Wicket") or \
#          (player == "Wicket" and computer == "Bat"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# # Main flow
# choices = get_choices()
# if choices:
#     result = check_win(choices["player"], choices["computer"])
#     print(result)
# Python program to print the multiplication table of 5

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
