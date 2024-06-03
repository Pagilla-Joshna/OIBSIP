import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Password Generator")
        self.geometry("500x400")
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="Password Generator", font=("Arial", 18))
        title_label.pack(pady=10)

        # Password Length
        length_label = tk.Label(self, text="Password Length:")
        length_label.pack(pady=5)
        
        self.length_var = tk.IntVar(value=12)
        length_spinbox = tk.Spinbox(self, from_=8, to=32, textvariable=self.length_var)
        length_spinbox.pack(pady=5)

        # Complexity Options
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        
        upper_check = tk.Checkbutton(self, text="Include Uppercase Letters", variable=self.include_upper)
        upper_check.pack(pady=2)
        
        lower_check = tk.Checkbutton(self, text="Include Lowercase Letters", variable=self.include_lower)
        lower_check.pack(pady=2)
        
        digits_check = tk.Checkbutton(self, text="Include Digits", variable=self.include_digits)
        digits_check.pack(pady=2)
        
        special_check = tk.Checkbutton(self, text="Include Special Characters", variable=self.include_special)
        special_check.pack(pady=2)

        # Generate Button
        generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        # Password Display
        self.password_entry = tk.Entry(self, width=30, font=("Arial", 14))
        self.password_entry.pack(pady=5)
        
        # Copy to Clipboard Button
        copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        include_upper = self.include_upper.get()
        include_lower = self.include_lower.get()
        include_digits = self.include_digits.get()
        include_special = self.include_special.get()

        if not any([include_upper, include_lower, include_digits, include_special]):
            messagebox.showwarning("Invalid Options", "At least one character type must be selected.")
            return
        
        characters = ""
        if include_upper:
            characters += string.ascii_uppercase
        if include_lower:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard")
        else:
            messagebox.showwarning("Empty Password", "No password to copy")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
