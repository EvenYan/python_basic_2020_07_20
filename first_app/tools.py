import hashlib


def gen_passwd(passwd):
    sha1 = hashlib.sha512()
    sha1.update(passwd.encode())
    return sha1.hexdigest()