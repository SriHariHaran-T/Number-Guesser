import random
import webbrowser
import tkinter as tk
from tkinter import ttk

# game state
attempts = 3
number = random.randint(1, 10)


def reset_game():
    global attempts, number
    set_difficulty()  # apply selected difficulty
    number = random.randint(1, 10)

    result_label.config(text="")
    reset_label.config(text="New number generated!")
    root.after(1500, lambda: reset_label.config(text=""))   
    entry.delete(0, tk.END)
    check_button.config(state="normal")
    reset_button.config(state="disabled")

def clear_message():
    result_label.config(text="")
    sub_label.config(text="")

def subscribe():
    sub_label.config(text="Thank you for subscribing to HeoCraft!")
    webbrowser.open("https://www.youtube.com/@HeoCraft")
    root.after(1500, clear_message)

def set_difficulty():
    global attempts
    mode = difficulty.get()

    if mode == "Easy":
        attempts = 5
        number = random.randint(1, 10)  # wider range for easy mode
        label.config(text="Guess a number between (1-10)")
    elif mode == "Medium":
        attempts = 3
        number = random.randint(1, 15)
        label.config(text="Guess a number between (1-15)")

    else:
        attempts = 2
        number = random.randint(1, 20)  # narrower range for hard mode
        label.config(text="Guess a number between (1-20)")

    attempts_label.config(text=f"Remaining attempts: {attempts}")

def check_guess():
    global attempts

    if attempts <= 0:
        return

    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number!")
        root.after(1500, clear_message)
        return

    if guess == number:
        result_label.config(text=f"Correct! Number was {number}")
        check_button.config(state="disabled")
        reset_button.config(state="normal")
        return

    attempts -= 1
    attempts_label.config(text=f"Remaining attempts: {attempts}")

    if attempts <= 0:
        result_label.config(text=f"Game Over! Number was {number}")
        check_button.config(state="disabled")
        reset_button.config(state="normal")
    elif guess < number:
        result_label.config(text="Too low!")
    else:
        result_label.config(text="Too high!")

    entry.delete(0, tk.END)
    root.after(1500, clear_message)

# window
root = tk.Tk()
root.title("Number Guesser")
root.geometry("400x480")

# difficulty variable
difficulty = tk.StringVar(value="Medium")

style = ttk.Style()
style.theme_use("clam")

#  Difficulty Section
settings_frame = ttk.LabelFrame(root, text="Difficulty")
settings_frame.pack(padx=10, pady=10, fill="x")

ttk.Radiobutton(settings_frame, text="Easy", value="Easy",variable=difficulty, command=set_difficulty).pack(anchor="w", padx=10)
ttk.Radiobutton(settings_frame, text="Medium", value="Medium",variable=difficulty, command=set_difficulty).pack(anchor="w", padx=10)
ttk.Radiobutton(settings_frame, text="Hard", value="Hard",variable=difficulty, command=set_difficulty).pack(anchor="w", padx=10)

# Game Section
game_frame = ttk.LabelFrame(root, text="Game")
game_frame.pack(padx=10, pady=10, fill="x")

label = ttk.Label(game_frame, text="Choose a difficulty to start guessing!")
label.pack(pady=5)

entry = ttk.Entry(game_frame, width=20, justify="center")
entry.pack(pady=5)
entry.focus()

check_button = ttk.Button(game_frame, text="Check", command=check_guess)
check_button.pack(pady=5)

# Status Section
status_frame = ttk.LabelFrame(root, text="Status")
status_frame.pack(padx=10, pady=10, fill="x")

attempts_label = ttk.Label(status_frame, text="Remaining attempts: 3")
attempts_label.pack(pady=5)

result_label = ttk.Label(status_frame, text="")
result_label.pack(pady=5)

reset_label = ttk.Label(status_frame, text="")
reset_label.pack(pady=5)

sub_label = ttk.Label(status_frame, text="")
sub_label.pack(pady=5)

# Bottom buttons
button_frame = ttk.Frame(root)
button_frame.pack(side="bottom", fill="x", pady=10)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

reset_button = ttk.Button(button_frame, text="Reset Game", command=reset_game)
reset_button.grid(row=0, column=0, sticky="w", padx=10)
reset_button.config(state="disabled")

subscribe_button = ttk.Button(button_frame, text="Subscribe", command=subscribe)
subscribe_button.grid(row=0, column=1, sticky="e", padx=10)

root.mainloop()