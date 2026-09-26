import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(window, text="CHAMPAIN", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input_box.get())

button = tkinter.Button(window, text="Click Me", command=button_clicked)
button.grid(column=1, row=1, padx=20, pady=20)

input_box = tkinter.Entry(window)
input_box.grid(column=3, row=3, padx=20, pady=20)

button2 = tkinter.Button(window, text="OK!")
button2.grid(column=2, row=0, padx=20, pady=20)

window.mainloop()