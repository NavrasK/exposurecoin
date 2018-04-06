# Handles storing and retrieving data from pastebin

# TODO: Build pastebin data reader and properly store generated URLs

# Note that the current test generates a new paste every time this is run

import yaml
import urllib
from pastebin import PasteBin as pbAPI
from pastebinparser import PasteFetcher

class PastebinHandler():
    def __init__(self):
        self.pasteparser = PasteFetcher()
        self.URL = "https://pastebin.com/"
        self.extension = {}
        self.read_backup()

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

    def create_paste(self, api, filename, title):
        if self.is_changed(api, filename):
            data = ''
            with open(filename, 'r') as file:
                data = file.read()
            newURL = api.paste(data, guest=True, name=title, format=None, private=1, expire=None)
            self.extension[filename] = str(newURL).replace(self.URL, "")
            return newURL
        else:
            return self.URL + self.extension[filename]

    def read_paste(self, api, filename):
        ext = self.extension[filename]
        data = self.pasteparser.parse_paste(ext)
        return data

    def is_changed(self, api, filename):
        oldData = self.read_paste(api, filename)
        newData = ''
        with open(filename, 'r') as file:
            newData = file.read()
        if oldData == newData:
            return False
        else:
            return True

    def update_backup(self):
        with open("bkup.txt", "w+") as file:
            file.truncate(0)
            for i in self.extension:
                file.write(i+':'+self.extension[i]+'\n')

    def read_backup(self):
        self.extension = {}
        with open("bkup.txt", "r") as file:
            for line in file:
                name, ext = line.split(':')
                self.extension[name] = ext

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
    print(pbh.create_paste(api, "test.txt","TESTING_TESTING_TESTING"))
    print("ext:" + pbh.extension["test.txt"])
    print("read:\n" + pbh.read_paste(api, "test.txt"))
    pbh.update_backup()
