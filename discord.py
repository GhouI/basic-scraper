import requests
class DiscordHook:
    def __init__(self, url):
        self.url = url

    def send_Message(self, message):
        data = {
            "content": message,
        }
        result = requests.post(self.url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Website content has changed. Notification sent to Discord.")
        
        

