from pastebin import PasteBin
import yaml

class Server():
    def __init__(self):
        url1 = "idk"
    def get_pastebin_dev_key(self):
        with open("credentials.yaml", "r") as file:
            data = yaml.load(file)
        keys = data.get('keys')
        id = keys.get('pastebin_dev_api')
        return id
    