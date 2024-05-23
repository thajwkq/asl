from time import sleep
from telethon import TelegramClient, sync
import sqlite3
import os
import requests


session_name = '20663523'
c = requests.session()
api_id = '9278263'
api_hash = 'f75fe6157dd68bdf0df5198adbc590fd'
client = TelegramClient('sessions/' + session_name, api_id, api_hash)
client.start()
sleep(20)
me = client.get_me()
id = (str)(me.id)
full_name = (me.first_name or "") + " " + (me.last_name or "")
client.disconnect()

db = sqlite3.connect('Tupac.db')
cur = db.cursor()
cur.execute("INSERT INTO users VALUES ('" + id + "','" + full_name + "')")
db.commit()

os.rename('sessions/' + session_name + '.session',
          'sessions/' +     id       + '.session')
