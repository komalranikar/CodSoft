import tkinter as tk
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Password length should be greater than zero.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        password_label.config(text="Generated Password: " + password)
    except ValueError:
        password_label.config(text="Invalid input! Please enter a valid integer.")

root = tk.Tk()
root.geometry("700x700")
root.title("Password Generator")
root.configure(bg='mediumpurple1')
times_font_big_bold = ('Times New Roman', 16, 'bold')
length_label = tk.Label(root, text="Enter Password Length:", bg='white', font=times_font_big_bold)
length_label.pack()
length_entry = tk.Entry(root, font=times_font_big_bold)
length_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#4caf50',
                            fg='white', font=times_font_big_bold)  # Set background, foreground colors, and font size
generate_button.pack()
password_label = tk.Label(root, text="", bg='#f0f0f0', font=times_font_big_bold)  # Set background color and font size
password_label.pack()
root.mainloop()
