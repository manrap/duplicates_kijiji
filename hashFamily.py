import hashlib

def hashFamily(i):
    resultSize = 8 # how many bytes we want back
    maxLen = 20 # how long can our i be (in decimal)
    salt = str(i).zfill(maxLen)[-maxLen:]

    def hashMember(x):
        return hashlib.sha1(x + salt).digest()[-resultSize:]

    return hashMember
