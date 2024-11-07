import tkinter as tk

def display_name():
    full_name = entry.get()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, full_name)

root = tk.Tk()
root.title("Midterm in OOP")
root.geometry("520x350")

input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=20)

label = tk.Label(input_frame, text="Enter your fullname:", fg='red', font=("Arial", 8))
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(input_frame, width=30, font=("Arial", 10))
entry.grid(row=0, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button = tk.Button(button_frame, text="Click to display your Fullname", command=display_name, fg='red', font=("Arial", 8), width=25)
button.grid(row=0, column=0, padx=10)

result_entry = tk.Entry(button_frame, width=30, font=("Arial", 10))
result_entry.grid(row=0, column=1)

root.mainloop()
