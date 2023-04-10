import sqlite3
import tkinter as tk
from PIL import ImageTk
from numpy import random

bg_color = "#3d6466"

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables) - 1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records


def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    ingredients = []

    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " Of " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame1)
    frame1.tkraise()
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")  # widget for frame as image
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text="Ready for your random recipe?",
             bg=bg_color,
             fg="white",
             font=("TkMenuFont", 14)
             ).pack()

    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg=bg_color,
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
    ).pack(pady=25)  # we apply padding  in pack because it fixes position and all.


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()  # most relevant frame will be on top

    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")  # widget for frame as image
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame2,
             text=title,
             bg=bg_color,
             fg="white",
             font=("TkHeadingFont", 20)
             ).pack(pady=25)

    for row in ingredients:
        tk.Label(
            frame2,
            text=row,
            bg="#28393a",
            fg="white",
            font=("TkMenuFont", 12)
            ).pack(fill="both")

    tk.Button(
        frame2,
        text="BACK",
        font=("TkHeadingFont", 20),
        bg=bg_color,
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(pady=25)


root = tk.Tk()
root.title("Recipe picker")  # Title of window
root.eval("tk::PlaceWindow . center")  # Place window at center

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)  # Contain other widget
frame2 = tk.Frame(root, bg=bg_color)

frame1.grid(row=0, column=0,sticky="nesw")
frame2.grid(row=0, column=0,sticky="nesw")

load_frame1()

import sqlite3
import tkinter as tk
from PIL import ImageTk
from numpy import random

bg_color = "#3d6466"

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables) - 1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records


def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    ingredients = []

    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " Of " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame1)
    frame1.tkraise()
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")  # widget for frame as image
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text="Ready for the quiz",
             bg=bg_color,
             fg="purple",
             font=("TkMenuFont", 14)
             ).pack()

    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg=bg_color,
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
    ).pack(pady=25)  # we apply padding  in pack because it fixes position and all.


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()  # most relevant frame will be on top

    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")  # widget for frame as image
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame2,
             text=title,
             bg=bg_color,
             fg="white",
             font=("TkHeadingFont", 20)
             ).pack(pady=25)

    for row in ingredients:
        tk.Label(
            frame2,
            text=row,
            bg="#28393a",
            fg="white",
            font=("TkMenuFont", 12)
            ).pack(fill="both")

    tk.Button(
        frame2,
        text="BACK",
        font=("TkHeadingFont", 20),
        bg=bg_color,
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(pady=25)


root = tk.Tk()
root.title("Recipe picker")  # Title of window
root.eval("tk::PlaceWindow . center")  # Place window at center

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)  # Contain other widget
frame2 = tk.Frame(root, bg=bg_color)

frame1.grid(row=0, column=0,sticky="nesw")
frame2.grid(row=0, column=0,sticky="nesw")

load_frame1()

root.mainloop()

root.mainloop()

