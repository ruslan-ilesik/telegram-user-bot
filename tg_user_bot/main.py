from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import pyfiglet
import time
from time import sleep
import random
from PIL import Image, ImageDraw, ImageFont
 
app = Client("my_account")
import ascii_image


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"
 
	while(tbp != orig_text):
	           try:
	           	msg.edit(tbp + typing_symbol)
	           	sleep(0.05) # 50 ms
	           	tbp = tbp + text[0]
	           	text = text[1:]
	           	msg.edit(tbp)
	           	sleep(0.05)
	           	
	           except FloodWait as e:
	           	sleep(e.x)
 

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
    message= msg.text.split(".hack ", maxsplit=1)[1]
    msg.edit("вышла ОшибОчка и было найдено что: "+ message)
 

@app.on_message(filters.command("timer", prefixes=".") & filters.me)
def timer(_, msg):
    text = msg.text.split(".timer ", maxsplit=1)[1]
    msg.edit("Сообщение будет видно через: 3")
    time.sleep(1)
    msg.edit("Сообщение будет видно через: 2")
    time.sleep(1)
    msg.edit("Сообщение будет видно через: 1")
    time.sleep(2)
    msg.edit(text)
    

@app.on_message(filters.command("img_to_sticker", prefixes=".") & filters.me)
def img_to_sticker(_, msg):
    app.download_media(msg,file_name = 'to_webp.jpg')
    chat_id = msg.chat.id
    msg.delete()
    im = Image.open('./downloads/to_webp.jpg').convert("RGB")
    im.save ('./downloads/to_webp.webp','webp')
    app.send_sticker(chat_id ,'./downloads/to_webp.webp')


@app.on_message(filters.command("text_to_ascii", prefixes=".") & filters.me)
def text_to_ascii(_, msg):
    content = ' '.join(list(msg.text.split('.text_to_ascii',maxsplit=1)[1])).replace('  ','     ')
    result = pyfiglet.figlet_format(content)
    chat_id = msg.chat.id
    
    msg.delete()
    font_size = 15
    s= len(list(content))
    img = Image.new('RGB', (int(16*font_size*2), int(max(2,s/6)*font_size*2)), color = (255,255,255))
    d = ImageDraw.Draw(img)
    d.text((0,0), result, fill=(0, 0, 0))
    img.save('./downloads/text_to_ascii.png')
    app.send_photo(chat_id ,'./downloads/text_to_ascii.png')

@app.on_message(filters.command("fuck", prefixes=".") & filters.me)
def fuck(_, msg):
    msg.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┗━┻━┻━┻┛┗━━━┛")


@app.on_message(filters.command("wtf", prefixes=".") & filters.me)
def wtf(_, msg):
    a ='.\n▒█░░▒█ ▀▀█▀▀ ▒█▀▀▀ \n▒█▒█▒█ ░▒█░░ ▒█▀▀▀ \n▒█▄▀▄█ ░▒█░░ ▒█░░░ '
    msg.edit(a)

@app.on_message(filters.command("ban", prefixes=".") & filters.me)
def ban(_, msg):
    a = '.\n████╗███╗█╗█╗\n█╔══╝█╔█║█║█║\n████╗███║███║\n█╔═█║█╔█║█╔█║\n████║█║█║█║█║\n╚═══╝╚╝╚╝╚╝╚╝'
    msg.edit(a)

@app.on_message(filters.command("r_cat", prefixes=".") & filters.me)
def r_cat(_, msg):
    a='.\n▒▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█ \n▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄ \n▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█ \n▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█ \n▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█ \n▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█ \n▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█ \n▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█ \n▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█'
    msg.edit(a)

@app.on_message(filters.command("question", prefixes=".") & filters.me)
def question(_, msg):
    a='▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██\n▓▓░░░░░░░░░░░░░░░░░░██\n▓▓░██░░░▓▓▓▓▓░░░░██░██\n▓▓░░░░▓▓████▓▓▓░░░░░██\n▓▓░░░░▓▓█░░░▓▓▓█░░░░██\n▓▓░░░░░██░░▓▓▓▓█░░░░██\n▓▓░░░░░░░▓▓▓████░░░░██\n▓▓░░░░░░░▓▓▓█░░░░░░░██\n▓▓░░░░░░░░███░░░░░░░██\n▓▓░░░░░░░▓▓▓░░░░░░░░██\n▓▓░░░░░░░▓▓▓█░░░░░░░██\n▓▓░██░░░░░███░░░░██░██\n▓▓░░░░░░░░░░░░░░░░░░██\n██████████████████████'        
    msg.edit(a)

app.run()