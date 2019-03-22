import os
from cryptography.fernet import Fernet

def encrypt(filename):
    #Get the key from the file
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()

    #Open the file to encrypt
    with open(filename, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    #Write the encrypted file
    with open(filename, 'wb') as f:
        f.write(encrypted)

def decrypt():
    #Get the key from the file
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()

    #Open the file to decrypt
    with open('Third.docx', 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    #Write the encrypted file
    with open('Third.docx', 'wb') as f:
        f.write(encrypted)


def Main():

    for fileNames in os.listdir('./'):
        if not os.path.isfile('key.key'):
            key = Fernet.generate_key()
            file = open('key.key', 'wb')
            key = file.write(key) # The key will be type bytes
            file.close()


    for filename in os.listdir('./'):
        if filename.endswith('.docx'):
            #Call method to encrypt all .txt files
            encrypt(filename)
            print("Done.")

#    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    #if choice == 'E':


#    elif choice == 'D':
#        decrypt()


if __name__ == '__main__':
	Main()
