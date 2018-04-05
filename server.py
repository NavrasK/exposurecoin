from pastebin import PasteBin as pbAPI
import yaml

class Server():
    def __init__(self):
        url1 = "idk"

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
    s = Server()
    uname = input("username:")
    pword = input("password:")
    api = s.create_api(uname, pword)
    print(s.create_paste(api, "test.txt","TESTINGTESTING123"))
