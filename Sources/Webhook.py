from flask import Flask, request
import json
from ConfigurationFile import *
from ChatBot import ChatBot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == webhookToken:
            return challenge
    else:
        chatBot = ChatBot(accessToken, facebookGraphURL)
        data = json.loads(request.data)
        messaging = data['entry'][0]['messaging']
        chatBot.run(messaging)
        return '200'    # otherwise Flask will return errors