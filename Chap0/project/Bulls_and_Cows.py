#! python3
import random
# from sys import exit

print("Wellcome to Bulls and Cows!")
print("You have 10 chance to guess the number from 1 to 20.")
print("Now let's go!\n")

number = random.randint(1,20)

print("Please type in your number and press Enter.")

for i in range(0,10):
    answer_str = input("> ")
    if answer_str.isdecimal():
        answer_int = int(answer_str)
        if number == answer_int:
            print("Yes. You win!")
            # exit(0)
            break
        elif number > answer_int:
            print("Sorry, the number is greater than your answer. ")
            print(f"You have {9-i} chance left.")
        elif number < answer_int:
            print("Sorry, the number is less than your answer. ")
            print(f"You have {9-i} chance left.")
        else:
            print("Sorry, the program is broken.")
            print(f"You have {9-i} chance left.")
            continue
    else:
        print("Please type in a number!")
        print(f"You have {9-i} chance left.")
