from MessageSender import MessageSender
from MessageParser import MessageParser


class ChatBot(MessageParser, MessageSender):
    def __init__(self, accessToken, facebookGraphURL):
        MessageSender.__init__(self, accessToken, facebookGraphURL)
        MessageParser.__init__(self)

    def run(self, messaging):
        if self.parseData(messaging):
            responseMessage = self.getResponse()
            if type(responseMessage) is str:
                self.sendText(self.psid, responseMessage)
            elif type(responseMessage) is dict:
                text = ""
                quickReplies = []
                if len(responseMessage) == 1:
                    for key, value in responseMessage.items():
                        text = key
                        quickReplies.append(value)
                    quickReplies = quickReplies[0]
                    print(quickReplies)
                    if len(quickReplies) == 2:
                        self.send2QuickReplies(self.psid, text, quickReplies)
                    elif len(quickReplies) == 3:
                        self.send3QuickReplies(self.psid, text, quickReplies)
                elif len(responseMessage) == 2:
                    # check if the dict contains "images" tag/key
                    # a dump implementation due to irreversibility of the python dictionary!
                    try:
                        images = responseMessage["images"]
                        for image in images:
                            self.sendImage(self.psid, image)
                    except Exception:
                        self.sendText(self.psid, "Ne pare rau, dar se pare ca imaginile nu pot fi afisate, va rugam sa "
                                                 "reveniti mai tarziu. Multumim!")
                    for key, value in responseMessage.items():
                        if key != "images":
                            text = key
                            if len(value) == 0:
                                self.sendText(self.psid, text)
                                break
                            else:
                                quickReplies.append(value)
                            quickReplies = quickReplies[0]
                            print(quickReplies)
                            if len(quickReplies) == 2:
                                self.send2QuickReplies(self.psid, text, quickReplies)
                            elif len(quickReplies) == 3:
                                self.send3QuickReplies(self.psid, text, quickReplies)
            elif type(responseMessage) is int:
                # this is only for other data types -> skipped for the moment
                pass
        else:
            if self.psid:
                self.sendText(self.psid, "Nu am inteles mesajul tau. Foloseste mesajele predefinite.")
            else:
                print("Critical error! Couldn't parse de user ID! Further debug needed!")
