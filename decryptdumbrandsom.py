import os 
from cryptography.fernet import Fernet 

allfiles = os.listdir()
files = []
for file in allfiles:
	if file != "dumbransome.py" and file != "decryptdumbrandsom.py" and file!="key.key":
		files.append(file)

with open("key.key","rb") as k:
	key=k.read() 
	
def encryptFiles():
	decryptedData = []
	fernet = Fernet(key)
	for file in files:
		with open(file,"rb") as file1:
			data = file1.read()
		decryptedData.append(fernet.decrypt(data))
	for file in range(len(files)):
		with open(files[file],"wb") as file2:
			file2.write(decryptedData[file])

encryptFiles()
print(f"Decrypted all files")