#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
combined=[rock,paper,scissors]
user_choose=int(input("What do you want to choose ? type 0 for rock,1 for paper , 2 for scissors : "))
x=combined[user_choose]
print(f"You choose {x}")
computer_choice=random.randint(0,2)
y=combined[computer_choice]
print(f"Computer choice {y}")
if user_choose==computer_choice:
    print("Draw")
elif user_choose==0 and computer_choice==2:
    print("You win")
elif user_choose==2 and computer_choice==0:
    print("Computer wins")
elif user_choose>computer_choice:
    print("You win")
elif computer_choice>user_choose:
    print("You loose")
else:
    print("Oops you choose wrong number")

    




