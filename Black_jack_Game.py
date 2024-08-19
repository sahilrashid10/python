import random

def cal_score(c):
    if sum(c) > 21 and 11 in c:
        c.remove(11)
        c.append(1)
    return sum(c)

def black_jack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_cards = [random.choice(cards),random.choice(cards)]
    computer_cards = [random.choice(cards),random.choice(cards)]

    player_score = cal_score(player_cards)
    computer_score = cal_score(computer_cards)

    if computer_score == 21 and player_score != 21:
        print("You Lose, computer hits Black Jack 😶‍🌫️\n")
        return
    if player_score == 21  :
        print("You hit Black Jack , you win 😍\n")
        return
    print(f" your cards: {player_cards}, score {player_score}")
    print(f" computer cards: {computer_cards[0]} ")

    flag1 = True
    while flag1:
        play = input("Enter y to draw, n to stand \n")
        if play == 'y':
            player_cards.append(random.choice(cards))
            player_score = cal_score(player_cards)
            print(f" your cards: {player_cards}, score {player_score}")
            print(f" computer cards: {computer_cards[0]} \n")
            if player_score == 21:
                print("You Win 😊\n")
                return
            if player_score > 21:
                print("You Lose 😶‍🌫️\n")
                return
        elif play == 'n':
            while computer_score < 17:
                computer_cards.append(random.choice(cards))
                computer_score = cal_score(computer_cards)
            if computer_score >17 and computer_score < player_score:
                print("You Win 😊\n")
                flag1 = False

            print(f" your cards: {player_cards}, score: {player_score}")
            print(f" computer cards: {computer_cards}, score: {computer_score}\n")

            if computer_score > 21:
                print("You Win 😊\n")
            elif computer_score > player_score:
                print("You Lose 😶‍🌫️\n")
            elif computer_score < player_score:
                print("You Win 😊\n")
            elif computer_score == player_score:
                print("Draw 😗 \n")
            flag1 = False

        else:
            print("Invalid input\n")


flag = 'y'
while flag !='n':
    flag = input("\nDo you want to play a game of Black Jack? y or n 👾\n")
    if flag == 'y':
        black_jack()
    if flag == 'n':
        print("\nThanks for visiting ❤️") 
