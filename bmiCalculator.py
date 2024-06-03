import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

# Initialize main window
root = tk.Tk()
root.title("BMI Calculator")

# Load data if available
data_file = 'bmi_data.json'
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        users_data = json.load(file)
else:
    users_data = {}

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        result_label.config(text=f"BMI: {bmi}")
        
        user = user_entry.get()
        if user not in users_data:
            users_data[user] = []
        users_data[user].append({'date': str(datetime.now()), 'bmi': bmi})
        
        with open(data_file, 'w') as file:
            json.dump(users_data, file)
        
        messagebox.showinfo("BMI Calculator", f"Your BMI is {bmi}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Function to view historical data
def view_history():
    user = user_entry.get()
    if user in users_data:
        history = users_data[user]
        history_text = "\n".join([f"{entry['date']}: {entry['bmi']}" for entry in history])
        messagebox.showinfo("BMI History", history_text)
    else:
        messagebox.showinfo("BMI History", "No data available for this user.")

# Function to plot BMI trend
def plot_trend():
    user = user_entry.get()
    if user in users_data:
        dates = [entry['date'] for entry in users_data[user]]
        bmis = [entry['bmi'] for entry in users_data[user]]
        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o')
        plt.xlabel('Date')
        plt.ylabel('BMI')
        plt.title(f'BMI Trend for {user}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("BMI Trend", "No data available for this user.")

# User input fields
tk.Label(root, text="User:").grid(row=0, column=0, padx=10, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate BMI button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# View history button
history_button = tk.Button(root, text="View History", command=view_history)
history_button.grid(row=4, column=0, columnspan=2, pady=5)

# Plot trend button
plot_button = tk.Button(root, text="Plot Trend", command=plot_trend)
plot_button.grid(row=5, column=0, columnspan=2, pady=5)

# Result display
result_label = tk.Label(root, text="BMI: N/A")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
