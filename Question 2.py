import tkinter as tk

def change_background():
    global button_color
    if button_color == "white":
        button.config(bg="yellow")
        button_color = "yellow"
    else:
        button.config(bg="white")
        button_color = "white"

button_color = "white"

root = tk.Tk()
root.title("Special Midterm Exam In OOP")

root.geometry("520x350")

button = tk.Button(root, text="Click to change color", command=change_background, highlightthickness=0) 
button.pack(pady=150, padx=150)

button.config(activebackground=button["bg"])  

root.mainloop()