# Import Required Library
from tkinter import *
from tkinter import ttk
from random import *

# Create Object
root = Tk()

# Set geometry
root.geometry("350x400")

root.title("Suit")

# List of players
list = ["batu","kertas","gunting"]

choose_number = randint(0,2)
print(choose_number) # For testing if it works

label = Label(root,text="Computer ",width = 20,height=4,font=("bell mt",15))
label.pack()

def spin():
    choose_number = randint(0,2)
    label.config(text=list[choose_number])
    if user_select.get() == "Batu":
        user_select_value = 0
        print(user_select_value)
    elif user_select.get() == "Kertas":
        user_select_value = 1
        print(user_select_value)
    elif user_select.get() == "Gunting":
        user_select_value = 2
        print(user_select_value)

    if user_select_value == 0:
        if choose_number == 0:
            wl_label.config(text="Seri! - "+" Computer:Bad luck")
        elif choose_number == 1:
            wl_label.config(text="Kamu Kalah - "+" Computer: Gua Lebih Jago ")
        elif choose_number == 2 :
            wl_label.config(text="Kamu Menang - "+" Computer: Lu Beruntung Kali ini")

    elif user_select_value == 1:
        if choose_number == 1:
            wl_label.config(text="Seri! - "+" Computer: NT NT")
        elif choose_number == 0:
            wl_label.config(text="Kamu Menang - "+" Computer: Anjay Lu Jago")
        elif choose_number == 2 :
            wl_label.config(text="Kamu Kalah - "+" Computer: WLeeeee :P")

    elif user_select_value == 2:
        if choose_number == 2:
            wl_label.config(text="Seri!")
        elif choose_number == 0:
            wl_label.config(text="Kamu Kalah - "+" Computer: Keren kan Gue")
        elif choose_number == 1 :
            wl_label.config(text="Kamu Menang")



# Adding dropdown box for Rock,Paper,Scissors
user_select = ttk.Combobox(root,value=["Batu","Kertas","Gunting"])
user_select.current(0)
user_select.pack()

# Add Labels,Button
wl_label = Label(root,text="",font=("arial",10),width=50,height=4)
wl_label.pack()

button = Button(root,text="Mulai!",font=("bell mt",10),command=spin)
button.pack()

root.mainloop()
