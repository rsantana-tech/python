# Python Exercise 45: Create a program that makes the computer
# play Rock, Paper, Scissors with you.

import random

options = ['rock', 'paper', 'scissors']
pc_choice = random.choice(options)

player_choice = int(input("""
Choose your option:
[0] Rock
[1] Paper
[2] Scissors

Your choice: """))

if player_choice not in [0, 1, 2]:
    print("❌ Invalid choice. Please select 0, 1, or 2.")
else:
    player_choice_select = options[player_choice]

    if pc_choice == player_choice_select:
        result = 'Draw'
    elif (pc_choice == 'rock' and player_choice_select == 'scissors') \
        or (pc_choice == 'paper' and player_choice_select == 'rock') \
        or (pc_choice == 'scissors' and player_choice_select == 'paper'):
        result = 'You Lose 😢'
    else:
        result = 'You Win 🎉'

    print(f"""
💻 Computer chose: {pc_choice}
🧍 You chose: {player_choice_select}
🏁 Result: {result}
""")
