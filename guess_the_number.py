import random
def compare(x,y):
    if x>y:
        print("too high\n")
    elif x<y:
        print("too low\n")
    else :
        print("you win😍\n")
        return True
    return False

number= random.randint(1,100)
level = input("Lets play number guessing game, type 'easy'👍 or 'hard'👾: ")
attempts = 0
emojis = []
if level == 'easy':
    attempts = 10
    emojis = ['😭', '😢', '☹️', '🙁', '😕', '😐', '🙂', '😊', '😃', '😁']

elif level == 'hard':
    attempts = 5
    emojis =  ['😭', '😢', '🙁', '🙂', '😁']
for i in range(attempts,0,-1):
    print(f"you have {i},{emojis[i-1]} attempts left!")
    guess = int(input("guess the number :"))
    if compare(guess, number):
        break
    elif i==1:
        print("You lose🧟‍♂️")



