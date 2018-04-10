import rsa

def newUser(uID):
    pk, sk = rsa.newkeys(512)  # 512 is the size of keys, docs said 512 for sha256
    return pk, sk