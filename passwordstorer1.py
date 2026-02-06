import hashlib
import os

print('Welcome to the Password SafeKeeper')


username = input("Username: ")


salt = os.urandom(32)

FirstPassword = input("Password: ")

MiddlePassword = hashlib.sha256(FirstPassword.encode('utf-8') + salt)
FinalPassword = MiddlePassword.hexdigest()


with open ('passwords.txt', 'a') as f:
    f.write(f'{username} : {FinalPassword}\n')
