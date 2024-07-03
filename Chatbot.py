import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm doing well, thank you!",
    "what can you do": "I can provide information and answer questions.",
    "bye" or "by": "Goodbye! Have a nice day.",
    "hey": "Hello there! How can I help you?",
    "who is the national bird": "The national bird of India is PEACOCK",
    "which language is very easy in programming": "PYTHON is the simplest language in programming",
    "who is the national animal": "The national animal of India is Tiger",
    "give me a information about programming": "Programming is the process of designing and building computer programs. It involves writing code in a specific programming language to create software applications, websites, games, and more. Programming requires logical thinking, problem-solving skills, and creativity.",
    "example of programming language": "There are many programming languages such as Python, Java, C++, and JavaScript, each with its own syntax and purpose.",
    "what is civil engineering": "Civil engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including works like roads, bridges, canals, dams, and buildings.",
    "what is mechanical engineering": "Mechanical engineering is the discipline that applies engineering, physics, engineering mathematics, and materials science principles to design, analyze, manufacture, and maintain mechanical systems. It is one of the oldest and broadest of the engineering disciplines.",
    "what is electrical engineering": "Electrical engineering is a field of engineering that generally deals with the study and application of electricity, electronics, and electromagnetism. It covers a wide range of subfields including electronics, digital computers, power engineering, telecommunications, control systems, and signal processing.",
    "what is computer engineering": "Computer engineering is a branch of engineering that integrates several fields of computer science and electronic engineering required to develop computer hardware and software. Computer engineers are involved in the design of computer systems and other electronic devices.",
     "what is artificial intelligence": "Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. It includes tasks such as learning, reasoning, problem-solving, perception, and language understanding.",
    "who discovered gravity": "Gravity was discovered by Sir Isaac Newton.",
    "what is the capital of France": "The capital of France is Paris.",
    "what is the tallest mountain in the world": "Mount Everest is the tallest mountain in the world.",
    "default": "Sorry, I don't understand that.",
}


def generate_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

def handle_user_input():
    user_input = entry.get()
    response = generate_response(user_input)
    output.insert(tk.END, f"You: {user_input}\n", "user")
    output.insert(tk.END, f"Bot: {response}\n\n", "bot")
    output.see(tk.END) 
    entry.delete(0, tk.END)

def clear_chat():
    output.delete('1.0', tk.END)

window = tk.Tk()
window.title("ChatBot")
window.geometry("600x500")
window.minsize(400, 300)  

welcome_message = "Welcome! I am ChatBot. Ask me anything ."

output = scrolledtext.ScrolledText(window, width=60, height=20, font=("Arial", 15))
output.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
output.tag_config("user", foreground="red")
output.tag_config("bot", foreground="blue")
output.insert(tk.END, f" {welcome_message}\n\n", "bot")
output.see(tk.END) 

entry = tk.Entry(window, width=50, font=("Arial", 12))
entry.pack(pady=10, expand=True, fill=tk.X)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

click_button = tk.Button(button_frame, text="Click", command=handle_user_input, bg="lightblue", font=("Arial", 12))
click_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_chat, bg="lightcoral", font=("Arial", 12))
clear_button.pack(side=tk.LEFT, padx=5)

window.mainloop()
