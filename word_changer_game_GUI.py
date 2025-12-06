import tkinter as tk
from tkinter import messagebox, simpledialog
from word_changer_game import WordLadderGame

class WordLadderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Ladder Game")
        self.game = None
        self.setup_start_screen()

    def setup_start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Word Ladder Game", font=("Arial", 16)).pack(pady=10)
        self.word_length_var = tk.StringVar()
        self.start_word_var = tk.StringVar()
        self.goal_word_var = tk.StringVar()
        
        tk.Label(self.root, text="Word Length:").pack()
        tk.Entry(self.root, textvariable=self.word_length_var).pack()
        tk.Label(self.root, text="Start Word:").pack()
        tk.Entry(self.root, textvariable=self.start_word_var).pack()
        tk.Label(self.root, text="Goal Word:").pack()
        tk.Entry(self.root, textvariable=self.goal_word_var).pack()
        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        try:
            word_length = int(self.word_length_var.get())
            if word_length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer greater than 0 for word length.")
            return
        start_word = self.start_word_var.get()
        goal_word = self.goal_word_var.get()
        self.game = WordLadderGame(word_length, start_word, goal_word)
        valid, msg = self.game.validate_start_and_goal()
        if not valid:
            messagebox.showerror("Error", msg)
            return
        self.setup_game_screen()

    def setup_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        state = self.game.get_state()
        tk.Label(self.root, text=f"Transform '{state['current_word']}' to '{state['goal_word']}' one letter at a time.", wraplength=350).pack(pady=10)
        self.move_var = tk.StringVar()
        self.moves_label = tk.Label(self.root, text="Moves: " + ", ".join(state['moves']))
        self.moves_label.pack(pady=5)
        tk.Entry(self.root, textvariable=self.move_var).pack()
        tk.Button(self.root, text="Submit Move", command=self.submit_move).pack(pady=5)
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=5)

    def submit_move(self):
        move = self.move_var.get()
        success, msg = self.game.make_move(move)
        if not success:
            self.status_label.config(text=msg, fg="red")
        else:
            self.status_label.config(text="", fg="black")
            state = self.game.get_state()
            self.moves_label.config(text="Moves: " + ", ".join(state['moves']))
            self.move_var.set("")
            if state['finished']:
                messagebox.showinfo("Congratulations!", f"You turned '{state['moves'][0]}' into '{state['goal_word']}' in {len(state['moves'])-1} moves!")
                self.ask_save_results(state)

    def ask_save_results(self, state):
        answer = messagebox.askyesno("Save Results", "Would you like to save your game results to a .txt file?")
        if answer:
            import os
            from tkinter import filedialog
            default_filename = "word_changer_game_results.txt"
            downloads = os.path.join(os.path.expanduser("~"), "Downloads")
            initialfile = default_filename
            initialdir = downloads if os.path.exists(downloads) else os.path.expanduser("~")
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=initialfile,
                initialdir=initialdir,
                title="Save Game Results",
                filetypes=[("Text Files", "*.txt")]
            )
            if file_path:
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("Word changer game results\n")
                        f.write(f"Start word: {state['moves'][0]}\n")
                        f.write(f"Goal word: {state['goal_word']}\n")
                        f.write(f"Number of turns: {len(state['moves'])-1}\n")
                    messagebox.showinfo("Saved", f"Results saved to {file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save file: {e}")
        self.setup_start_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordLadderGUI(root)
    root.mainloop()
