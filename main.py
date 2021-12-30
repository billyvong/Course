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
import sys

#User picks choice while computer randomly picks choice
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
comp_choice = int(random.randint(0,2))

#Graphics for choices
print("You chose:\n")
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  sys.exit("You did not choose a valid option")

print("Computer chose:\n")
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
else:
  print(scissors)

#Comparing choices to determine winner
if choice == comp_choice:
    print("Draw")
elif choice == 0:
  if comp_choice == 1:
    print("Paper beats rock. You lose")
  if comp_choice == 2:
    print("Rock beats scissors. You win")
elif choice == 1:
  if comp_choice == 0:
    print("Paper beats rock. You win")
  if comp_choice == 2:
    print("Scissors beats paper. You lose")
elif choice == 2:
  if comp_choice == 0:
    print("Rock beats scissors. You lose")
  if comp_choice == 1:
    print("Scissors beats paper. You win")