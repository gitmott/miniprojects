import tkinter

def calculate_km():
    user_input = miles_entry.get()
    converted_km = float(user_input) * 1.6
    calculated_km_label.config(text= f"{converted_km}")

    # output = int(user_input) * 1.6
    # calculated_km_label.config(output)
    # return 

# Window
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)

# Labels
equals_label = tkinter.Label(text="is equal to")
equals_label.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calculated_km_label = tkinter.Label(text="0")
calculated_km_label.grid(column=1, row=1)

# Entry
miles_entry = tkinter.Entry(width= 10)
miles_entry.grid(column=1, row=0)

# Button
calculate_button = tkinter.Button(width=10, text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)




window.mainloop()
