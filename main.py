import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

def generate_password():
    letters_count = random.randint(8, 10)
    symbols_count = random.randint(2, 4)
    numbers_count = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(letters_count)]
    password_symbols = [random.choice(special) for _ in range(symbols_count)]
    password_numbers = [str(random.choice(range(9))) for _ in range(numbers_count)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Missing Fields!")

    else:
        try:
            with open("data.json", "r") as file:
                # read old data
                data = json.load(file)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- Searcg ------------------------------- #
def search_account():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            # read old data
            data = json.load(file)
            username = data[website]["username"]
            password = data[website]["password"]
    except:
        print("No Account Found")
    else:
        messagebox.showinfo(title="Account Found", message=f"Username: {username} \nPassword: {password}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx="50", pady="50")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1,  sticky="EW")

username_text = Label(text="Email/Username:")
username_text.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2,  sticky="EW")

password_text = Label(text="Password:")
password_text.grid(column=0, row=3,)

password_input = Entry(width=21)
password_input.grid(column=1, row=3,  sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Seach", command=search_account)
search_button.grid(column=2, row=1, sticky="EW")

add_button = Button(text="Add", width=36, command=save_pw)
add_button.grid(column=1, row=4, columnspan=2,  sticky="EW")

window.mainloop()
