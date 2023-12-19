from tkinter import *
from tkinter import messagebox



# Password saving
def save():
   
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You have left a field blank, go back and enter a value")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                    f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_user_entry.delete(0, END)
                password_entry.delete(0, END)




# SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=500, height=540)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "mattemail@email.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password:")
generate_password_button.grid(row=3, column=2)
add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)





window.mainloop()