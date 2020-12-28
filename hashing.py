import hashlib


def shake_128(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.shake_128(password).hexdigest()
    return cracked_pw_h

def sha3_224(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha3_224(password).hexdigest()
    return cracked_pw_h

def sha224(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha224(password).hexdigest()
    return cracked_pw_h

def sha3_256(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha3_256(password).hexdigest()
    return cracked_pw_h

def sha256(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha256(password).hexdigest()
    return cracked_pw_h

def sha384(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha384(password).hexdigest()
    return cracked_pw_h

def blake2s(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.blake2s(password).hexdigest()
    return cracked_pw_h

def sha1(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha1(password).hexdigest()
    return cracked_pw_h

def blake2b(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.blake2b(password).hexdigest()
    return cracked_pw_h

def sha512(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha512(password).hexdigest()
    return cracked_pw_h

def sha3_512(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha3_512(password).hexdigest()
    return cracked_pw_h

def shake_256(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.shake_256(password).hexdigest()
    return cracked_pw_h

def md5(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.md5(password).hexdigest()
    return cracked_pw_h

def sha3_384(password):
    password = password.encode('utf-8')
    cracked_pw_h = hashlib.sha3_384(password).hexdigest()
    return cracked_pw_h
