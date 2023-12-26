import tkinter as tk
import subprocess

def run_program():
    # Replace 'your_program.py' with the program you want to run
    subprocess.Popen(['python', 'app.py'])

# Create the main window
root = tk.Tk()
root.title("Program Runner")

# Create a button to run the program
run_button = tk.Button(root, text="Run Program", command=run_program)
run_button.pack()

# Run the Tkinter main loop
root.mainloop()
