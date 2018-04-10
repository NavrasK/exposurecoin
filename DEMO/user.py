import rsa

class User():
    def __init__(self):
        pk, sk = rsa.newkeys(512)  # 512 is the size of keys, docs said 512 for sha256

def newUser(uID):
    
    return pk, sk