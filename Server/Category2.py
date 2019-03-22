#Get the file size through os
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
	#chunks read from file
	chunksize = 64*1024
	#Create a new file with this new name
	outputFile = "(encrypted)"+filename
	#Get the size of the file
	filesize = str(os.path.getsize(filename)).zfill(16)

	#Randomize and produce distinct cihertext's for certain cipher modes
	IV = Random.new().read(16)

	#Creating the cipher with chain clocker mode
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	#open file to read
	with open(filename, 'rb') as infile:
		#Open file to write
		with open(filename, 'wb') as outfile:
			#Writing the file size to bytes
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				#Read all data from the file
				chunk = infile.read(chunksize)
				#Check if there is any data left in the file
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					#Padding
					chunk += b' ' * (16 - (len(chunk) % 16))
				#Writing encryption to new file
				outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
	chunksize = 64*1024


	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'wb') as outfile:
		while True:
			chunk = infile.read(chunksize)

			if len(chunk) == 0:
				break

			outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

def Main():

	choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")

	if choice == 'E':
		password = input("Password: ")

		#Search through currernt directory to check for .txt files
		for filename in os.listdir('.'):
			if filename.endswith('.docx'):
				#Call method to encrypt all .txt files
				encrypt(getKey(password), filename)
				print("Done.")

	elif choice == 'D':
		password = input("Password: ")

		for filename in os.listdir('.'):
			if filename.endswith('.docx'):
				#Call method to decrypt all .txt files
				decrypt(getKey(password), filename)
				print("Done.")
	else:
		print("No Option selected, closing...")

if __name__ == '__main__':
	Main()
