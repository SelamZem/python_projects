import random

def guess():
    lowest = int(input('Enter the lowest number: '))
    highest = int(input('Enter the highest number:  '))
    user_response = -1000
    
    while user_response!=0:
        random_number= random.randint(lowest , highest)
        print(random_number)
        print('1.Too High / 2. Too low/ 0. matched')
        user_response= int(input('Enter your response: '))
        if user_response == 1:
            highest = random_number - 1
        elif user_response == 2:
            lowest = random_number + 1
    
    print('yay, You got it')

guess()

    
