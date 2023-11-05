import tkinter

window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "underline"))
my_label.pack()

my_label["text"] = "New Text"
# my_label.config(text="New Text")



def button_click():
    user_input = input.get()
    my_label.config(text= f"{user_input}")


button = tkinter.Button(text="egg", command=button_click)
button.pack()

# entry 
input = tkinter.Entry(width= 10)
input.pack()
# user_input = input.get()



window.mainloop()

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