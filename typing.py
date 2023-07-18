import tkinter as tk
from time import time
import random

# list of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump",
    "Bright vixens jump; dozy fowl quack",
    "Sphinx of black quartz, judge my vow",
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.start_time = None
        self.end_time = None
        self.sentence = tk.StringVar()
        self.result_text = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Type the following sentence:").pack()
        tk.Label(self.root, textvariable=self.sentence).pack()
        self.input_field = tk.Entry(self.root)
        self.input_field.pack()
        self.input_field.bind('<Return>', self.check_speed)  # Bind 'Return' key to check_speed
        tk.Label(self.root, textvariable=self.result_text).pack()
        self.get_new_sentence()

    def get_new_sentence(self):
        self.sentence.set(random.choice(sentences))
        self.start_time = time()

    def check_speed(self, event=None):  # Add event parameter for key binding
        self.end_time = time()
        typed_text = self.input_field.get()
        if typed_text == self.sentence.get():
            elapsed_time = self.end_time - self.start_time
            words_per_minute = (len(typed_text.split()) / elapsed_time) * 60
            self.result_text.set(f"Your typing speed is {words_per_minute:.2f} words per minute")
        else:
            self.result_text.set("The sentence is not typed correctly. Try again.")
        self.input_field.delete(0, 'end')
        self.get_new_sentence()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
