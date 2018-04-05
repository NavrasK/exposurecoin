from pastebin import PasteBin as pbapi
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
        api = pbapi(dev_key)
        user_key = api.create_user_key(uname,pword)
        return user_key

if __name__ == "__main__":
    uname = input()
    pword = input()
    s = Server()
    dkey = s.get_pastebin_dev_key()
    ukey = s.get_pastebin_user_key(dkey, uname, pword)
    print(dkey)
    print(ukey)
