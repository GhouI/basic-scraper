import requests
import random
import string

class DiscordHook:
    def __init__(self, url):
        self.url = url

    def send_Message(self, message):

        # Generate random hex number
        random_hex = ''.join(random.choices(string.hexdigits, k=6))

        data = {
            "embeds": [
                {
                    "title": "Maybe new update",
                    "fields": [
                        {
                            "name": f"update {random_hex}",
                            "value": message
                        }
                    ]
                }
            ]
        }

        result = requests.post(self.url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Sent Discord WebHook successfully!")
                
        

