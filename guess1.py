import random

def guess(x):
    random_number=random.randint(1, x)
    ran_number = -1000
    while ran_number != random_number:
        ran_number = int(input(f'Guess a number between 1 and x :  ' ))
        if ran_number<random_number:
            print('Sorry, guess again.Too low.')
        elif ran_number > random_number:
            print('Sorry, You guessed to high!')
    else: 
        print(f'congrats! You have guessed the number {random_number}')
guess(10)