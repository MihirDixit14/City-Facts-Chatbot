from flask import Flask, jsonify, request
import requests
from nltk.chat.util import Chat, reflections


app=Flask(__name__)

def get_city_name(city_name):
     
     url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city_name}"
     response=requests.get(url)
     if response.status_code==200:
          data=response.json()
          
          return data['extract']
     return "Sorry, The city name is invalid or there are no facts in the database."


pairs = [
    [
        r"hi|hello|hey",
        ["Hello! I'm your chatbot. You can ask me about any city, and I'll provide some interesting facts."]
    ],
    [
        r"(.*) city facts (.*)",
        ["Sure! Just tell me the name of a city, and I'll give you some cool facts."]
    ],
    [
        r"tell me about (.*)",
        ["I can find facts about a city. Just give me a city name!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad I could help!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Please ask about a city, or say 'hello'."]
    ]
]
chatbot = Chat(pairs, reflections)
# Endpoint for chatting with the bot
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = chatbot.respond(user_message)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)



     








     






