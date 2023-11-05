import tkinter

def button_click():
    user_input = input.get()
    my_label.config(text= f"{user_input}")


window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "underline"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"



# Button
button = tkinter.Button(text="egg", command=button_click)
button.grid(column=1, row=1)

# New button
new_button = tkinter.Button(text="new_egg", command=button_click)
new_button.grid(column=2, row=0)

# entry 
input = tkinter.Entry(width= 10)
input.grid(column=3, row=2)
# user_input = input.get()

window.mainloop()



# # Args and kwargs
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     # print(total)
#     return total


# add(1, 2, 3, 4, 5)

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)