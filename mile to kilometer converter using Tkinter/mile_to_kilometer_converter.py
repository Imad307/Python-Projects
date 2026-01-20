from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(600, 600)
window.config(padx=20, pady=20)

main = Frame(window)
main.grid()

Label(main, text="Enter Miles", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")

entry = Entry(main, width=20)
entry.grid(row=0, column=1)

Label(main, text="is equal to", font=("Arial", 16, "bold")).grid(row=1, column=0, sticky="w")

output = Label(main, text="", font=("Arial", 16, "bold"), width=20, anchor="w")
output.grid(row=1, column=1)

def submit():
    try:
        miles = float(entry.get())
        output.config(text=f"{miles * 1.6:.2f} Kilometers")
    except ValueError:
        notification("Only Numbers Allowed")

Button(
    main,
    text="Calculate",
    font=("Arial", 14, "bold"),
    command=submit
).grid(row=2, column=0, columnspan=2, pady=10)

def notification(message, duration=2000):
    popup = Toplevel(window)
    popup.overrideredirect(True)
    popup.attributes("-topmost", True)
    popup.geometry("300x50+100+50")

    Label(
        popup,
        text=message,
        bg="black",
        fg="white",
        padx=10,
        pady=5
    ).grid()

    popup.after(duration, popup.destroy)

window.mainloop()
