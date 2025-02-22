import random
import nltk
from nltk.chat.util import Chat, reflections
import gradio as gr

# Define chatbot responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm fine, thank you!", "I'm doing great!"]],
    ["what is your name?", ["I'm a chatbot!", "Call me AI Bot!"]],
    ["bye|goodbye", ["Goodbye!", "See you soon!", "Take care!"]],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

def chat_with_ai(user_input):
    return chatbot.respond(user_input.lower())

# Gradio UI for interaction
iface = gr.Interface(fn=chat_with_ai, inputs="text", outputs="text")
iface.launch()
