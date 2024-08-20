import random

def compare(x,y):
    if x>y:
        print("too high\n\n")
    elif x<y:
        print("too low\n\n")
    else :
        print("you win😍\n\n")
        return True
    return False

def set_difficulty(l,a,e):
    if l == 'easy':
        a = 10
        e = ['😭', '😢', '☹️', '🙁', '😕', '😐', '🙂', '😊', '😃', '😁']

    elif l == 'hard':
        a = 5
        e =  ['😭', '😢', '🙁', '🙂', '😁']
    return l,a,e

def game():
    number= random.randint(1,100)
    level = input("Lets play number guessing game, type 'easy'👍 or 'hard'👾: ")
    attempts = 0
    emojis = []
    level,attempts,emojis = set_difficulty(level,attempts,emojis)
    for i in range(attempts,0,-1):
        print(f"you have {i},{emojis[i-1]} attempts left!")
        guess = int(input("guess the number :"))
        if compare(guess, number):
            break
        elif i==1:
            print("You lose🧟‍♂️")

# GAME STARTS HERE
game()


