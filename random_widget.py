import tkinter as tk
import random

def generate_random_number():
    """Generate a random number and update the label."""
    random_number = random.randint(0, 100)
    label.config(text=str(random_number))
    root.after(3000, generate_random_number)  # Update every 3 seconds

# Create main window
root = tk.Tk()
root.title("Random Number Widget")

# Make the window small
root.geometry("100x50")
root.resizable(False, False)

# Number label
label = tk.Label(root, text="--", font=("Arial", 20, "bold"))
label.pack(expand=True)

# Start generating numbers
generate_random_number()

# Run GUI
root.mainloop()
