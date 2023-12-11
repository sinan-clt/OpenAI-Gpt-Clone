import os
import openai
import gradio as gr
from dotenv import load_dotenv
import openai

load_dotenv()  # This loads the environment variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help ypu today?\nHuman: "

def gpt_output(prompt,state):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=True,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:"," AI:"]
    )
    return response.choices[0].text

def chat_gpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ''.join(s)
    output = gpt_output(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>AGI AI Assistant</h1></center>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chat_gpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug=True)






