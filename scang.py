#!/usr/bin/env python3
from os import _exit
try:
    import amino
except:
    print ("\nno internet\n\nplease login network for run")
    _exit(1)
from getpass import getpass
from time import sleep
first='‎‏'
last=' ‌‬‭'
c=amino.Client()
ff=False
while ff==False:
    url=input("url group : ")
    try:
        urll=amino.Client().get_from_code(url)
        chatId=urll.objectId
        comId=urll.path[1:str(urll.path).index("/")]
        ff=True
    except:
        ff=False
        if input("to be continue ? : y/n : ")=="n":
            _exit(1)
# ce1ae0d634@firemailbox.club 
# password
zz=False
while zz==False:
    q=input("login with email or sid ?\n\n    if email type : e\n     if sid type : s \n\n choose one : ")
    if q=="e":
        zz=True
        ff=False
        while ff==False:
            try:
                c.login(input("email = "),getpass("password = "))
                ff=True
            except:
                ff=False
                if input("to be continue ? : y/n : ")=="n":
                    _exit(1)
    elif q=="s":
        zz=True
        ff=False
        while ff==False:
            try:
                c.login_sid(SID=input("sid = "))
                ff=True
            except:
                ff=False
                if input("to be continue ? : y/n : ")=="n":
                    _exit(1)
    else:
        zz=False
sub=amino.SubClient(comId,profile=c.profile)

while True:
    print("scaning ..")
    listo=sub.get_chat_messages(chatId)
    for userId,ref,name in zip(listo.author.userId,listo.clientRefId,listo.author.nickname):
        if ref>=2147483648 or ref<=-2147483649:
            
            try:
                sub.kick(userId=userId,chatId=chatId,allowRejoin=False)
            except:
                pass
            
            imposter=first+"@"+name+last
            message="حاول "+imposter+" تفليش القروب برسالة القليتش لكن تم القبض عليه "
            print("imposter is ",name,"\nuser= ",userId)
            print("\n\nrepair the chat ...")
            try:
                sub.send_message(chatId, message="تنضيف الشات ب 25 رسالة  ")
            except:
                pass
            for i in range(0,25):
                try:
                    sub.send_message(chatId, message="تنضيف الشات رسالة رقم "+str(i+1))
                except:
                    pass
            try:
                sub.send_message(chatId, message=message,mentionUserIds=[userId])
            except:
                pass
            """
            try:
                sub.delete_message(chatId,messageId=messageId)
            except:
                pass
ملاحظة : حذف الرسالة لا يعني ازالة القليتش , حتى ولو انحذفت الرسالة ماراح ياثر             

            """
            break
    sleep(5)
        
