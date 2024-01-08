from instabot import Bot
import os
import random
import datetime
import time
import download
import shutil

username = "xyz"
password = "xyz"

try:
    shutil.rmtree("./config/")
    shutil.rmtree("./__pycache__/")
except:
    print("nothing to remove")

#download.download_MEME()
MEME=os.listdir("./Meme")
caption = "hi"
image_filename = "./MEME/"+random.choice(MEME)
image="./MEME/1.jpg"
#image_path = os.path.join(".\Meme", image_filename)
print(image_filename)
# Upload the post


bot = Bot()
bot.login(username=username, password=password)
#bot.upload_photo(photo=image)
bot.upload_photo(image_filename, caption=caption)
#os.remove(image_path)

bot.logout()
