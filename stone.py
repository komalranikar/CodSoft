import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.configure(bg='#FFFFE0')  
        self.root.geometry("500x300")

        self.user_score = 0
        self.comp_score = 0

        self.label = tk.Label(root, text="Choose: Rock, Paper, or Scissors", font=('Times New Roman', 20, 'bold'), bg='#FFFFE0')
        self.label.pack()

        self.buttons_frame = tk.Frame(root, bg='#FFFFE0')
        self.buttons_frame.pack()

        self.choices = ["👊 Rock", "📄 Paper", "✂️ Scissors"]

        self.user_choice = tk.StringVar()

        for choice in self.choices:
            button = tk.Button(self.buttons_frame, text=choice, font=('Times New Roman', 16, 'bold'),
                               command=lambda ch=choice.split()[-1]: self.play(ch), width=12, height=2, bg='#800000', fg='#FFFFFF',
                               activebackground='#8B0000', activeforeground='#FFFFFF')
            button.pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])

        result = self.get_result(user_choice, comp_choice)

        messagebox.showinfo("Result", f"User: {user_choice}\nComputer: {comp_choice}\n{result}")

        self.label.config(text=f"Score - User: {self.user_score} Computer: {self.comp_score}")

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            self.root.destroy()

    def get_result(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Scissors" and comp_choice == "Paper") or \
             (user_choice == "Paper" and comp_choice == "Rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.comp_score += 1
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
