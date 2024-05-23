import random
import re
import requests
from time import sleep
import sqlite3
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import ChannelsTooMuchError
from telethon import TelegramClient, sync
from threading import Thread
import asyncio

db = sqlite3.connect('Tupac.db')
cur = db.cursor()
c = requests.session()
api_id = '9278263'
api_hash = 'f75fe6157dd68bdf0df5198adbc590fd'
amr1= 'ارسل معرف البوت الان دون @ : '
amr2='تم بداء تجميع حساب : '
channel_username = input(amr1)
amr = '@' + channel_username
def startUser(user):
    print(amr2 + user[0])
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient('sessions/' + user[0], api_id, api_hash, loop=loop)
    client.start()
    channel_entity = client.get_entity(channel_username)
    sleep(1)
    client.send_message(amr, '/start')
    sleep(2)
    mssag = client.get_messages(amrakl, limit=1)
    mssag[0].click(2)
    sleep(2)
    mssag1 = client.get_messages(amrakl, limit=1)
    mssag1[0].click(0)
    sleep(2)
    for x in range(17):
        l = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None,
                                 offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        sleep(2)
        j = l.messages[0]
        if j.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            client.send_message('me', 'تم انهاء القنوات')
            client.disconnect()
            sleep(2)
            return
        if (j.reply_markup == None):
            client.send_message('me', 'حدث خطاء ما')
            client.disconnect()
            sleep(2)
            return
        url = j.reply_markup.rows[0].buttons[0].url
        try:
            try:
               client(JoinChannelRequest(url))
            except ChannelsTooMuchError:
                # TODO remove all cahnnels
                client.send_message('me', 'الحساب قام بلاشتراك باكثر من 500 قناة')
                client.disconnect()
                sleep(2)
                return
            except:
                bott = url.split('/')[-1]
                client(ImportChatInviteRequest(bott))
            mssag2 = client.get_messages(amrakl, limit=1)
            mssag2[0].click(text='تحقق')
            sleep(5)
        except:
            client.send_message('me', 'مشكلة في دخول الجروب')
            print(url)
            break
    client.disconnect()
    return


while(True):
    users = cur.execute("SELECT * FROM users;")
    threadlist = []
    for user in users.fetchall():
        threadlist.append(Thread(target=startUser, args=(user,), daemon=False))
        
    for t in threadlist:
        t.start()

    for t in threadlist:
        t.join()
    sleep(random.randint(100,300))

