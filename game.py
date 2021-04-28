#using online tutorial and python website
import random 

user = int(input("Rock = 1, Paper = 2, Scissors = 3"))
computer = random.randint(1,3)

if user == computer:
    print("Its a draw!")
elif user == 1 and computer == 2 :
    print("You lost!")
elif user == 1 and computer == 3 :
    print("You won!")
elif user == 2 and computer == 1 :
    print("You won!")
elif user == 2 and computer == 3 :
    print("You lost!")
elif user == 3 and computer == 1 :
    print("You lost!")
elif user == 3 and computer == 2 :
    print("You won!")

#i tried to use random.choice so there would be no need for numbers but it bugged and i couldnt fix it on my own