# Handles storing and retrieving data from pastebin

# TODO: Build pastebin data reader and properly store generated URLs

# Note that the current test generates a new paste every time this is run

from pastebin import PasteBin as pbAPI
from networking_ import Network
import yaml
import urllib

class PastebinHandler():
    def __init__(self):
        self.net = Network()
        self.URL = "https://pastebin.com/"
        self.raw = "https://pastebin.com/raw/"
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
        with open(filename, 'r') as file:
            data = file.read()
        newURL = api.paste(data, guest=True, name=title, format=None, private=1, expire=None)
        self.extension[filetype] = str(newURL).replace(self.URL, "")
        return newURL

    def read_paste(self, filetype): #raw address giving HTML not TXT
        #ext = self.extension[filetype]
        ext = "ecYsn5zd"
        data = urllib.request.urlopen(self.raw + ext)
        data = str(data.encode())
        with open("readintest.txt", 'w+') as file:
            file.truncate(0)
            for line in data:
                file.write(str(line.rstrip().decode()))
        return data

if __name__ == "__main__":
    pbh = PastebinHandler()
    uname = pbh.get_pastebin_username()
    if not uname:
            uname = input("Enter your username:")
            uname = uname.rstrip()
    pword = pbh.get_pastebin_password()
    if not pword:
            pword = input("Enter your password:")
            pword = pword.rstrip()
    api = pbh.create_api(uname, pword)
    # print(s.create_paste(api, "test.txt","TESTINGTESTING123", "test"))
    # print("ext:" + s.extension["test"])
    print("read:" + pbh.read_paste("test"))
