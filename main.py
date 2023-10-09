import random
import math

lower = int(input("Enter lower bound:- "))

upper = int(input("Enter Upper bond:- "))

x = random.randint(lower,upper)

print("\n\t You've only ",
      round(math.log(upper - lower + 1,2)),
      " chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower +1,2):
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You Guessed too small!")
    elif x < guess:
        print("You Guesses too high!")


if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" % x)
    print("\t Better Luck next time!")