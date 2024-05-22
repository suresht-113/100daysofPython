import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
turtle.shape(image)
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt= "Whats another state's name").capitalize()

    if answer_state == "Exit":

        # not_answered = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         not_answered.append(state)
        not_answered = [state for state in all_states if state not in guessed_state]
        if len(not_answered) > 0:
            data_out = pandas.DataFrame(not_answered)
            data_out.to_csv("out.csv")
        break
    if answer_state in data.values:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()