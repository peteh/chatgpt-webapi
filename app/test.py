from revChatGPT.V1 import Chatbot
from decouple import config
chatbot = Chatbot(config={
    "email": config('OPENAI_USER'),
    "password": config('OPENAI_PASS')
})

prompt = "how many beaches does portugal have?"
response = ""

resone = ""
for data in chatbot.ask(prompt):
    print(data)
    response = data["message"]

print(response)
