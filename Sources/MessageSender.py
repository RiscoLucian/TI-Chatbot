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
        #self.sendCarousel(psid, "te432xt", "quickReplies")

    def send3QuickReplies(self, psid, text, message):
        self.sendPersistentMenu(psid)
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

    def sendCarousel(self, psid, text, message):
        data = {
            "recipient": {
                "id": psid
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Audi A6",
                                "image_url": "https://cdn.pixabay.com/photo/2016/12/07/21/50/audi-1890494_1280.jpg",
                                "subtitle": "Cel mai nou model de la Audi A6",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://autoblog.md/foto-premiera-noul-sedan-plug-in-hybrid-audi-a6-55-tfsi-e-quattro/",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://autoblog.md/foto-premiera-noul-sedan-plug-in-hybrid-audi-a6-55-tfsi-e-quattro/",
                                        "title": "View Website"
                                    }
                                ]
                            },
                            {
                                "title": "Audi A6",
                                "image_url": "https://cdn.pixabay.com/photo/2016/12/07/21/50/audi-1890494_1280.jpg",
                                "subtitle": "Cel mai nou model de la Audi A6",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://autoblog.md/foto-premiera-noul-sedan-plug-in-hybrid-audi-a6-55-tfsi-e-quattro/",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://autoblog.md/foto-premiera-noul-sedan-plug-in-hybrid-audi-a6-55-tfsi-e-quattro/",
                                        "title": "View Website"
                                    }
                                ]
                            }
                        ]
                    }
                    }
                }
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def sendActionTypingOn(self, psid):
        """
        This method doesn't work because fb API throws exception:
        "error":{"message":"(#10) Aceast\\u0103 ac\\u0163iune nu a fost trimis\\u0103 din cauza noilor reguli din Europa
        privind confiden\\u0163ialitatea. Pentru mai multe informa\\u0163ii, consult\\u0103 documenta\\u0163ia dezvoltatorului.
        :param psid:
        :return:
        """
        data = {
            "recipient": {
                "id": psid
            },
            "sender_action": "typing_on",
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def sendActionTypingOff(self, psid):
        """
        This method doesn't work because fb API throws exception:
        "error":{"message":"(#10) Aceast\\u0103 ac\\u0163iune nu a fost trimis\\u0103 din cauza noilor reguli din Europa
        privind confiden\\u0163ialitatea. Pentru mai multe informa\\u0163ii, consult\\u0103 documenta\\u0163ia dezvoltatorului.
        :param psid:
        :return:
        """
        data = {
            "recipient": {
                "id": psid
            },
            "sender_action": "typing_on",
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def sendPersistentMenu(self, psid):
        print("alin was here")
        data = {
            'recipient': json.dumps({
                'id': psid
            }),
            "persistent_menu": [
                {
                    "locale": "default",
                    "composer_input_disabled": "false",
                    "call_to_actions": [
                        {
                            "type": "postback",
                            "title": "Talk to an agent",
                            "payload": "CARE_HELP"
                        },
                        {
                            "type": "postback",
                            "title": "Outfit suggestions",
                            "payload": "CURATION"
                        },
                        {
                            "type": "web_url",
                            "title": "Shop now",
                            "url": "https://www.originalcoastclothing.com/",
                            "webview_height_ratio": "full"
                        }
                    ]
                }
            ]
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)