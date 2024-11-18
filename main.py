import tkinter as tk
from tkinter import ttk
import openai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()  # Ensure your .env file is named `.env` and in the same directory
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please add your API key to the .env file.")

openai.api_key = API_KEY

def generate_completion():
    user_input = prompt_entry.get("1.0", tk.END).strip()
    if not user_input:
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        output_box.config(state="disabled")
        return

    try:
        # Call the OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100
        )
        
        print(f"API Response: {response}")
        # Extract and display the response
        output = response["choices"][0]["message"]["content"].strip()
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state="disabled")
    except Exception as e:
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")
        output_box.config(state="disabled")


# Create the GUI
app = tk.Tk()
app.title("Interactive GUI Project")
app.geometry("500x400")

# Prompt Label and Textbox
prompt_label = ttk.Label(app, text="Enter your prompt:")
prompt_label.pack(pady=10)

prompt_entry = tk.Text(app, height=5, width=50)
prompt_entry.pack(pady=5)

# Submit Button
submit_button = ttk.Button(app, text="Submit", command=generate_completion)
submit_button.pack(pady=10)

# Output Box
output_label = ttk.Label(app, text="Output:")
output_label.pack(pady=10)

output_box = tk.Text(app, height=10, width=50, state="disabled")
output_box.pack(pady=5)

print("Starting the GUI...")  # Moved before the GUI starts
# Run the GUI
app.mainloop()
