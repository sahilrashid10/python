from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
FONT = ("Arial", 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #replacing the below code by list comprehension and for loop by join
    #nr_letters = random.randint(8, 10)
    #nr_symbols = random.randint(2, 4)
    #nr_numbers = random.randint(2, 4)
    # password_list = []
    #
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #     password += char
    #print(f"Your password:{password}")

    #continue..
    pas_letter = [choice(letters) for _ in range(randint(8, 10))]
    pas_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pas_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    pass_list = pas_letter + pas_numbers + pas_symbols
    shuffle(pass_list)
    # join()
    # pas = ""
    # for char in pass_list:
    #     pas += char
    # print(f"Your password:{pas}")
    #continue...(for de bugging print)
    pas = "".join(pass_list)
    # print(f"Your Password: {pas}")
    pass_entry.insert(0, pas)
    pyperclip.copy(pas)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("OOPS", "Please don't leave input empty.")
    else:
        flag = messagebox.askyesno(title="Confirm data entered", message=f"Website:{website}\nEmail:{email}"
                                                                         f"\nPassword:{password}\n")
        if flag:
            with open("password_data.txt", "a") as file:
                file.write(website + "|")
                file.write(email + "|")
                file.write(password + "\n")
                web_entry.delete(0, END)
                mail_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Main window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="black")

# Canvas for logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0)
email_label = Label(text="Email/User-Name:", font=FONT)
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:", font=FONT)
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(font=FONT, width=32)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
web_entry.focus()
mail_entry = Entry(font=FONT, width=32)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "sahil@gmail.com")

# Password entry and button
pass_entry = Entry(font=FONT, width=20)
pass_entry.grid(row=3, column=1)
generate_button = Button(text="Generate Password", font=FONT, width=15, command=generate_password)
generate_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", font=FONT, width=32, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

# Main loop
window.mainloop()


def add(*args):
    s = 0
    for i in args:
        s = s + i
    return s


a = add(1, 2, 4, 5, 6)
print(a)
