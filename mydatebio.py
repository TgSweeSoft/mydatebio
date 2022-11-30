#GitHub: TgSweeSoft

from time import sleep
from time import strftime, gmtime
from pyrogram.raw import functions
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
from pyrogram import Client, filters, sync, idle, enums

import os
import time
import random
import asyncio
import datetime
import colorama
import pyrogram
os.system("clear")
app = Client('my', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()
os.system("clear")
app.stop()
print(" DAAD " * 10)


@app.on_message(filters.command("test", prefixes=".") & filters.me)
def test(app, message):
	while True:
	           		try:
	           			d1 = "2021/10/12"
	           			d2 = d1
	           			
	           			d3 = datetime.datetime.today()
	           			d4 = datetime.datetime.strptime(d1, '%Y/%m/%d')
	           			
	           			d5 = d3 - d4
	           			d6 = f'{d5}'
	           			
	           			d7 = d6.replace('days', 'Дней')
	           			d8 = d7[:18]
	           			d9 = d8.replace('.', '')
	           			
	           			app.update_profile(bio=d9)
	           		except FloodWait as e:
	           			sleep(e.x)
	           		
	           		sleep(1)
	
	
	
	
app.run()