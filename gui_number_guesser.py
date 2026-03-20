import random
import tkinter as tk

# initial game state
attempts = 3
number = random.randint(1, 10)

def reset_game():
    global attempts, number
    attempts = 3
    number = random.randint(1, 10)

    result_label.config(text="")
    attempts_label.config(text=f"Remaining attempts: {attempts}")
    reset_label.config(text="New number generated!")
    root.after(1500, lambda: reset_label.config(text=""))
    entry.delete(0, tk.END)
    check_button.config(state="normal", text="Check", fg="black")
    reset_button.config(state="disabled")   

def clear_message():
    result_label.config(text="")   
    sub_label.config(text="")
def subscribe():
    sub_label.config(text="Thank you for subscribing to HeoCraft!")
    root.after(1500, clear_message)
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        root.after(1500, clear_message)
        return

    if guess == number:
        result_label.config(text=f"Correct! The number was {number}.", fg="green")
        check_button.config(state="disabled", text="Reset to Play Again")
        return

    attempts -= 1
    attempts_label.config(text=f"Remaining attempts: {attempts}")

    if attempts <= 0:
        result_label.config(text=f"Game Over! The number was: {number}", fg="red")
        check_button.config(state="disabled", text="Reset to Play Again")
    elif guess < number:
        result_label.config(text="Too low!", fg="red")
    else:
        result_label.config(text="Too high!", fg="red")

    if guess == number or attempts <= 0:
        reset_button.config(state="normal")
    
    root.after(1500, clear_message)

# window
root = tk.Tk()
root.title("Number Guesser")
root.geometry("320x320")

# attempts label
attempts_label = tk.Label(root, text="Remaining attempts: 3")
attempts_label.pack(pady=10)

# button frame (bottom bar)
button_frame = tk.Frame(root)
button_frame.pack(side="bottom", fill="x", pady=10)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

reset_button = tk.Button(button_frame, text="Reset Game", command=reset_game)
reset_button.grid(row=0, column=0, sticky="w", padx=10)
reset_button.config(state="disabled")

subscribe_button = tk.Button(button_frame, text="Subscribe To HeoCraft", command=subscribe)
subscribe_button.grid(row=0, column=1, sticky="e", padx=10)

# text
label = tk.Label(root, text="Guess a number (1-10)")
label.pack(pady=5)

# center frame for entry + check button
center_frame = tk.Frame(root)
center_frame.pack(pady=5)

entry = tk.Entry(center_frame, width=20, justify="center")
entry.focus_set()
entry.grid(row=0, column=0, padx=5)

check_button = tk.Button(center_frame, text="Check", command=check_guess)
check_button.grid(row=1, column=0, pady=8)

# reset message label
reset_label = tk.Label(root, text="")
reset_label.config(fg="green")
reset_label.pack(pady=5)

# subscription label
sub_label = tk.Label(root, text="")
sub_label.pack(pady=5)

# result
result_label = tk.Label(root, text="")
result_label.pack(pady=5)


root.mainloop()