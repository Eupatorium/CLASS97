import random
print("number guessing game")
number = random.randint(0,9)
chances = 0
print('guess a number between 1 and 9:')
while chances > 5:
    guess = int(input("guess your number "))
    if guess == number:
        print("congratulations you won")
        break
    elif guess < number:
        print("your guess was too low ,try a number greater than this" )
    else:
        print("your guess was too high ,try a number less than")
    chances =  chances + 1
if not chances < 5:
    print("YOU LOSE, The correct number is",number)