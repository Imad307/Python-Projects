import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
US_States_Image = "blank_states_img.gif"
screen.addshape(US_States_Image)
turtle.shape(US_States_Image)

state_data = pd.read_csv("50_states.csv")
result = state_data.set_index("state").values.tolist()
state_dict = dict(zip(state_data["state"], result))
print(state_dict)
# all_states = state_data.state.to_list()
# all_states_x_cor_list = state_data.x.to_list()
# all_states_y_cor_list = state_data.y.to_list()
guessed_states = []
ending_words = ["End","Finished", "Give up", "Exit"]
attempt = 0
while attempt!= 100:
    attempt+=1
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 correct US State Guesses", prompt = "Enter the US State Name: ").title()
    if user_answer in state_dict and user_answer not in guessed_states:
        state_x_cor = state_dict[user_answer][0]
        state_y_cor = state_dict[user_answer][1]
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(state_x_cor, state_y_cor)
        state_text.write(arg=f"{user_answer}")
        guessed_states.append(user_answer)
    elif user_answer in ending_words:
        missed_states = []
        for key in state_dict:
            if key in guessed_states:
                continue
            else:
                missed_states.append(key)
        states_to_learn = pd.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        turtle.done()
        break
    else:
        continue

#states that user missed


if len(missed_states) == 0:
    print("You know all the states. You are a genius.")
else:
    print(f"Here are all the states you missed: {missed_states}")

