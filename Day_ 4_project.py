rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print('Welcome to the Rock, Paper, Scissors game!')
# Lets get input from the user
user_input = int(input('To make a choice, Type 0 for Rock, 1 for Paper, 2 for Scissors: \n'))

# Let's get input from the computer
computer_input = random.randint(0,2)

# printing the user input
if user_input == 0:
  print(rock)

elif user_input == 1:
  print(paper)

elif user_input == 2:
  print(scissors)

else:
  print('input invalid')

# printing the computer input
if computer_input == 0:
  print('Computer choose', computer_input)
  print(rock)

elif computer_input == 1:
  print('Computer choose', computer_input)
  print(paper)

elif computer_input == 2:
  print('Computer choose', computer_input)
  print(scissors)

else:
  print('input invalid')

# checking for the winner
if user_input == 0 and computer_input == 2:
  print('You have won')

elif user_input == 1 and computer_input == 0:
  print('You have won')

elif user_input == 2 and computer_input == 1:
  print('You have won')

elif user_input == computer_input:
  print('It is a draw')

else:
  print('You lost the game')
