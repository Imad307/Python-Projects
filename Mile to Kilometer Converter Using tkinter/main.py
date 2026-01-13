from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(width=500, height=500)

#label
my_label = Label(text="I am a Label.", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)

my_label.config(text="Imad's Windows Dashboard")

#create button
def button_clicked():
    user_input = entry.get()
    my_label.config(text=f"{user_input}")


button = Button(text="Click Me", command=button_clicked, width=10)
button.grid(column=2, row=2)

new_button = Button(text="New Button", command=button_clicked, width=20)
new_button.grid(column=3, row=0)

#get entry
entry = Entry(width=20)
entry.insert(END, string="Type anything")
entry.grid(column=4, row=4)



window.mainloop()