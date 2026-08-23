import time
import pyttsx3
mt_dict={}
v=pyttsx3.init()
v.say("HELLO,SIR HOW ARE YOU , HOPE YOU WILL BE FINE")
v.runAndWait()

count=int(input("how many friends you have::- "))
for i in range(1,count+1):
    add=input("ENTER THE NAME OF YOUR 1ST FRIEND::- ")
    lan=input("ENTER THE NAME OF HIS PROFFICENCY LANGUAGE::- ")
    mt_dict.update({add:lan})
for name,lan in mt_dict.items():
    print(f"{name.upper()} has proffeciency in {lan.upper()}")
time.sleep(1)
v.say("THANKS FOR USING OUR SITE")
v.runAndWait()
v.stop()