from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('key.key', 'wb')
key = file.write(key) # The key will be type bytes
file.close()
