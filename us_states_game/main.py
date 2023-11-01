
import turtle
import pandas

# Setup screen
screen = turtle.Screen()
screen.title("U.S States Games")
image = r"C:\Users\Matt\repos\miniprojects\us_states_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Setup states list
data = pandas.read_csv(r"C:\Users\Matt\repos\miniprojects\us_states_game\50_states.csv")
state_list = []
state_column = data.state
for state in state_column:
    state_list.append(state)

correctly_guessed_states = []
score = 0

game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Guess a state")
    answer_state = answer_state.title()
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_data = data[data.state == answer_state]
        t.goto(int(row_data.), int(row_data.y))



        score += 1
        correctly_guessed_states.append(answer_state)
        # state_list.remove(answer_state)
    else:
        game_on = False

print(len(state_list))
print(len(correctly_guessed_states))






screen.exitonclick()