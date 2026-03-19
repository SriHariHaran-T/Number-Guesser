attempts = 3
import random
import tkinter as tk

number = random.randint(1, 10)
    
def check_guess():
    global attempts
    attempts -= 1   
    guess = int(entry.get())
    
    if guess == number:
        result_label.config(text="Correct!")
    elif attempts == 0:
        result_label.config(text=f"Game Over! The number was: {number}")
    elif guess < number:
        result_label.config(text=f"Too low! The Remaining attempts: {attempts}")
    else:
        result_label.config(text=f"Too high! The Remaining attempts: {attempts}")

# window
root = tk.Tk()
root.title("Number Guesser")
root.geometry("300x200")

# attempts label
attempts_label = tk.Label(root, text=f"Total Attempts: {attempts}")
attempts_label.pack()

# text
label = tk.Label(root, text="Guess a number (1-10)")
label.pack()

# input box
entry = tk.Entry(root)
entry.pack()

# button
button = tk.Button(root, text="Check", command=check_guess)
button.pack()

#figet
subscribe = tk.Button(root, text="Subscribe To HeoCraft")
subscribe.pack()

# result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()