import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tsvn = STRING27
ttit = STRING28
tnn = STRING29
trt = STRING30
tro = STRING31

idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
ni = ""
shi = ""
non = ""
rooted = ""
raj = ""
put = ""
qwe = ""
wer = ""
ert = ""
rty = ""
tyu = ""
yui = ""

que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_mayank():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global ni
    global shi
    global non
    global rooted
    global raj
    global put
    global qwe
    global wer
    global ert
    global rty
    global tyu
    global yui
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await idk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await ydk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await wdk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await hdk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await sdk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await adk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await bdk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await cdk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await ddk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await edk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await vkk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await kkk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            await lkk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await mkk(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await sid(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await shy(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            await aan(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await ake(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await eel(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        ni = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await ni.start()
            botme = await ni.get_me()
            await ni(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await ni(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        ni = TelegramClient(session_name, a, b)
        try:
            await ni.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await shi(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        non = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await non.start()
            botme = await non.get_me()
            await non(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await non(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        non = TelegramClient(session_name, a, b)
        try:
            await non.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        rooted = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await rooted.start()
            botme = await rooted.get_me()
            await rooted(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await rooted(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        rooted = TelegramClient(session_name, a, b)
        try:
            await rooted.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await raj(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            await put(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass

if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        qwe = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await qwe.start()
            botme = await raj.get_me()
            await qwe(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await qwe(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        qwe = TelegramClient(session_name, a, b)
        try:
            await qwe.start()
        except Exception as e:
            pass

if tsvn:
        session_name = str(tsvn)
        print("String 27 Found")
        wer = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await wer.start()
            botme = await wer.get_me()
            await wer(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await wer(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        wer = TelegramClient(session_name, a, b)
        try:
            await wer.start()
        except Exception as e:
            pass

if ttit:
        session_name = str(ttit)
        print("String 28 Found")
        ert = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await ert.start()
            botme = await ert.get_me()
            await ert(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await ert(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        session_name = "startup"
        ert = TelegramClient(session_name, a, b)
        try:
            await ert.start()
        except Exception as e:
            pass

if tnn:
        session_name = str(tnn)
        print("String 29 Found")
        rty = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await rty.start()
            botme = await rty.get_me()
            await rty(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await rty(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        session_name = "startup"
        rty = TelegramClient(session_name, a, b)
        try:
            await rty.start()
        except Exception as e:
            pass

if trt:
        session_name = str(trt)
        print("String 30 Found")
        tyu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await tyu.start()
            botme = await tyu.get_me()
            await tyu(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await tyu(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        session_name = "startup"
        tyu = TelegramClient(session_name, a, b)
        try:
            await tyu.start()
        except Exception as e:
            pass

if tro:
        session_name = str(tro)
        print("String 31 Found")
        yui = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await yui.start()
            botme = await raj.get_me()
            await yui(functions.channels.JoinChannelRequest(channel="@hackelite01"))
            await yui(functions.channels.JoinChannelRequest(channel="@MarcusUserbot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "startup"
        yui = TelegramClient(session_name, a, b)
        try:
            await yui.start()
        except Exception as e:
            pass


   
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_mayank())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "Module Name = Bio\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(mayank[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio By NonRooted Spam Bot")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "Module Name = Join\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = mayank[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("JOIN KARDIYA BOSS")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "Module Name = Private Join\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SMEX_USERS:
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mayank[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("JOIN KARDIYA BOSS")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
async def _(e):
    usage = "Module Name = Leave\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        mayank = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = mayank[0]
            bc = int(bc)
            text = "NonRooted Spam Bot Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                

@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.leave"))

async def _(e):
    usage = "Module Name = Leave\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = mayank[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "Module Name = Spam\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(mayank) == 2:
            message = str(mayank[1])
            counter = int(mayank[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(mayank[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(mayank[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))

async def spam(e):
    usage = "Module Name = Delayspam\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        mayank = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        mayankop = mayank[1:]
        if len(mayankop) == 2:
            message = str(mayankop[1])
            counter = int(mayankop[0])
            sleeptime = float(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(mayankop[0])
            sleeptime = float(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(mayankop[0])
            sleeptime = float(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))


async def spam(e):
    usage = "Module Name = BigSpam\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(mayank) == 2:
            message = str(mayank[1])
            counter = int(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(mayank[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

async def spam(e):
    usage = "Module Name = Raid\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(mayank) == 2:
            message = str(mayank[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(mayank[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mayank[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@ni.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@non.on(events.NewMessage(incoming=True))
@rooted.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@qwe.on(events.NewMessage(incoming=True))
@wer.on(events.NewMessage(incoming=True))
@ert.on(events.NewMessage(incoming=True))
@rty.on(events.NewMessage(incoming=True))
@tyu.on(events.NewMessage(incoming=True))
@yui.on(events.NewMessage(incoming=True))



async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))


async def _(e):
    global que
    usage = "Module Name = ReplyRaid\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(mayank[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))


async def _(e):
    global que
    usage = "Module Name = DeActivate ReplyRaid\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mayank = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(mayank[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "PONG!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"✦ Pong!
★ {ms}

⋤ ⋥ 𝙽𝚘𝚗𝚁𝚘𝚘𝚝𝚎𝚍 𝚂𝙿𝙰𝙼𝙱𝙾𝚃 ⋤ ⋥
")


    
        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.restart"))

async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "RESTARTED\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ni.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@non.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@rooted.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@qwe.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wer.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ert.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@rty.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@tyu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yui.on(events.NewMessage(incoming=True, pattern=r"\.help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "❂ AVAILABLE COMMANDS IN NonRooted SpamBot \n\n回 UTILS COMMANDS:\n.ping\n.restart\n\n回 USERBOT COMMANDS:\n.bio\n.join\n.leave\n.pjoin\n.pleave\n\n回 SPAM COMMANDS:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """

   _  __          ___            __         __
  / |/ /__  ___  / _ \___  ___  / /____ ___/ /
 /    / _ \/ _ \/ , _/ _ \/ _ \/ __/ -_) _  / 
/_/|_/\___/_//_/_/|_|\___/\___/\__/\__/\_,_/  
                                              
              
"""

print(text)
print("")
print("SMEX! NonRooted Spam Bot Started Sucessfully.")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        ni.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        non.disconnect()
    except Exception as e:
        pass
    try:
        rooted.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        qwe.disconnect()
    except Exception as e:
        pass
    try:
        wer.disconnect()
    except Exception as e:
        pass
    try:
        ert.disconnect()
    except Exception as e:
        pass
    try:
        rty.disconnect()
    except Exception as e:
        pass
    try:
        tyu.disconnect()
    except Exception as e:
        pass
    try:
        yui.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ni.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        non.run_until_disconnected()
    except Exception as e:
        pass
    try:
        rooted.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        qwe.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wer.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ert.run_until_disconnected()
    except Exception as e:
        pass
    try:
        rty.run_until_disconnected()
    except Exception as e:
        pass
    try:
        tyu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yui.run_until_disconnected()
    except Exception as e:
        pass
