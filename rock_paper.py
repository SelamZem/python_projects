import random

def play():
    user_choice = input("what is your choice? 'r' for rock, 'p' for paper and 's' for scissor: " ).lower()
    computer = random.choice(['r', 'p', 's'])

    if(computer==user_choice):
        play()

    if winner(computer , user_choice):
        print(f'Hurray, You won!')
    else: 
        print('You Lose!Try again')
        return


def winner(comp, user):
    if (comp=='p'and user=='s') or (comp=='r' and user=='p') or (comp=='s' and user=='r'):
        return 1
    
play()