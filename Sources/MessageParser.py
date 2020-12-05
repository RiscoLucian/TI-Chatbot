from DataContainer import *

class MessageParser:
    def __init__(self):
        self.psid = 0
        self.message = ""
        self.payload = ""

    def parseData(self, messaging):
        retVal = False
        messaging = messaging[0]
        try:
            self.psid = messaging['sender']['id']
        except Exception:
            print("Couldn't parse the user ID!")

        for key, value in messaging.items():
            if key == 'message':
                try:
                    self.message = value['text']
                    retVal = True
                except Exception:
                    print("Couldn't correctly parse the data!")
            elif key == 'postback':
                try:
                    self.message = value['title']
                    self.payload = value['payload']
                    retVal = True
                except Exception:
                    print("Couldn't correctly parse the data!")
            else:
                pass

        return retVal

    def getMessageType(self):
        if self.payload != "":
            return "postback"
        elif self.payload == "" and self.message != "":
            return "text"
        else:
            return ""

    def getResponse(self):
        messageType = self.getMessageType()
        if "postback" == messageType or "text" == messageType:
            # search the message in the ResponseContainer
            for key, value in dataContainer.items():
                if self.message == key:
                    print(value)
                    if type(value) is dict:
                        for k, v in value.items():
                            if k == " . Cu ce va mai pot ajuta?":
                                # get data from database, fill the empty dict and then return the entire dict
                                pass
                    return value
        else:
            # other data type -> probably an attachment
            # not used for the moment
            return 0
            pass
