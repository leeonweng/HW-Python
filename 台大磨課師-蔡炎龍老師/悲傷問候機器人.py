# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:16:35 2019

@author: Home love
"""

message=""
while True:
    message = input("怎麼了?\n>>")
    P = ('過來我拍拍!')
    O = ('過來我秀秀!')
    H = ('過來我抱一下!')
    PP = ('拍拍不難過了')
    E = ('一切都會變好的!')
    A = ('有任何的不愉快歡迎你再來!bye bye')
    if ("悲傷" in message):
        print(P)
    elif("難受" in message):
        print(O)
    elif("想哭" in message):
        print(H)
    elif("難過" in message):
        print(PP)
    elif("痛苦" in message):
        print(E)
    elif("心碎" in message):
        print(E)
    elif("再見" in message):
         print(A)
         break
    elif("BYE" in message):
         print(A)
         break
    elif("掰" in message):
         print(A)
         break
    elif("Bye" in message):
         print(A)
         break
    elif("bye" in message):
         print(A)
         break
    else:
        print("祝你愉快~")