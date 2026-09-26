from plistlib import dump
from textwrap import indent
from tkinter import END, messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters)for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers)for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)
    password_final = "".join(password_list)
    entz.delete(0, END)
    entz.insert(0, password_final)
    pyperclip.copy(password_final)

# password = ""
# for char in password_list:
#   password += char

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = ent.get()
    email = entx.get()
    password = entz.get()
    new_data={website:
        {
        "email":email,
        "password":password
    }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty.")

    else:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
                #data=json.read(data_file)
                #print(data)
                #change file mode to "r"

                ent.delete(0, tkinter.END)
                entz.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)
canvas = tkinter.Canvas(width=200, height=200)
ph = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=ph)
canvas.grid(column=1, row=0)
label1=tkinter.Label(window,text="Website:")
label1.grid(column=0,row=1)
ent=tkinter.Entry(window,width=35)
ent.focus()
ent.grid(column=1,row=1,columnspan=2)
label2=tkinter.Label(window,text="Email/Username:")
label2.grid(column=0,row=2)
entx=tkinter.Entry(window,width=35)
entx.grid(column=1,row=2,columnspan=2)
entx.insert(0,"omarsherif3444@gmail.com")
label3=tkinter.Label(window,text="Password:")
label3.grid(column=0,row=3)
entz=tkinter.Entry(window,width=17)
entz.grid(column=1,row=3)
button=tkinter.Button(window,text="Generate Password",command=password_generator)
button.grid(column=2,row=3)
button2=tkinter.Button(window,text="Add",width=30,command=save)
button2.grid(column=1,row=4,columnspan=2)

window.mainloop()