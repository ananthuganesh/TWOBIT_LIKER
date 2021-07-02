from FunctionData.somefun import*
from instabot import*
import random
from tqdm import tqdm
from time import sleep
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


bot = Bot(
    min_likes_to_like=1,
    max_likes_to_like=10,
    like_delay=10,
    max_likes_per_day=600
    )


console_clear()
print('\u001b[31;1m   _______      ______  ___  __________  __   ______ _________ '),time.sleep(.1)
print('  /_  __/ | /| / / __ \/ _ )/  _/_  __/ / /  /  _/ //_/ __/ _ \ '),time.sleep(.1)
print('   / /  | |/ |/ / /_/ / _  |/ /  / /   / /___/ // ,< / _// , _/'),time.sleep(.1)
print('  /_/   |__/|__/\____/____/___/ /_/   /____/___/_/|_/___/_/|_| \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print('\u001b[32mInstagram App API: Private             YOUR IP:', IPAddr, '\u001b[0m'),time.sleep(.1)
print('\u001b[33;1mOwner(s): @un_f_amour @anandhx         Last Update: 30.5.2021\u001b[0m'),time.sleep(.1)
print('\u001b[31;1mMaintainer(s): @_arun                  Telegram: ProjectX_insta\u001b[0m'),time.sleep(.1)

print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print(' [ϟ] L O G I N')
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)

USERNAME = input("\u001b[32m[+]\u001b[0m Enter username:-")
PASSWORD = input("\u001b[32m[+]\u001b[0m Enter password:-")

print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
bot.login(username=USERNAME, password=PASSWORD, use_cookie=False)
console_clear()

print('\u001b[31;1m   _______      ______  ___  __________  __   ______ _________ '),time.sleep(.1)
print('  /_  __/ | /| / / __ \/ _ )/  _/_  __/ / /  /  _/ //_/ __/ _ \ '),time.sleep(.1)
print('   / /  | |/ |/ / /_/ / _  |/ /  / /   / /___/ // ,< / _// , _/'),time.sleep(.1)
print('  /_/   |__/|__/\____/____/___/ /_/   /____/___/_/|_/___/_/|_| \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print('\u001b[32mInstagram App API: Private             YOUR IP:', IPAddr, '\u001b[0m'),time.sleep(.1)
print('\u001b[33;1mOwner(s): @un_f_amour @anandhx         Last Update: 30.5.2021\u001b[0m'),time.sleep(.1)
print('\u001b[31;1mMaintainer(s): @_arun                  Telegram: ProjectX_insta\u001b[0m'),time.sleep(.1)
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)

while True:
    bot.like_timeline(amount=None)
    for i in tqdm(range(0, 100), desc ="\u001b[33;1mFetching Timeline\u001b[00m"):
	    sleep(.30)