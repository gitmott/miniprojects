
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


while len(correctly_guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(correctly_guessed_states)}/50 States guessed", prompt="Guess a state").title()
    
    if answer_state.title() == "Exit":
        missing_states = []
        for state in state_list:
            if state not in correctly_guessed_states:
                missing_states.append(state)
        missed_states_data = pandas.DataFrame(missing_states)
        missed_states_data.to_csv("states_to_practise.csv")
        break
        
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_data = data[data.state == answer_state]
        t.goto(int(row_data.x.iloc[0]),int(row_data.y.iloc[0]))
        t.write(row_data.state.item())
        score += 1
        correctly_guessed_states.append(answer_state)
        # state_list.remove(answer_state)

print(len(state_list))
print(len(correctly_guessed_states))

screen.exitonclick()