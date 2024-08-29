from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
screen.title("US states Guessing game")

correct_guess = 0

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

flag = len(guessed_state)
while flag < 50:
    #use title case , since python is case-sensitive
    guess = screen.textinput(f"{correct_guess}/50 Guess the state", "What is the next state?").title()
    #code to exit(exit no , Exit yes bcz guess is in title case)
    if guess == 'Exit':
        #using list comprehension(to avoid for loop)
        to_learn_list = [n for n in states if n not in guessed_state]
        data = pandas.DataFrame(to_learn_list)
        data.to_csv('learn')
        break
    if guess in states:
        guessed_state.append(guess)
        correct_guess += 1
        mark_position = Turtle()
        mark_position.hideturtle()
        mark_position.penup()
        # picking up a  column(series)even if only 1 item in the column(series), it has a index associated with it)
        # so use  item()
        guess_x = data[data.state == guess]['x'].item()
        guess_y = data[data['state'] == guess]['y'].item()
        mark_position.goto(guess_x, guess_y)
        mark_position.write(f"{guess}")

        # Victory message
        if flag == 49:
            print("YOU WIN👾")

# making a csv file for knowing missing states


