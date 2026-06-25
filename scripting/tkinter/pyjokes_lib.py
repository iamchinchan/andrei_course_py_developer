import tkinter as tk
import pyjokes

print(tk.TkVersion)

# Create the main window
root = tk.Tk()
root.title("My First Tkinter GUI")
# Add a label to the window
label = tk.Label(root, text=pyjokes.get_joke())
label.pack()
# Start the Tkinter event loop
root.mainloop()
