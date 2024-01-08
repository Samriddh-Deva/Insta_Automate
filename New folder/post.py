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

bot = Bot()
bot.login(username=username, password=password)
bot.logout()
