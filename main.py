from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_for_password = [choice(letters) for _ in range(randint(8, 10))]
    symbols_for_password = [choice(symbols) for _ in range(randint(2, 4))]
    number_for_password = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_for_password + symbols_for_password + number_for_password
    shuffle(password_list)

    ## This next line take all velues from list and join it
    ## example list["d", "i","m", "a"]  when we use join list we get dima

    password = "".join(password_list)

    ### I need to put my result in field passwrod
    ## Now this funcrtion just generate the password

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_user():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("database.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("database.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("database.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            ## afte click on ADD button, delate all symbols which we write in website and password fields
            website_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get()
    try:
        with open("database.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for Website: {website} exists.")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=30)

canvas = Canvas(width=200, height=200, bg="black")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "@gmail.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=35)
password_input.grid(column=1, row=3)


generate_password = Button(text="Generate Password", width=30, command=create_random_password)
generate_password.grid(column=1, row=4)


add_button = Button(text="Add", width=30, command=save_user)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text="Search", width=30, command=find_password)
search_button.grid(column=1, row=6, columnspan=2)



window.mainloop()
