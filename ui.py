import tkinter as tk
from main import run

def start():
    output.insert("end", "Running repair...\n")
    run()
    output.insert("end", "Done.\n")

root = tk.Tk()
root.title("Repair AI Tool")

btn = tk.Button(root, text="Run Repair", command=start)
btn.pack()

output = tk.Text(root, height=20, width=60)
output.pack()

root.mainloop()
