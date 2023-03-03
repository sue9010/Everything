import tkinter as tk
import requests

def send_request():
    user_input = input_field.get()
    response = requests.post("https://api.openai.com/v1/engines/chatgpt/jobs", json={ "prompt": user_input })
    output = response.json()["choices"][0]["text"]
    output_field.insert("end", output)

root = tk.Tk()
root.title("ChatGPT GUI")

input_field = tk.Entry(root)
input_field.pack()

send_button = tk.Button(root, text="Send", command=send_request)
send_button.pack()

output_field = tk.Text(root)
output_field.pack()

root.mainloop()