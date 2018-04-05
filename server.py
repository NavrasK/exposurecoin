from pastebin import PasteBin as pbAPI
import yaml

URL = None
extension = None

class Server():
    def __init__(self, url):
        URL = url

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
        data = open(filename).read()
        newURL = api.paste(data, guest=True, name=title, format=None, private=1, expire=None)
        return newURL

if __name__ == "__main__":
    s = Server("https://www.pastebin.com/")
    uname = s.get_pastebin_username()
    if not uname:
            uname = input("Enter your username:")
            uname = uname.rstrip()
    pword = s.get_pastebin_password()
    if not pword:
            pword = input("Enter your password:")
            pword = pword.rstrip()
    api = s.create_api(uname, pword)
    print(s.create_paste(api, "test.txt","TESTINGTESTING123"))
