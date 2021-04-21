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
import random
choice = input('Please make your choice: Rock = 0, Paper = 1, Scissors = 2. Your choice:\n')

choice_int = int(choice)


if choice == '0':
  print(rock)
elif choice == '1':
  print(paper)
elif choice == '2':
  print(scissors)
else:
  print('Something goes wrong.')

choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)
if choice_int >= 3:
  print('Not a valid choice.')
else:
  print(computer_choice)

if choice_int >= 3:
  print('Please try again.')
elif choice == '1' and computer_choice == choice_list[0]:
  print('Paper wins against rock. You win!')
elif choice == '0' and computer_choice == choice_list[2]:
  print('Rock wins against scissors. You win!')
elif choice == '2' and computer_choice == choice_list[1]:
  print('Scissors win against paper. You win!')
elif choice == '0' and computer_choice == choice_list[0]:
  print("It's drawn. Try again.")
elif choice == '1' and computer_choice == choice_list[1]:
  print("It's drawn. Try again.")
elif choice == '2' and computer_choice == choice_list[2]:
  print("It's drawn. Try again.")
else:
  print('Computer wins!')

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.