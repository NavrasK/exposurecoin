# Handles storing and retrieving data from pastebin

# TODO: Build pastebin data reader and properly store generated URLs

# Note that the current test generates a new paste every time this is run

from pastebin import PasteBin as pbAPI
import yaml
from networking_ import Network

class Server():
    def __init__(self, url):
        self.net = Network()
        self.URL = url
        self.extension = {}

    def get_pastebin_username(self):
        with open("credentials.yaml", "r") as file:
            data = yaml.load(file)
        pb = data.get('pastebin')
        uname = pb.get('username')
        return uname

    def get_pastebin_password(self):
        with open("credentials.yaml", "r") as file:
            data = yaml.load(file)
        pb = data.get('pastebin')
        pword = pb.get('password')
        return pword

    def get_pastebin_dev_key(self):
        with open("credentials.yaml", "r") as file:
            data = yaml.load(file)
        pb = data.get('pastebin')
        API_key = pb.get('pastebin_dev_api')
        return API_key

    def get_pastebin_user_key(self, dev_key, uname, pword):
        api = pbAPI(dev_key)
        user_key = api.create_user_key(uname,pword)
        if 'Bad API request' not in user_key:
            return user_key
        else:
            raise ValueError("INVALID PASTEBIN CREDENTIALS")

    def create_api(self, uname, pword):
        dev_key = self.get_pastebin_dev_key()
        user_key = self.get_pastebin_user_key(dev_key, uname, pword)
        api = pbAPI(dev_key, user_key)
        return api

    def create_paste(self, api, filename, title, filetype):
        data = ''
        with open(filename) as file:
            data = file.read()
        newURL = api.paste(data, guest=True, name=title, format=None, private=1, expire=None)
        self.extension[filetype] = str(newURL).replace(self.URL, "")
        return newURL

    def read_paste(self, api, ext):
        print('fuckoffS')

if __name__ == "__main__":
    s = Server("https://pastebin.com/")
    uname = s.get_pastebin_username()
    if not uname:
            uname = input("Enter your username:")
            uname = uname.rstrip()
    pword = s.get_pastebin_password()
    if not pword:
            pword = input("Enter your password:")
            pword = pword.rstrip()
    api = s.create_api(uname, pword)
    print(s.create_paste(api, "test.txt","TESTINGTESTING123", "test"))
    print("ext:" + s.extension["test"])
