import random
import game_data
import art

def display_names(n1,n2):
    print(f"A. {game_data.data[n1]['name']},who is a {game_data.data[n1]['description']}, from {game_data.data[n1]['country']}")
    print(art.vs)
    print(f"B. {game_data.data[n2]['name']},who is a {game_data.data[n2]['description']}, from {game_data.data[n2]['country']}")

def compare(n1, n2, p):
    count1 = game_data.data[n1]['follower_count']
    count2 = game_data.data[n2]['follower_count']
    if p == 'A' and count1 > count2 :
        print("RIGHT")
        return True,n1
    elif p == 'B' and count1 < count2:
        print("RIGHT")
        return True,n2
    else:
        print("WRONG")
        return False,0


def higher_or_lower():
    print(art.logo)
    score=0
    num1, num2 = 0, 0
    while num1 == num2:
        num1 = random.randint(0, len(game_data.data)-1)
        num2 = random.randint(0, len(game_data.data)-1)

    # choose random 2 names
    flag = True
    while flag:
            display_names(num1, num2)
            play = input("Who has more followers? Type 'A' or 'B': ").upper()
            print("\n"*20)
            # check if true or false
            flag,winning_number = compare(num1,num2, play)
            num1 = winning_number
            num2 = random.randint(0, len(game_data.data))
            while num1 == num2:
                num2 = random.randint(0, len(game_data.data))
            score += 1
            print(f"Your sore is: {score}")

higher_or_lower()