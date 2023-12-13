import hashlib

passwd = "asies"
hashpassword = hashlib.sha256(passwd.encode()).hexdigest()
print(hashpassword)