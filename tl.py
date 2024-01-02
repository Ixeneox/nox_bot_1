import telebot
from PIL import Image
import pyshorteners
import random
import requests
from pytube import YouTube
from youtubesearchpython import *
import os

import os


token="6758131775:AAGcEbZ37EMzyFkfrDe40MX20f9ZC2y-uik"
bot=telebot.TeleBot(token)

# def short(url):
#     return pyshorteners.Shortener().tinyurl.short(url)

# def short(url):
#     return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=["start"])
def start_command(Message):
    bot.send_message(Message.chat.id,text="Hi welcome")
    bot.send_video( Message.chat.id,open("1.mp4","rb"))


@bot.message_handler(commands=["gen"])
def gen_pic(Message):
    i=1
    x=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    global hc1
    hc1=""
    while i < 7: 
        y=random.randint(0,14)
        hc1 +=x[y]
        i +=1
    img=Image.new(mode="RGB",size=(1080,1080),color=f"#"+hc1)
    img.save("1.jpg")
    bot.send_photo(Message.chat.id,open("1.jpg","rb"))

@bot.message_handler(commands=["id"])
def id(Message):
    cht_id=Message.chat.id
    frst=Message.chat.first_name
    bot.send_message(Message.chat.id,text="{} \n id :@{} ".format(cht_id,frst))




# @bot.message_handler(content_types=['photo','audio','document','video'])
# def file_sent(Message):
#    imgurl=short(bot.get_file_url(Message.document.file_id))
#    response = requests.get(imgurl)
#    open("1.mp4", "wb").write(response.content)
#    bot.send_photo( Message.chat.id,open("1.mp4","rb"))


@bot.message_handler(commands=["yt"])
def yt(Message):
    bot.send_message(Message.chat.id,text="please send youtubelink" )
    
    bot.register_next_step_handler(Message,get_vid)

def get_vid(Message):
     yt1=Message.text
     yt=YouTube(yt1)
     ytn=yt.title
     fv=yt.streams.get_by_itag(18)
     short_link=pyshorteners.Shortener().tinyurl.short(fv)
    #  fv.download(filename=f"{ytn}+mp4")
    #  bot.send_video(Message.chat.id,open(f"{ytn}+mp4","rb"))
    #  os.remove(f"{ytn}+mp4")
pass
     
     
     
    
