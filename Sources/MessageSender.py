import requests
import json
import os
from requests_toolbelt import MultipartEncoder


class MessageSender:
    def __init__(self, accessToken, facebookGraphURL):
        self.accessToken = accessToken
        self.facebookGraphURL = facebookGraphURL

    def sendText(self, psid, message, messaging_type="RESPONSE"):
        """ sendText
        Description:
            Sends a specific text back to user

        Parameters:
            psid: The ID of the sender/user
            message: The message sent to user
            messaging_type: message type (default: "RESPONSE")

        Returns:
            None.

        """
        contentType = {'Content-Type': 'application/json'}

        data = {
            'messaging_type': messaging_type,
            'recipient': {'id': psid},
            'message': {'text': message}
        }

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def sendImage(self, psid, image):
        data = {
            'recipient': json.dumps({
                'id': psid
            }),
            'message': json.dumps({
                'attachment': {
                    'type': 'image',
                    'payload': {}
                }
            }),
            'filedata': (os.path.basename(image), open(image, 'rb'), 'image/png')

        }

        multipart_data = MultipartEncoder(data)

        multipart_header = {
            'Content-Type': multipart_data.content_type
        }

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=multipart_header, params=pageAccessToken,
                                        data=multipart_data)
        print(messageResponse.content)

    def sendButton(self, psid, message):
        data = {
            'recipient': json.dumps({
                'id': psid
            }),
            'message': json.dumps({
                'attachment': {
                    'type': 'template',
                    'payload': {
                        'template_type': 'button',
                        'text': 'What do you want to do next?',
                        'buttons': [
                            {
                                'type': 'web_url',
                                'url': 'https://www.messenger.com',
                                'title': 'Visit Messenger'
                            }
                        ]
                    }
                }
            })
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=data)
        print(messageResponse.content)

    def send2QuickReplies(self, psid, text, message):
        data = {
            "recipient": {
                "id": psid
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": text,
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": message[0],
                        "payload": message[0],
                    }, {
                        "content_type": "text",
                        "title": message[1],
                        "payload": message[1],
                    }
                ]
            }
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def send3QuickReplies(self, psid, text, message):
        data = {
            "recipient": {
                "id": psid
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": text,
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": message[0],
                        "payload": message[0],
                    }, {
                        "content_type": "text",
                        "title": message[1],
                        "payload": message[1],
                    }, {
                        "content_type": "text",
                        "title": message[2],
                        "payload": message[2],
                    }
                ]
            }
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)