# FridayProject9

FridayProject9

This project is an interactive GUI-based application that utilizes OpenAI's API to generate responses to user prompts. It allows users to input a text prompt, submit it via a graphical user interface, and view the AI-generated output.

Features

Interactive GUI: Built with Tkinter, the application provides a user-friendly interface for entering prompts and viewing results.

OpenAI Integration: Connects to OpenAI's ChatCompletion API (e.g., GPT-3.5-turbo) for generating responses.

Environment Variable Security: Uses a .env file to securely store the OpenAI API key.

How to Run

Prerequisites

Python 3.7 or higher installed on your machine.

Required libraries installed:

openai

python-dotenv

tkinter (usually pre-installed with Python)

Setup

Clone the repository:

git clone https://github.com/bgettler30/FridayProject9.git
cd FridayProject9

Install the required Python libraries:

pip install openai python-dotenv

Create a .env file in the FridayProject9 folder:

OPENAI_API_KEY=your_actual_api_key_here

Replace your_actual_api_key_here with your OpenAI API key.

Run the application:

python3 main.py

Usage

Enter a prompt into the text box.

Click the Submit button.

View the AI-generated response in the output box.

File Structure

main.py: The main Python script that runs the application.

.env: Stores the OpenAI API key (excluded from version control).

.gitignore: Ensures sensitive files like .env are not committed to the repository.

Example Prompts

"What is the capital of France?"

"Write a short poem about the ocean."

"Tell me a joke."

Troubleshooting

API Key Not Found: Ensure the .env file is in the same directory as main.py and correctly formatted.

Empty Prompt Error: Enter text in the input box before clicking Submit.

Connection Issues: Ensure you have an active internet connection and valid API key.

Future Enhancements

Add support for selecting different OpenAI models.

Improve error handling and display user-friendly messages.

Enhance the GUI with custom styling.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Created by Bryce Gettler.

For questions or feedback, feel free to reach out!
