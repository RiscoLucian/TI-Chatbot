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

        if message == "Ok, in cazul in care va razganditi puteti cere informatii oricand prin accesarea intrebariilor predefinite accesand butonul 'Modele masini'. Va multumim!":
            self.sendGif(psid)

    def sendEmoticon(self, psid, message, messaging_type="RESPONSE"):
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
            'message': {'text': "😁"}
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

    def sendGif(self, psid):
        data = {
            'recipient': {
                'id': psid
            },
            'message': {
                'attachment': {
                    'type': 'image',
                    'payload': {
                        "url": "https://j.gifs.com/98OvjJ.gif"
                    }
                }
            },
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken,
                                        data=json.dumps(data))
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

    def send8QuickReplies(self, psid, text, message):
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
                    },
                    {
                        "content_type": "text",
                        "title": message[1],
                        "payload": message[1],
                    },
                    {
                        "content_type": "text",
                        "title": message[2],
                        "payload": message[2],
                    },
                    {
                        "content_type": "text",
                        "title": message[3],
                        "payload": message[3],
                    },
                    {
                        "content_type": "text",
                        "title": message[4],
                        "payload": message[4],
                    },
                    {
                        "content_type": "text",
                        "title": message[5],
                        "payload": message[5],
                    },
                    {
                        "content_type": "text",
                        "title": message[6],
                        "payload": message[6],
                    },
                    {
                        "content_type": "text",
                        "title": message[7],
                        "payload": message[7],
                    }
                ]
            }
        }

        contentType = {'Content-Type': 'application/json'}

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)

    def sendCarousel(self, psid, title, image_url, subtitle, website_url):
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
                                "title": title[0],
                                "image_url": image_url[0],
                                "subtitle": subtitle[0],
                                "default_action": {
                                    "type": "web_url",
                                    "url": image_url[0],
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": website_url,
                                        "title": "Acceseaza website"
                                    }
                                ]
                            },
                            {
                                "title": title[1],
                                "image_url": image_url[1],
                                "subtitle": subtitle[1],
                                "default_action": {
                                    "type": "web_url",
                                    "url": image_url[1],
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": website_url,
                                        "title": "Acceseaza website"
                                    }
                                ]
                            },
                            {
                                "title": title[2],
                                "image_url": image_url[2],
                                "subtitle": subtitle[2],
                                "default_action": {
                                    "type": "web_url",
                                    "url": image_url[2],
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": website_url,
                                        "title": "Acceseaza website"
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

    def sendList(self, psid):
        """
        This method doesn't work because fb API throws exception:
        "error":{"message":"(#100) List template on Messenger Platform is deprecated on API 4.0. It will be removed from all versions soon."
        :param psid:
        :return:
        """
        contentType = {'Content-Type': 'application/json'}

        data = {
            'recipient': {'id': psid},
              "message": {
                    "attachment": {
                      "type": "template",
                      "payload": {
                        "template_type": "list",
                        "top_element_style": "compact",
                        "elements": [
                            {
                                "title": "Classic T-Shirt Collection",
                                "subtitle": "See all our colors",
                                "buttons": [
                                    {
                                        "title": "View",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=100",
                                        "messenger_extensions": "false",
                                        "webview_height_ratio": "tall",
                                    }
                                ]
                            },
                            {
                                "title": "Classic T-Shirt Collection",
                                "subtitle": "See all our colors",
                                "buttons": [
                                    {
                                        "title": "View",
                                        "type": "web_url",
                                        "url": "https://peterssendreceiveapp.ngrok.io/view?item=100",
                                        "messenger_extensions": "false",
                                        "webview_height_ratio": "tall",
                                    }
                                ]
                            }
                        ],
                         "buttons": [
                          {
                            "title": "View More",
                            "type": "postback",
                            "payload": "payload"
                          }
                        ]
                      }
                    }
            }
        }

        pageAccessToken = {'access_token': self.accessToken}
        messageResponse = requests.post(self.facebookGraphURL, headers=contentType, params=pageAccessToken, data=json.dumps(data))
        print(messageResponse.content)
        self.sendGif(psid)


    def sendMapDealership(self, psid):
        data = {
            'recipient': {'id': psid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Audi Timisoara",
                                "image_url": "https://im7.ezgif.com/tmp/ezgif-7-5c72304fdc6a.png",
                                "subtitle": "Reprezentata Audi Timisoara",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://www.google.com/maps/place/Porsche+Timisoara+-+dealer+Audi+si+Skoda/@45.7761406,21.3111878,15z/data=!4m5!3m4!1s0x474560d63a50b5e9:0x51309b7524374593!8m2!3d45.7766074!4d21.3141784",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.google.com/maps/place/Porsche+Timisoara+-+dealer+Audi+si+Skoda/@45.7761406,21.3111878,15z/data=!4m5!3m4!1s0x474560d63a50b5e9:0x51309b7524374593!8m2!3d45.7766074!4d21.3141784",
                                        "title": "Vezi harta"
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