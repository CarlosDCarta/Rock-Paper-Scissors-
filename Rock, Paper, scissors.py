import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

selected1 = choices[user_choice]
print(selected1)

computer_choice = random.randint(0,2)
selected2 = choices[computer_choice]
print(f"Computer choose: {selected2}")

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose")
else:
    print("You Lose")
