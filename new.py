from instabot import Bot
import os
import random
import datetime
import time
import download
import shutil


username = "sirmeme_a_lot"
password = "@_LoT123569"

try:
    shutil.rmtree("./config/")
    shutil.rmtree("./__pycache__/")
except:
    print("nothing to remove")

MEME=os.listdir("./Meme")
caption = ""
image_filename = "./MEME/"+random.choice(MEME)
image="./MEME/one.jpg"
os.rename(image_filename,image)

bot = Bot()
bot.login(username=username, password=password)
#bot.upload_photo(photo=image)
time.sleep(10)
bot.upload_photo(image, caption=caption)
bot.logout()