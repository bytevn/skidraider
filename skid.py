##############################################################################################################################################
#                                             8       o      8                 o      8                                                      #
#                            +                8              8                        8                                 +                 +  #
#            +                         .oPYo. 8  .o  o8 .oPYo8   oPYo. .oPYo. o8 .oPYo8 .oPYo. oPYo.                                         #
#                                      Yb..   8oP'    8 8    8   8  `' .oooo8  8 8    8 8oooo8 8  `'                                         #
#  +                          +          'Yb. 8 `b.   8 8    8   8     8    8  8 8    8 8.     8        +                                    #
#                                      `YooP' 8  `o.  8 `YooP'   8     `YooP8  8 `YooP' `Yooo' 8                          +                  #
#                   +                  :.....:..::...:..:.....:::..:::::.....::..:.....::.....:..::::                                        #
#        +                             ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::                                        #
#                               +      ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::          +                  +          #
#                                                                                                                                            #
##############################################################################################################################################

import re  
import os
import sys 
import time
import json
import httpx
import ctypes
import random
import base64
import string
import discord
import requests
import binascii
import websocket
import threading
import tls_client
import json as jsond
import datetime as dt
from Crypto.Cipher        import AES
from typing               import Union
from decimal              import Decimal
from discord.ext          import commands
from pypresence           import Presence
from websocket            import WebSocket 
from base64               import b64encode 
from Crypto.Util.Padding  import pad, unpad
from plyer                import notification
from random               import sample, choice
from urllib.parse         import urlparse, parse_qs

os.system('cls')
os.system('title Loading...')
def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(_str)
    elif system == 'posix':
        sys.stdout.write(_str)
    else:
        pass
setTitle('Skid | Console')
print('Watting...')

def load_token():
    path = os.path.join(os.getenv('APPDATA'), 'Skid', 'user.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, 'r', encoding='utf-8') as file:
            user = json.load(file)
    except FileNotFoundError:
        user = {"tokenencode": ""}
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(user, file, indent=4)
    return user["tokenencode"]

def load_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {
            "prefix": ".",
            "notification": "True",
            "rpc": "True",
            "bal": {
                "btc": "",
                "eth": "",
                "ltc": ""
            }
        }
        save_config(config)

    return config

def save_config(config):
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)

def reloadconfig():
    config = load_config()
    return config

def reload_token():
    TOKEN = load_token()
    try:
        key = b'\xc6Y\xb2M\x8b\xf6\xe1\x98K\x8e\xfa|}~\xbb\xa9\xc7\xa1\xe5Y\x9e\xaf[$%\x12\xd4\xb4Q\xc9\xb3\xa3'
        iv = b'\x9c\xb17\x98\x07\x91\x1a\xf0\xb3"\xb3\xb83\xbd2*'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(base64.b64decode(TOKEN)), AES.block_size)
        return pt.decode('utf-8')
    except:
        return ''
def load_settings():
    try:
        with open('settings.json', 'r', encoding='utf-8') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {
                        "spam": {
                            "message": "",
                            "channelid": "",
                            "serverid": "",
                            "delay": 0,
                            "random": {
                                "use": "True",
                                "type": "emoji",
                                "length": 100
                            },
                            "massping": {
                                "type": "True",
                                "onlyonline": "True",
                                "pingpermessage": 1
                            }
                        },
                        "massspam": {
                            "message": "",
                            "channelids": [],
                            "serverid": "",
                            "delay": 0,
                            "random": {
                                "use": "True",
                                "type": "emoji",
                                "length": 100
                            },
                            "massping": {
                                "type": "True",
                                "onlyonline": "True",
                                "pingpermessage": 1
                            }
                        },
                        "poll": {
                            "channelid": "",
                            "question": "who are u?",
                            "answerlist": ["nigger", "gay", "sex", "trans", "nigger and gay", "nigger and trans"],
                            "number": 3,
                            "duration": 24,
                            "delay": 0
                        },
                        "join": {
                            "invite": ""
                        },
                        "leave": {
                            "serverid": ""
                        },
                        "nick": {
                            "nickname": "",
                            "serverid": ""
                        },
                        "voicecall": {
                            "channelid": "",
                            "serverid": "",
                            "mute": "False",
                            "deaf": "False",
                            "stream": "False",
                            "video": "False"
                        },
                        "reaction": {
                            "channelid": "",
                            "messageid": ""
                        },
                        "button": {
                            "number": "",
                            "channelid": "",
                            "serverid": "",
                            "messageid": ""
                        },
                        "boost": {
                            "serverid": ""
                        },
                        "vaultcord": {
                            "botid": ""
                        },
                        "message": {
                            "message": "",
                            "channelid": ""
                        },
                        "call": {
                            "userid": ""
                        },
                        "friend": {
                            "username": ""
                        },
                        "unfriend": {
                            "userid": ""
                        },
                        "dm": {
                            "userid": "",
                            "message": ""
                        },
                        "typing": {
                            "channelid": ""
                        },
                        "fun": {
                            "channelid": ""
                        }
                    }
        save_settings(settings)

    return settings

def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

def reloadsettings():
    settings = load_settings()
    return settings

if not os.path.exists('tokens.txt'):
    with open('tokens.txt', 'w', encoding='utf-8') as file:
        file.write("") 
if not os.path.exists('scraped'):
    os.makedirs('scraped')
            
config = reloadconfig()
settings = reloadsettings()
PREFIX = config["prefix"]
TOKEN = reload_token()
class console:
    def log(message, token=None):
        nowz = dt.datetime.now().strftime("%H:%M:%S")
        if token is None:
            print(f"{nowz} {message}")
        else:
            print(f"{nowz} {message} Token: {token[:26]}")

    def push(message):
        config = reloadconfig()
        if config["notification"] == "True" or config["notification"] == "true":
            def notify(message):
                notification.notify(
                    title='Skid',
                    message=message,
                    timeout=1
                )
            threading.Thread(target=notify, args=(message,)).start()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

try:
    stop_spam = False

    bot = commands.Bot(command_prefix= PREFIX, self_bot=True)
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        if config["rpc"] == 'True' or config["rpc"] == 'true':
            RPC = Presence('1251072773820911626')
            RPC.connect()
            RPC.update(
                details='Activated - Console',
                large_image='icon',
                buttons=[{"label": "Check It Out!", "url": "https://discord.gg/jF4MEYm5HD"}, {"label": "ShowCase", "url": "https://youtu.be/HZOrWxRvIAI"}]
            )
    except: None
    @bot.event
    async def on_ready():
        os.system('cls')
        print(f'Client ready! Active with name: {bot.user.name}')
        console.push(f'Connected {bot.user.name}')

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            console.log(f"invalid command: {ctx.message.content}")
            console.push(f"Invalid command: {ctx.message.content}")
            await ctx.send(f"Invalid command: {ctx.message.content}", delete_after=3)

    def spamchannel(token, delay, channel_id, message, guild_id):
        global stop_spam
        stop_spam = False
        while not stop_spam:
            settings=reloadsettings()
            message = settings["spam"]["message"]
            channel_id = settings["spam"]["channelid"]
            guild_id = settings["spam"]["serverid"]
            delay = settings["spam"]["delay"]
            message1 = message
            if settings["spam"]["massping"]["type"] == "True" or settings["spam"]["massping"]["type"] == "true":
                with open(f"scraped/{guild_id}.txt", "r") as file:
                        allText = file.read()
                        words = list(map(str, allText.split()))
                moss = " ".join(random.choice(words) for _ in range(settings["spam"]["massping"]["pingpermessage"]))
                message1 += " | " + moss
            if settings["spam"]["random"]["use"] == "True" or settings["spam"]["random"]["use"] == "true":
                if settings["spam"]["random"]["type"] == "emoji":
                    emojis = [
                        "😀", "😁", "😂", "🤣", "😃", "😄", "😎", "😋", "😊", "😉",
                        "😆", "😅", "😍", "😘", "🥰", "😗", "😙", "🥲", "🤔", "🤩",
                        "🤗", "🙂", "☺️", "😚", "🫡", "🤨", "😐", "😑", "😶", "🙄",
                        "😏", "😣", "😥", "😮", "😴", "😫", "🥱", "😪", "😯", "🤐",
                        "😌", "😛", "😜", "😝", "🤤", "😒", "🫠", "🙃", "🫤", "😕",
                        "😔", "😓", "🤑", "😲", "☹️", "🙁", "😖", "😞", "😧", "😦",
                        "😭", "😢", "😤", "😟", "😨", "😩", "🤯", "😬", "😮‍💨", "😰",
                        "😵", "🤪", "😳", "🥶", "🥵", "😱", "😵‍💫", "🥴", "😠", "😡",
                        "🤬", "😷", "😇", "🤧", "🤮", "🤢", "🤕", "🤒", "🥳", "🥸",
                        "🥺", "🥹", "🤠", "🤡", "🧐", "🫣", "🫢", "🤭", "🤫", "🤥", "🤓"
                    ]
                    random_emojis = "".join(random.sample(emojis, k=settings["spam"]["random"]["length"]))

                    message1 += " | " + random_emojis
                else:
                    random_texts = ''.join(random.choices(string.ascii_letters + string.digits, k=settings["spam"]["random"]["length"]))
                    message1 += " | " + random_texts
            try:
                url = 'https://discord.com/api/v9/channels/' + channel_id + '/messages'
                payload = {
                    'mobile_network_type': 'unknown',
                    'content': message1,
                    'nonce': str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                    'tts': False,
                    'flags': 0,
                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                    'Accept': '*/*',
                    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Content-Type': 'application/json',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ2aS1WTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzM5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Discord-Timezone': 'Asia/Ho_Chi_Minh',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com/channels/@me',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Priority': 'u=1',
                }
                session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
                r = session.post(url, headers=headers, json=payload)
                if r.status_code == 200:
                    console.log('sent', token)
                elif "exceeds the mention limit set by this server" in r.text:
                    console.log('mention limit', token)
                elif "This content is blocked by this server" in r.text:
                    console.log('content block', token)
                elif "retry_after" in r.text:
                    time.sleep((r.json()["retry_after"]))
                else:
                    print(r.text)
                try:
                    time.sleep(int(delay))
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

    def spammasschannel(token, delay, channel_id, message, guild_id):
        global stop_spam
        stop_spam = False
        while not stop_spam:
            settings=reloadsettings()
            message = settings["massspam"]["message"]
            guild_id = settings["massspam"]["serverid"]
            delay == settings["massspam"]["delay"]
            message1 = message
            if settings["massspam"]["massping"]["type"] == "True" or settings["massspam"]["massping"]["type"] == "true":
                with open(f"scraped/{guild_id}.txt", "r") as file:
                        allText = file.read()
                        words = list(map(str, allText.split()))
                moss = " ".join(random.choice(words) for _ in range(settings["massspam"]["massping"]["pingpermessage"]))
                message1 += " | " + moss
            if settings["massspam"]["random"]["use"] == "True" or settings["spamassspamm"]["random"]["use"] == "true":
                if settings["massspam"]["random"]["type"] == "emoji":
                    emojis = [
                        "😀", "😁", "😂", "🤣", "😃", "😄", "😎", "😋", "😊", "😉",
                        "😆", "😅", "😍", "😘", "🥰", "😗", "😙", "🥲", "🤔", "🤩",
                        "🤗", "🙂", "☺️", "😚", "🫡", "🤨", "😐", "😑", "😶", "🙄",
                        "😏", "😣", "😥", "😮", "😴", "😫", "🥱", "😪", "😯", "🤐",
                        "😌", "😛", "😜", "😝", "🤤", "😒", "🫠", "🙃", "🫤", "😕",
                        "😔", "😓", "🤑", "😲", "☹️", "🙁", "😖", "😞", "😧", "😦",
                        "😭", "😢", "😤", "😟", "😨", "😩", "🤯", "😬", "😮‍💨", "😰",
                        "😵", "🤪", "😳", "🥶", "🥵", "😱", "😵‍💫", "🥴", "😠", "😡",
                        "🤬", "😷", "😇", "🤧", "🤮", "🤢", "🤕", "🤒", "🥳", "🥸",
                        "🥺", "🥹", "🤠", "🤡", "🧐", "🫣", "🫢", "🤭", "🤫", "🤥", "🤓"
                    ]
                    random_emojis = "".join(random.sample(emojis, k=settings["massspam"]["random"]["length"]))

                    message1 += " | " + random_emojis
                elif settings["massspam"]["random"]["type"] == "text":
                    random_texts = ''.join(random.choices(string.ascii_letters + string.digits, k=settings["massspam"]["random"]["length"]))
                    message1 += " | " + random_texts
            try:
                url = 'https://discord.com/api/v9/channels/' + channel_id + '/messages'
                payload = {
                    'mobile_network_type': 'unknown',
                    'content': message1,
                    'nonce': str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                    'tts': False,
                    'flags': 0,
                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                    'Accept': '*/*',
                    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Content-Type': 'application/json',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ2aS1WTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzM5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Discord-Timezone': 'Asia/Ho_Chi_Minh',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com/channels/@me',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Priority': 'u=1',
                }
                session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
                r = session.post(url, headers=headers, json=payload)
                if r.status_code == 200:
                    console.log('sent', token)
                elif "exceeds the mention limit set by this server" in r.text:
                    console.log('mention limit', token)
                elif "This content is blocked by this server" in r.text:
                    console.log('content block', token)
                elif "retry_after" in r.text:
                    time.sleep((r.json()["retry_after"]))
                else:
                    print(r.text)
                try:
                    time.sleep(int(delay))
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

    def spam1(token, message, channel_id):
        try:
            url = 'https://discord.com/api/v9/channels/' + channel_id + '/messages'
            payload = {
                'mobile_network_type': 'unknown',
                'content': message1,
                'nonce': str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                'tts': False,
                'flags': 0,
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
                'Accept': '*/*',
                'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Content-Type': 'application/json',
                'Authorization': token,
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ2aS1WTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzM5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                'X-Discord-Locale': 'en-US',
                'X-Discord-Timezone': 'Asia/Ho_Chi_Minh',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'Connection': 'keep-alive',
                'Referer': 'https://discord.com/channels/@me',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Priority': 'u=1',
            }
            session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
            r = session.post(url, headers=headers, json=payload)
            if r.status_code == 200:
                console.log('sent', token)
            elif "exceeds the mention limit set by this server" in r.text:
                console.log('mention limit', token)
            elif "This content is blocked by this server" in r.text:
                console.log('content block', token)
            elif "retry_after" in r.text:
                time.sleep((r.json()["retry_after"]))
        except Exception as e:
            print(e)

    def poll_spam(token, channel_id, delay):
        global stop_spam
        stop_spam = False
        while not stop_spam:
            settings=reloadsettings()
            question = settings["poll"]["question"]
            answerlist = settings["poll"]["answerlist"]
            number = settings["poll"]["number"]
            duration = settings["poll"]["duration"]
            delay = settings["poll"]["delay"]
            if question != "" and answerlist != [""]:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
                    'authorization': token,
                    'content-type': 'application/json',
                    'origin': 'https://discord.com',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-discord-timezone': 'Asia/Saigon',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
                }

                def randomanswer(answerlist):
                    answer = random.choice(answerlist)
                    return answer
                json_data = {
                    'mobile_network_type': 'unknown',
                    'content': '',
                    "nonce": str(round(Decimal(time.time()*1000-1420070400000)*4194304)),
                    'tts': False,
                    'flags': 0,
                    'poll': {
                        'question': {
                            'text': question,
                        },
                        'answers': [],
                        'allow_multiselect': False,
                        'duration': duration,
                        'layout_type': 1,
                    },
                }

                for _ in range(number):
                    textdd = {
                        'poll_media': {
                            'text': randomanswer(answerlist),
                        }
                    }
                    json_data['poll']['answers'].append(textdd)
                session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
                req = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=json_data)
                if req.status_code == 200:
                    console.log('created poll', token)
                elif "retry_after" in req.text:
                    time.sleep((req.json()["retry_after"]))
                else:
                    console.log('fail to create poll', token)
                    print(req.text)
                try:
                    time.sleep(int(delay))
                except Exception as e:
                    print(e)
            else:
                console.log('fail to create poll', token)
                print(req.text)

    def voicecall(token, channel_id, guild_id):
        def connectvc(token, channel_id, guild_id):
            global stop_spam
            stop_spam = False
            while not stop_spam:
                settings=reloadsettings()
                mute = (lambda s: s.lower() == "true")(settings["voicecall"]["mute"])
                deaf = (lambda s: s.lower() == "true")(settings["voicecall"]["deaf"])
                stream = (lambda s: s.lower() == "true")(settings["voicecall"]["stream"])
                video = (lambda s: s.lower() == "true")(settings["voicecall"]["video"])
                ws = WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                hello = json.loads(ws.recv())
                heartbeat_interval = hello['d']['heartbeat_interval']
                ws.send(json.dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
                ws.send(json.dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": channel_id,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
                ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": channel_id,"preferred_region": "singapore"}}))
                ws.send(json.dumps({"op": 1,"d": None}))
                ws.recv()
                time.sleep(hello.get("d").get("heartbeat_interval") / 1000)

        threading.Thread(target=connectvc, args=(token, channel_id, guild_id)).start()
        console.log('Joined Voice Call', token)

    def accept_invite(token, invite, guild_id, channel_id, channel_type):
        settings=reloadsettings()
        config = reloadconfig()
        invite = settings["join"]["invite"]
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        jsonContext = {
            "location": "Join Guild",
            "location_guild_id": str(guild_id),
            "location_channel_id": str(channel_id),
            "location_channel_type": int(channel_type),
        }

        json_str = json.dumps(jsonContext)
        xContext = b64encode(json_str.encode()).decode()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
            'Accept': '*/*',
            'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/json',
            'X-Context-Properties': '',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ2aS1WTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzA3MzkyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Asia/Ho_Chi_Minh',
            'X-Debug-Options': 'bugReporterEnabled',
            'Origin': 'https://discord.com',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/channels/@me',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies)
        try:
            headers["Cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'
            headers['Referer'] = f"https://discord.com/channels/{guild_id}/{channel_id}"
            headers['X-Context-Properties'] = xContext
            try:
                req = session.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers, cookies=cookies, json={})

                if req.status_code == 200:
                    console.log(f'joined', token)
                    headers.pop('X-Context-Properties', None)
                    check = req.json()["guild"]["features"]
                    guild_id = req.json()["guild_id"]
                    if 'MEMBER_VERIFICATION_GATE_ENABLED' in check:
                        get_rules = session.get(
                            f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false",
                            headers=headers,
                            cookies=cookies
                        ).json()
                        req = session.put(
                            f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
                            headers=headers,
                            cookies=cookies,
                            json=get_rules
                        )
                        
                        if req.status_code == 201:
                            console.log('accepted rules', token)
                        elif "You need to verify your account in order to perform this action." in req.json():
                            console.log('request to verify phone number to bypass rules', token)
                        else:
                            console.log('fail to accept rule', token)

                    if 'GUILD_ONBOARDING_EVER_ENABLED' in check:
                        class OnboardingInfo:
                            guild_id: int = 0
                            required_prompts: list[dict[str, Union[str, list[Union[str, dict, list, bool, None]]]]] = []
                            onboarding_prompts_seen: dict[str, int] = {}
                            onboarding_responses_seen: dict[str, int] = {}
                            onboarding_responses: list[str] = []

                        req=False
                        while not req:
                            req = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/onboarding",headers=headers, cookies=cookies)

                            if req.status_code == 200:
                                break
                            else:
                                time.sleep(1)

                        req = req.json()

                        updated_prompts = []
                        try:
                            for prompt in req["prompts"]:
                                if prompt["required"]:
                                    updated_prompts.append(prompt)
                        except Exception as e:
                            return False, None    

                        try:
                            req["prompts"] = updated_prompts
                            for prompt in req["prompts"]:
                                OnboardingInfo.onboarding_prompts_seen[str(prompt["id"])] = 1681404058976
                            for prompt in req["prompts"]:
                                for option in prompt["options"]:
                                    OnboardingInfo.onboarding_responses_seen[str(option["id"])] = 1681404058976
                            for prompt in req["prompts"]:
                                OnboardingInfo.onboarding_responses.append(choice(prompt["options"])["id"])
                        except Exception as e:
                            return False, None         

                        js = {
                            "onboarding_prompts_seen": OnboardingInfo.onboarding_prompts_seen,
                            "onboarding_responses": OnboardingInfo.onboarding_responses,
                            "onboarding_responses_seen": OnboardingInfo.onboarding_responses_seen,
                            "update_roles_and_channels": True,
                        }

                        req = session.post(f"https://discord.com/api/v9/guilds/{guild_id}/onboarding-responses",headers=headers, cookies=cookies, json=js)
                        if req.status_code == 200:
                            console.log('bypassed onboarding', token)
                        else:
                            console.log('fail to bypass onboarding', token)

                elif req.status_code == 401:
                    console.log('token invalid', token)
                elif req.status_code == 400:
                    console.log('captcha on join', token)
                else:
                    console.log(f'fail to join server', token)
                    print(req.text)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
            
    def leaveserver(token, guild_id):
        settings=reloadsettings()
        guild_id = settings["leave"]["serverid"]

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }

        try:
            session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
            json_data = {
                'lurking': False,
            }
            response = session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers=headers, json=json_data)
            if response.status_code == 204:
                console.log('leaved', token)
            else:
                console.log('fail to leave server', token)
                print(response.text)
        except Exception as e:
            print(e)

    def addreaction(token, emoji, channel_id, message_id):

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }

        a = requests.put(
            f"https://discordapp.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",headers=headers)

        if a.status_code == 204:
            console.log('reaction', token)
        else:
            console.log('fail to reaction', token)
            print(a.text)

    def onliner(token):
        global stop_spam
        stop_spam = False
        while not stop_spam:
            type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening'])
            status = random.choice(['online', 'dnd', 'idle'])

            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            if type == "Playing":
                game = random.choice(["Minecraft", "Badlion", "Roblox", "The Elder Scrolls: Online", "DCS World Steam Edit", ])
                gamejson = {
                    "name": game,
                    "type": 0
                }
            elif type == 'Streaming':
                game = random.choice(["Youtube"], ["Twitch"])
                if game == 'Youtube':
                    stream_text = 'https://www.youtube.com/'
                if game == 'Twitch':
                    stream_text = 'https://www.twitch.tv/'
                gamejson = {
                    "name": game,
                    "type": 1,
                    "url": stream_text
                }
            elif type == "Listening":
                game = random.choice(["Spotify", "Deezer", "Apple Music", "YouTube", "SoundCloud", "Pandora", "Tidal", "Amazon Music", "Google Play Music", "Apple Podcasts", "iTunes", "Beatport"])
                gamejson = {
                    "name": game,
                    "type": 2
                }
            elif type == "Watching":
                game = random.choice(["YouTube", "Twitch"])
                gamejson = {
                    "name": game,
                    "type": 3
                }

            auth = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": 'windows',
                        "$browser": "Discord",
                        "$device": f"desktop"
                    },
                    "presence": {
                        "game": gamejson,
                        "status": status,
                        "since": 0,
                        "afk": False
                    }
                },
                "s": None,
                "t": None
            }
            ws.send(json.dumps(auth))
            ack = {
                "op": 1,
                "d": None
            }
            print(f"online", token)
            while not stop_spam:
                time.sleep(heartbeat_interval / 1000)
                try:
                    ws.send(json.dumps(ack))

                except Exception as e:
                    print(e)
                    break
                
    def booster(token, guild_id):
        def has_nitro(token, session = None, headers= None, cookies=None):
            try:
                sub_ids = []
                req = session.get(
                    "https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots",
                    headers=headers,
                    cookies=cookies
                )
                if req.status_code in [403, 401]:
                    console.log('token is invalid', token)
                    return False
                data = req.json()
                try:
                    for sub in data:
                        sub_ids.append(sub["id"])
                except Exception as e:
                    return False, None

                if len(sub_ids) == 0:
                    console.log('token does not have any nitro boosts', token)
                    return False, None
                return True, sub_ids
            except Exception as e:
                console.log('error', token)
                return False, None

        def boostServer(guildID, sub_ids):
            for i in range(len(sub_ids)):
                headers["Content-Type"] = "application/json"
                r = session.put(
                    url=f"https://discord.com/api/v9/guilds/{guildID}/premium/subscriptions",
                    headers=headers,
                    cookies=cookies,
                    json={
                        "user_premium_guild_subscription_slot_ids": [f"{sub_ids[i]}"]
                    },
                )
                if r.status_code == 201:
                    data = {
                        "success": True,
                        "message": "Successfully boosted server.",
                    }
                elif r.status_code == 400:
                    data = {
                        "success": False,
                        "message": "You already boosted this server.",
                    }
                else:
                    def short_string(string: str, length: int = None):
                        if length is None or not str(length).isdigit():
                            length = os.get_terminal_size().columns
                        if len(string) > int(length):
                            return string[:int(length)] + "..."
                        else:
                            return string
                    data = {
                        "success": False,
                        "message": short_string(r.text),
                    }
            return data
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'

            has_nitro, sub_ids = has_nitro(token, session, headers, cookies)
            if has_nitro and sub_ids is not None:
                bost = boostServer(guild_id, sub_ids)
                if bost.get("success", False):
                    console.log('boosted', token)
                else:
                    console.log('fail to boost server', token)
            else:
                console.log('no nitro', token)
        except Exception as e:
            print(e)

    def typer(channel_id, token):
        global stop_spam
        stop_spam = False
        settings=reloadsettings()
        channel_id = settings["typing"]["channelid"]

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }

        req = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/typing",
            headers=headers
        )

        if req.status_code == 204:
            console.log('success', token)

            while not stop_spam:
                requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/typing",
                    headers=headers
                )
                time.sleep(5)

        else:
            console.log('fail to send requests', token)
            print(req.text)

    def open_dms(user_id, token, message):
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'

            headers['referer'] = f"https://discord.com"
            headers['x-context-properties'] = "eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSBNb2RhbCAtIENvbnRleHQgTWVudSJ9"

            open_dm = session.post("https://discord.com/api/v9/users/@me/channels",headers=headers, cookies=cookies,json={
                "recipients": [
                    str(user_id)
                ]
            })

            if open_dm.status_code==200:
                threading.Thread(target=spam_dm, args=[user_id, message, session, headers,cookies, open_dm, token]).start()
            else:
                if open_dm.json().get("message"):
                    console.log(open_dm.json()['message'], token)
                else:
                    console.log('fail to open dms', token)
                    print(open_dm.text)
        except Exception as e:
            print(e)
    def spam_dm(user_id, message, session, headers,cookies, open_dm, token):
        global stop_spam
        stop_spam = False
        while not stop_spam:
            config = reloadconfig()
            data={
                'mobile_network_type': 'unknown',
                "content": message,
                "nonce": str(round(Decimal(time.time()*1000-1420070400000)*4194304)),
                "tts": False,
                "flags": 0
            }

            send =session.post(f"https://discord.com/api/v9/channels/{open_dm.json()['id']}/messages",headers=headers, cookies=cookies,json=data)
            
            if send.status_code==200:
                console.log(f'sent', token)
                message_id = send.json()['id']
                delete = session.delete(f"https://discord.com/api/v9/channels/{open_dm.json()['id']}/messages/{message_id}", headers=headers, cookies=cookies)
                continue

            elif "captcha" in send.text:
                console.log('captcha on dm')
            else:
                if send.json().get("message"):
                    console.log('sent', token)
                elif "retry_after" in send.text:
                    time.sleep((send.json()["retry_after"]))

    def open_call(user_id, token):
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'
            headers['referer'] = f"https://discord.com"
            headers['x-context-properties'] = "eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSBNb2RhbCAtIENvbnRleHQgTWVudSJ9"

            open_dm = session.post("https://discord.com/api/v9/users/@me/channels",headers=headers, cookies=cookies,json={
                "recipients": [
                    str(user_id)
                ]
            })

            if open_dm.status_code==200:
                del headers["x-context-properties"]
                threading.Thread(target=calll, args=[user_id, open_dm, token]).start()
            else:
                if open_dm.json().get("message"):
                    console.log(open_dm.json()['message'], token)
                else:
                    console.log('fail to open dm', token)
                    print(open_dm.text)
        except Exception as e:
            print(e)
    def calll(user_id, open_dm, token):
        try:
            user_id = open_dm.json().get("id")            
            def _call(user_id, token):
                global stop_spam
                stop_spam = False
                skip = False
                while not stop_spam:
                    try:
                        if skip:
                            skip = not skip
                            time.sleep(1.75)
                            continue
                        console.log('calling', token)
                        ws = WebSocket()
                        ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                        hello = json.loads(ws.recv())
                        ws.send(json.dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
                        ws.send(json.dumps({"op": 4,"d": {"guild_id": None,"channel_id": str(user_id),"self_mute": False,"self_deaf": False, "self_stream": False, "self_video": False}}))
                        ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": None,"channel_id": str(user_id),"preferred_region": "singapore"}}))
                        ws.send(json.dumps({"op": 1,"d": None}))
                        time.sleep(1)
                        ws.send(json.dumps({
                            "op":4,
                            "d":{
                                "guild_id":None,
                                "channel_id":None,
                                "self_mute":True,
                                "self_deaf":False,
                                "self_video":False
                            }
                        }))
                        time.sleep(1.75)
                    except Exception as e:
                        console.log(e, token)
                        continue
            while True:
                _call(user_id, token)
        except Exception as e:
            print(e)

    def unfrienduser(token, user_id):
        settings=reloadsettings()
        user_id = settings["unfriend"]["userid"]
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        headers['x-context-properties'] = "eyJsb2NhdGlvbiI6InVzZXIgcHJvZmlsZSBhY3Rpb25zIG1lbnUifQ=="
        req = session.delete(f"https://discord.com/api/v9/users/@me/relationships/{user_id}",headers=headers)

        if req.status_code == 204:
            console.log('unfriend success', token)
        elif "captcha_key" in req.text:
            console.log('captcha detect', token)
        else:
            console.log('fail to unfriend', token)
            print(req.text)

    def frienduser(token: str, username: str):
        settings=reloadsettings()
        username = settings["friend"]["username"]
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'
            headers['x-context-properties'] = "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ=="
            data = {
                'username': username,
                'discriminator': None,
            }


            try:
                req = session.post(
                    "https://discord.com/api/v9/users/@me/relationships",
                    headers=headers,
                    cookies=cookies,
                    json=data
                )
                if req.status_code==204:
                    console.log('sent friend', token)
                elif "captcha_key" in req.text:
                    console.log('captcha detect', token)
                else:
                    console.log('fail to send friend', token)
                    print(req.text)
            except ValueError:
                console.log('invalid username')
                return
        except Exception as e:
            print(e)
    def changenick(token, guild_id, nickname):
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
            'Accept': '*/*',
            'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'Authorization': token,
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ2aS1WTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzM5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Asia/Ho_Chi_Minh',
            'X-Debug-Options': 'bugReporterEnabled',
            'Origin': 'https://discord.com',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/channels/@me',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=1',
        }
        
        r = session.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me/nick", headers=headers,json={"nick": nickname})
        if r.status_code == 200:
            console.log('nick', token)
        if r.status_code != 200:
            console.log('fail to change nick', token)
            print(r.text)
    def funnycommand1(token, channel_id, message_id):
        emojis = [
            "👩", "👨", "🧑", "👧", "👦", "🧒", "👶", "👵", "👴", "🧓",
            "👩‍🦰", "👨‍🦰", "🧑‍🦰", "👩‍🦱", "👨‍🦱", "🧑‍🦱", "🧑‍🦳", "👱‍♂️", "👨‍🦳", "👱‍♂️"
        ]

        for emoji in emojis:
            emoji = random.choice(emojis)
            headers = {'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US',
                    'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    'DNT': '1',
                    'origin': 'https://discord.com',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    'TE': 'Trailers',
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                    }
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                headers=headers)

            if a.status_code == 204:
                console.log('funny', token)
            elif "retry_after" in a.text:
                time.sleep((a.json()["retry_after"]))



    def bypass(token, botid):
        def generate_random_ip():
            ip_parts = [str(random.randint(0, 255)) for _ in range(4)]

            random_ip = '.'.join(ip_parts)

            return random_ip
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'


            custom_redirect = session.get(f"https://discord.com/api/v9/oauth2/authorize?client_id={botid}&response_type=code", headers=headers,cookies=cookies).json().get("redirect_uri")


            querystring = {
                "client_id":str(botid),
                "response_type":"code",
                "redirect_uri":custom_redirect,
                "scope":"identify guilds.join",
                "state":str(botid)
            }

            request = session.post(
                f"https://discord.com/api/v9/oauth2/authorize",
                headers=headers,
                cookies=cookies,
                params=querystring,
                json={"permissions":"0","authorize":True}
            )
            if "location" in request.text:
                answer = request.json()["location"]
                url = urlparse(answer)

                code = parse_qs(url.query).get('code', [None])[0]
                
                headers = {
                    'authority': 'api.vaultcord.com',
                    'accept': '*/*',
                    'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
                    'content-type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': 'https://discord.com',
                    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
                }
                json_data = {
                    'code': code,
                    'domain': url.netloc,
                    'ip': generate_random_ip(),
                    'fingerprint': None,
                }

                response = requests.post('https://api.vaultcord.com/servers/verify', headers=headers, json=json_data)
                if response.status_code == 200:
                    console.log('bypass', token)
                else:
                    console.log('fail to bypass', token)
                    print(response.text)
        except Exception as e:
            print(e)

    def click_button(token, guild_id, channel_id, message_id, custom_id, application_id):
        session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)

        headers = {
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Saigon',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjYzNjcuMTE4IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC42MzY3LjExOCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTcyNzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',        
        }
        cookies = dict(session.get(f"https://discord.com/api/v9/users/@me", headers=headers).cookies); cookies["__cf_bm"] = "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="; cookies["locale"] = "vi"
        try:
            headers["cookie"] = f'__dcfduid={cookies["__dcfduid"]}; __sdcfduid={cookies["__sdcfduid"]}; __cfruid={cookies["__cfruid"]}; __cf_bm={cookies["__cf_bm"]}; locale={cookies["locale"]}'
            post_data = {
                "application_id": str(application_id),
                "channel_id": str(channel_id),
                "data": {
                    "component_type": 2,
                    "custom_id": str(custom_id)
                },
                "guild_id": str(guild_id),
                "message_flags": 0,
                "message_id": str(message_id),
                "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                "session_id": str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                "type": 3,
                
            }
            headers.update({"referer": f"https://discord.com/channels/{guild_id}/{channel_id}"})
            req = session.post(f"https://discord.com/api/v9/interactions", headers=headers, cookies=cookies, json=post_data)
            if req.status_code == 204:
                console.log(f"pressed button", token)
            else:
                console.log(f"fail to press button", token)
                print(req.text)
        except Exception as e:
            print(e)

    class DiscordSocket(websocket.WebSocketApp):
        
        def __init__(self, token, guild_id, channel_id, onlyonlinemember):
            self.MAX_ITER = 10
            self.token = token
            self.guild_id = guild_id
            self.channel_id = channel_id
            self.blacklisted_roles, self.blacklisted_users = [], []
            self.socket_headers = {
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0",
            }
            super().__init__(
                "wss://gateway.discord.gg/?encoding=json&v=9",
                header=self.socket_headers,
                on_open=lambda ws: self.sock_open(ws),
                on_message=lambda ws, msg: self.sock_message(ws, msg, onlyonlinemember),
                on_close=lambda ws, close_code, close_msg: self.sock_close(
                    ws, close_code, close_msg
                ),
            )
            self.endScraping = False
            self.guilds = {}
            self.members: list[str] = []
            self.ranges = [[0]]
            self.lastRange = 0
            self.packets_recv = 0
            self.msgs = []
            self.d = 1
            self.iter = 0
            self.big_iter = 0
            self.finished = False
            
            

        def getRanges(self, index, multiplier, memberCount):
            initialNum = int(index * multiplier)
            rangesList = [[initialNum, initialNum + 99]]
            if memberCount > initialNum + 99:
                rangesList.append([initialNum + 100, initialNum + 199])
            if [0, 99] not in rangesList:
                rangesList.insert(0, [0, 99])
            return rangesList

        def parseGuildMemberListUpdate(self, response):
            memberdata = {
                "online_count": response["d"]["online_count"],
                "member_count": response["d"]["member_count"],
                "id": response["d"]["id"],
                "guild_id": response["d"]["guild_id"],
                "hoisted_roles": response["d"]["groups"],
                "types": [],
                "locations": [],
                "updates": [],
            }
            for chunk in response["d"]["ops"]:
                memberdata["types"].append(chunk["op"])
                if chunk["op"] in ("SYNC", "INVALIDATE"):
                    memberdata["locations"].append(chunk["range"])
                    if chunk["op"] == "SYNC":
                        memberdata["updates"].append(chunk["items"])
                    else:
                        memberdata["updates"].append([])
                elif chunk["op"] in ("INSERT", "UPDATE", "DELETE"):
                    memberdata["locations"].append(chunk["index"])
                    if chunk["op"] == "DELETE":
                        memberdata["updates"].append([])
                    else:
                        memberdata["updates"].append(chunk["item"])
            return memberdata

        def find_most_reoccuring(self, list):
            return max(set(list), key=list.count)

        def run(self) -> list[str]:
            try:
                self.run_forever()
                self.finished = True
                return self.members
            except Exception as e:
                print(e)
                pass

        def scrapeUsers(self):
            if self.endScraping == False:
                self.send(
                    '{"op":14,"d":{"guild_id":"'
                    + self.guild_id
                    + '","typing":true,"activities":true,"threads":true,"channels":{"'
                    + self.channel_id
                    + '":'
                    + json.dumps(self.ranges)
                    + "}}}"
                )

        def sock_open(self, ws):
            self.send(
                '{"op":2,"d":{"token":"'
                + self.token
                + '","capabilities":125,"properties":{"os":"Windows","browser":"Firefox","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0","browser_version":"94.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}'
            )

        def heartbeatThread(self, interval):
            try:
                while True:
                    self.send('{"op":1,"d":' + str(self.packets_recv) + "}")
                    time.sleep(interval)
            except Exception as e:
                return

        def sock_message(self, ws, message, onlyonlinemember):
            try:
                decoded = json.loads(message)
                if decoded is None:
                    return
                if decoded["op"] != 11:
                    self.packets_recv += 1
                if decoded["op"] == 10:
                    threading.Thread(
                        target=self.heartbeatThread,
                        args=(decoded["d"]["heartbeat_interval"] / 1000,),
                        daemon=True,
                    ).start()
                if decoded["t"] == "READY":
                    for guild in decoded["d"]["guilds"]:
                        self.guilds[guild["id"]] = {"member_count": guild["member_count"]}
                if decoded["t"] == "READY_SUPPLEMENTAL":
                    self.ranges = self.getRanges(
                        0, 100, self.guilds[self.guild_id]["member_count"]
                    )
                    self.scrapeUsers()
                elif decoded["t"] == "GUILD_MEMBER_LIST_UPDATE":
                    parsed = self.parseGuildMemberListUpdate(decoded)
                    self.msgs.append(len(self.members))
                    print(f"Scraped {len(self.members)} members", end="\r")
                    if self.d == len(self.members):
                        self.iter += 1
                        if self.iter == self.MAX_ITER:
                            print(f"Scraped {len(self.members)} members")
                            self.endScraping = True
                            self.close()
                            return
                    self.d = self.find_most_reoccuring(self.msgs)
                    if parsed["guild_id"] == self.guild_id and (
                        "SYNC" in parsed["types"] or "UPDATE" in parsed["types"]
                    ):
                        for (elem, index) in enumerate(parsed["types"]):
                            if index == "SYNC":
                                for item in parsed["updates"]:
                                    if len(item) > 0:
                                        for member in item:
                                            if "member" in member:
                                                mem = member["member"]
                                                obj = {
                                                    "tag": mem["user"]["username"]
                                                    + "#"
                                                    + mem["user"]["discriminator"],
                                                    "id": mem["user"]["id"],
                                                }

                                                if onlyonlinemember == 'True':
                                                    if not mem["user"].get("bot") and (mem["presence"]["status"] == "online" or mem["presence"]["status"] == "idle" or mem["presence"]["status"] == "dnd"):
                                                        self.members.append(str(mem["user"]["id"]))
                                                else:
                                                    if not mem["user"].get("bot"):
                                                        self.members.append(str(mem["user"]["id"]))


                            elif index == "UPDATE":
                                for item in parsed["updates"][elem]:
                                    if "member" in item:
                                        mem = item["member"]
                                        obj = {
                                            "tag": mem["user"]["username"]
                                            + "#"
                                            + mem["user"]["discriminator"],
                                            "id": mem["user"]["id"],
                                        }
                                        if onlyonlinemember == 'y':
                                            if not mem["user"].get("bot") and (mem["presence"]["status"] == "online" or mem["presence"]["status"] == "idle" or mem["presence"]["status"] == "dnd"):
                                                self.members.append(str(mem["user"]["id"]))
                                        else:
                                            if not mem["user"].get("bot"):
                                                self.members.append(str(mem["user"]["id"]))
                            self.lastRange += 1
                            self.ranges = self.getRanges(
                                self.lastRange, 100, self.guilds[self.guild_id]["member_count"]
                            )
                            time.sleep(0.45)
                            self.scrapeUsers()
                    if self.endScraping:
                        print(f"Scraped {len(self.members)} members")
                        self.close()
            except Exception as e:
                print(e)
                
    def scrape_members(token, guild_id, channel_id, onlyonlinemember):
        return DiscordSocket(token, guild_id, channel_id, onlyonlinemember).run()

    def runthread(func, *args_list):
        tokens = open("tokens.txt", "r").read().splitlines()
        threads = []

        for token in tokens:
            thread = threading.Thread(target=func, args=(token, *args_list))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    
    @bot.command()
    async def check(ctx):
        await ctx.message.delete()
        lock = threading.Lock()
        def success(text):
            lock.acquire()
            console.log('valid', text)
            lock.release()

        def invalid(text):
            lock.acquire()
            console.log('invalid', text)
            lock.release()

        with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
        def save_tokens():
            with open("tokens.txt", "w") as f: f.write("")
            for token in tokens:
                with open("tokens.txt", "a") as f: f.write(token + "\n")
        def removeDuplicates(file):
            lines_seen = set()
            with open(file, "r+") as f:
                d = f.readlines(); f.seek(0)
                for i in d:
                    if i not in lines_seen: f.write(i); lines_seen.add(i)
                f.truncate()
        def check_token(token:str):
            session = tls_client.Session(client_identifier=f"chrome_124", random_tls_extension_order=True)
            response = session.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="})
            if response.status_code == 200: success(f"{token[:26]}")
            else: tokens.remove(token); invalid(f"{token[:26]}")
        def check_tokens():
            threads=[]
            for token in tokens:
                try:threads.append(threading.Thread(target=check_token, args=(token,)))
                except Exception as e: pass
            for thread in threads: thread.start()
            for thread in threads: thread.join()
        def tokenchecker():
            removeDuplicates("tokens.txt")
            check_tokens()
            save_tokens()

        tokenchecker()
        console.log('All Tokens have been Checked!')
        console.push('All Tokens have been Checked!')

    @bot.command()
    async def reaction(ctx, emoji=None, channel_id=None, message_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        rg = re.compile(r"^https:\/\/(ptb.|canary.|)discord.com\/channels\/\d+\/\d+\/\d+$")
        if rg.match(channel_id):
            message_id = channel_id.split("/")[6]
            channel_id = channel_id.split("/")[5]
        elif emoji is None:
            message_id = settings["reaction"]["messageid"]
            channel_id = settings["reaction"]["channelid"]
        settings["reaction"]["messageid"] = message_id
        settings["reaction"]["channelid"] = channel_id
        save_settings(settings)
        settings=reloadsettings()
        runthread(addreaction, emoji, channel_id, message_id)

    @bot.command()
    async def button(ctx, number=None, channel_id=None, guild_id=None, message_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        rg = re.compile(r"^https:\/\/(ptb.|canary.|)discord.com\/channels\/\d+\/\d+\/\d+$")
        if rg.match(channel_id):
            guild_id = channel_id.split("/")[4]
            message_id = channel_id.split("/")[6]
            channel_id = channel_id.split("/")[5]
        elif number is None:
            number = settings["button"]["number"]
            message_id = settings["button"]["messageid"]
            channel_id = settings["button"]["channelid"]
            guild_id = settings["button"]["serverid"]
        else:
            if channel_id is None:
                channel_id = str(ctx.channel.id)
                guild_id = str(ctx.guild.id)
            elif guild_id is None:
                guild_id = str(ctx.guild.id)
        settings["button"]["number"] = number
        settings["button"]["messageid"] = message_id
        settings["button"]["channelid"] = channel_id
        settings["button"]["serverid"] = guild_id
        save_settings(settings)
        settings=reloadsettings()
        try:
            message = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1&around={message_id}", headers={'Authorization': TOKEN}).json()[0]
            buttons = []
            if len(message["components"]) == 0:
                console.log('0 buttons found!')
            else:
                for component in message["components"]:
                    for button in component["components"]:
                        buttons.append({
                            "label": button.get("label"),
                            "custom_id": button["custom_id"],
                            "application_id": message["author"]["id"],
                        })
                for button in buttons:
                    if buttons.index(button)==int(number)-1:
                        custom_id = button['custom_id']
                        application_id = button['application_id']
                        runthread(click_button, guild_id, channel_id, message_id, custom_id, application_id)
                    else:
                        console.log('Button not found')
        except Exception as e:
            print(e)

    @bot.command()
    async def spam(ctx, message=None, delay=None, channel_id=None, guild_id=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if message is None:
            message = settings["spam"]["message"]
            channel_id = settings["spam"]["channelid"]
            guild_id = settings["spam"]["serverid"]
            delay = settings["spam"]["delay"]
        else:
            if delay is None:
                delay = 0
            if channel_id is None:
                channel_id = str(ctx.channel.id)
                guild_id = str(ctx.guild.id)
            elif guild_id is None:
                guild_id = str(ctx.guild.id)
        try: delay = int(delay)
        except: delay = 0
        settings["spam"]["message"] = message
        settings["spam"]["channelid"] = channel_id
        settings["spam"]["serverid"] = guild_id
        settings["spam"]["delay"] = delay
        save_settings(settings)
        settings=reloadsettings()
        if settings["spam"]["massping"]["type"] == "True" or settings["spam"]["massping"]["type"] == "true":
            onlyonlinemember = settings["spam"]["massping"]["onlyonline"]     
            users = scrape_members(TOKEN, guild_id, channel_id, onlyonlinemember)
            with open(f"scraped/{guild_id}.txt", "w") as f:
                for user in users:
                    f.write(f"<@{user}>\n")
            print(f"Scraped {len(users)} users")
            print(f"Saved to scraped/{guild_id}.txt")
        for token in tokens:
            thread = threading.Thread(target=spamchannel, args=(token, delay, channel_id, message, guild_id))
            thread.start()

    @bot.command()
    async def massspam(ctx, message=None, delay=None, guild_id=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if message is None:
            message = settings["massspam"]["message"]
            guild_id = settings["massspam"]["serverid"]
            delay = settings["massspam"]["delay"]
        else:
            if delay is None:
                delay = 0
            if guild_id is None:
                guild_id = str(ctx.guild.id)
        try: delay = int(delay)
        except: delay = 0
        channellist = []

        response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers={'Authorization': TOKEN})

        if response.status_code == 200:
            channels = response.json()
            for channel in channels:
                channellist.append(channel["id"])

            settings["massspam"]["message"] = message
            settings["massspam"]["channelids"] = channellist
            settings["massspam"]["serverid"] = guild_id
            settings["massspam"]["delay"] = delay
            save_settings(settings)
            settings=reloadsettings()
            if settings["massspam"]["massping"]["type"] == "True" or settings["massspam"]["massping"]["type"] == "true":
                onlyonlinemember = settings["massspam"]["massping"]["onlyonline"]     
                channel = random.choice(channellist)
                users = scrape_members(TOKEN, guild_id, channel, onlyonlinemember)
                with open(f"scraped/{guild_id}.txt", "w") as f:
                    for user in users:
                        f.write(f"<@{user}>\n")
                print(f"Scraped {len(users)} users")
                print(f"Saved to scraped/{guild_id}.txt")
            channel_ids = settings["massspam"]["channelids"]
            for token in tokens:
                for channel_id in channel_ids:
                    thread = threading.Thread(target=spammasschannel, args=(token, delay, channel_id, message, guild_id))
                    thread.start()

        else:
            print(f'Failed to fetch channels: {response.status_code} - {response.text}')
            print(response.text)

    @bot.command()
    async def vc(ctx, channel_id=None, guild_id=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if channel_id is None:
            channel_id = settings["voicecall"]["channelid"]
            guild_id = settings["voicecall"]["serverid"]
        settings["voicecall"]["channelid"] = channel_id
        settings["voicecall"]["serverid"] = guild_id
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=voicecall, args=(token, channel_id, guild_id))
            thread.start()

    @bot.command()
    async def online(ctx):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=onliner, args=(token,))
            thread.start()

    @bot.command()
    async def poll(ctx, delay = None, channel_id=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if delay is None and channel_id is None:
            channel_id = settings["poll"]["channelid"]
            delay = settings["poll"]["delay"]
        elif delay is None:
            delay = 0
        if channel_id is None:
            channel_id = str(ctx.channel.id)

        try: delay = int(delay)
        except: delay = 0
        settings["poll"]["channelid"] = channel_id
        settings["poll"]["delay"] = delay
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=poll_spam, args=(token, channel_id, delay))
            thread.start()

    @bot.command()
    async def join(ctx, invite=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        config=reloadconfig()
        if invite is None:
            try:
                if ctx.author.guild_permissions:
                    channel_id = str(ctx.channel.id)
                    json_data = {
                        'validate': None,
                        'max_age': 0,
                        'max_uses': 0,
                        'target_user_id': None,
                        'target_type': None,
                        'temporary': False,
                    }

                    response = requests.post(
                        f'https://discord.com/api/v9/channels/{channel_id}/invites',
                        headers= {'authorization': TOKEN},
                        json=json_data,
                    ).json()
                    invite = response["code"]
            except:
                invite = settings["join"]["invite"]
                
        invite = invite.replace("https://discord.gg/", "").replace("https://discord.com/invite/", "").replace("discord.gg/", "").replace("https://discord.com/invite/", "")
        settings["join"]["invite"] = invite
        save_settings(settings)
        try:
            res = requests.get(f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true").json()
            runthread(accept_invite, invite, res['guild']['id'], res['channel']['id'], res['channel']['type'])
        except:
            console.log('Your ip address blocked!')

    @bot.command()
    async def leave(ctx, guild_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if guild_id is None:
            try: 
                guild_id = str(ctx.guild.id)
            except:
                guild_id = settings["leave"]["serverid"]
        settings["leave"]["serverid"] = guild_id
        save_settings(settings)
        runthread(leaveserver, guild_id)
            
    @bot.command()
    async def boost(ctx, guild_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if guild_id is None:
            try:
                guild_id = str(ctx.guild.id)
            except:
                guild_id = settings["boost"]["serverid"]
        settings["boost"]["serverid"] = guild_id
        save_settings(settings)
        runthread(booster, guild_id)

    @bot.command()
    async def unfriend(ctx, user_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if user_id is None: 
            user_id = settings["unfriend"]["userid"]
        settings["unfriend"]["userid"] = user_id
        save_settings(settings)
        runthread(unfrienduser, user_id)

    @bot.command()
    async def friend(ctx, username=None):
        await ctx.message.delete()
        settings = reloadsettings()
        if username is None:
            username = settings["friend"]["username"]
        settings["friend"]["username"] = user_id
        save_settings(settings)
        runthread(frienduser, username)

    @bot.command()
    async def typing(ctx, channel_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        tokens = open("tokens.txt", "r").read().splitlines()
        if channel_id is None:
            try:
                channel_id = str(ctx.channel.id)
            except:
                channel_id = settings["typing"]["channelid"]
        settings["typing"]["channelid"] = channel_id
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=typer, args=(channel_id, token))
            thread.start()

    @bot.command()
    async def dm(ctx, user_id=None, message=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if user_id is None:
            user_id = settings["dm"]["userid"]
            message = settings["dm"]["message"]
        settings["dm"]["userid"] = user_id
        settings["dm"]["message"] = message
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=open_dms, args=(user_id, token, message))
            thread.start()


    @bot.command()
    async def call(ctx, user_id=None):
        await ctx.message.delete()
        tokens = open("tokens.txt", "r").read().splitlines()
        settings=reloadsettings()
        if user_id is None:
            user_id = settings["call"]["userid"]
        settings["call"]["userid"] = user_id
        save_settings(settings)
        for token in tokens:
            thread = threading.Thread(target=open_call, args=(user_id, token))
            thread.start()

    @bot.command()
    async def nick(ctx, nickname=None, guild_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if nickname is None:
            nickname = settings["nick"]["nickname"]
            guild_id = settings["nick"]["serverid"]
        elif guild_id is None:
            guild_id = str(ctx.guild.id)
        settings["nick"]["nickname"] = nickname
        settings["nick"]["serverid"] = guild_id
        save_settings(settings)
        runthread(changenick, guild_id, nickname)

    @bot.command()
    async def fun(ctx, channel_id=None, message_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        time.sleep(0.5)
        if channel_id is None:
            try:
                channel_id = str(ctx.channel.id)
            except:
                channel_id = settings["fun"]["channelid"]
        if message_id is None:
            message = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1",headers= {'authorization': TOKEN}).json()
            for message in message:
                message_id = message.get('id')
        settings["fun"]["channelid"] = channel_id
        save_settings(settings)
        runthread(funnycommand1, channel_id, message_id)

    @bot.command()
    async def vaultcord(ctx, botid=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if botid is None:
            botid = settings["vaultcord"]["botid"]
        settings["vaultcord"]["botid"] = botid
        save_settings(settings)
        runthread(bypass, botid)

    @bot.command()
    async def message(ctx, message, channel_id=None):
        await ctx.message.delete()
        settings=reloadsettings()
        if message is None:
            message = settings["message"]["message"]
            channel_id = settings["message"]["channelid"]
        elif channel_id is None:
            channel_id = str(ctx.channel.id)
        settings["message"]["message"]
        settings["message"]["channelid"]
        save_settings(settings)
        runthread(spam1, message, channel_id)

    @bot.command()
    async def calc(ctx, *, expression):
        await ctx.message.delete()
        try:
            result = eval(expression)
            await ctx.send(f'**{result}**')
        except:
            await ctx.send('Invalid expr')


    @bot.command(aliases=['ltcbal'])
    async def getltcbal(ctx, ltcaddress):
        await ctx.message.delete()
    
        response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
        if response.status_code == 200:
            data = response.json()
            balance = data['balance'] / 10**8  
            total_balance = data['total_received'] / 10**8
            unconfirmed_balance = data['unconfirmed_balance'] / 10**8
        else:
            await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
            return

        cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        if cg_response.status_code == 200:
            usd_price = cg_response.json()['litecoin']['usd']
        else:
            await ctx.send("Failed to retrieve the current price of Litecoin.")
            return
        
        usd_balance = balance * usd_price
        usd_total_balance = total_balance * usd_price
        usd_unconfirmed_balance = unconfirmed_balance * usd_price
        
        message = f"LTC Address: `{ltcaddress}`\n"
        message += f"Current LTC: **${usd_balance:.2f} USD**\n"
        message += f"Total LTC Received: **${usd_total_balance:.2f} USD**\n"
        message += f"Unconfirmed LTC: **${usd_unconfirmed_balance:.2f} USD**"
        
        response_message = await ctx.send(message)
        
        time.sleep(60)
        await response_message.delete()

    @bot.command(aliases=['btcbal'])
    async def getbtcbal(ctx, btcaddress):
        await ctx.message.delete()
        
        response = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{btcaddress}/balance')
        if response.status_code == 200:
            data = response.json()
            balance = data['balance'] / 10**8  
            total_balance = data['total_received'] / 10**8
            unconfirmed_balance = data['unconfirmed_balance'] / 10**8
        else:
            await ctx.send("Failed to retrieve balance. Please check the Bitcoin address.")
            return

        cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        if cg_response.status_code == 200:
            usd_price = cg_response.json()['bitcoin']['usd']
        else:
            await ctx.send("Failed to retrieve the current price of Bitcoin.")
            return
        
        usd_balance = balance * usd_price
        usd_total_balance = total_balance * usd_price
        usd_unconfirmed_balance = unconfirmed_balance * usd_price
        
        message = f"BTC Address: `{btcaddress}`\n"
        message += f"Current BTC: **${usd_balance:.2f} USD**\n"
        message += f"Total BTC Received: **${usd_total_balance:.2f} USD**\n"
        message += f"Unconfirmed BTC: **${usd_unconfirmed_balance:.2f} USD**"
        
        response_message = await ctx.send(message)
                        
        time.sleep(60)
        await response_message.delete()

    @bot.command(aliases=['ethbal'])
    async def getethbal(ctx, ethaddress):
        await ctx.message.delete()
        response = requests.get(f'https://api.blockcypher.com/v1/eth/main/addrs/{ethaddress}/balance')
        if response.status_code == 200:
            data = response.json()
            balance = data['balance'] / 10**8  
            total_balance = data['total_received'] / 10**8
            unconfirmed_balance = data['unconfirmed_balance'] / 10**8
        else:
            await ctx.send("Failed to retrieve balance. Please check the Bitcoin address.")
            return

        cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        if cg_response.status_code == 200:
            usd_price = cg_response.json()['ethereum']['usd']
        else:
            await ctx.send("Failed to retrieve the current price of Bitcoin.")
            return
        
        usd_balance = balance * usd_price
        usd_total_balance = total_balance * usd_price
        usd_unconfirmed_balance = unconfirmed_balance * usd_price
        
        message = f"ETH Address: `{ethaddress}`\n"
        message += f"Current ETH: **${usd_balance:.2f} USD**\n"
        message += f"Total ETH Received: **${usd_total_balance:.2f} USD**\n"
        message += f"Unconfirmed ETH: **${usd_unconfirmed_balance:.2f} USD**"
        
        response_message = await ctx.send(message)
        
        time.sleep(60)
        await ctx.response_message.delete()

        await ctx.send(response)

    @bot.command()
    async def ltc(ctx):
        await ctx.message.delete()
        config = reloadconfig()
        try:
            ltcaddress = config["bal"]["ltc"]
            await ctx.send(ltcaddress)
        except: None

    @bot.command()
    async def eth(ctx):
        await ctx.message.delete()
        config = reloadconfig()
        try:
            ethaddress = config["bal"]["eth"]
            await ctx.send(ethaddress)
        except: None

    @bot.command()
    async def btc(ctx):
        await ctx.message.delete()
        config = reloadconfig()
        try:
            btcaddress = config["bal"]["btc"]
            await ctx.send(btcaddress)
        except: None

    @bot.command()
    async def addy(ctx):
        await ctx.message.delete()
        config = reloadconfig()
        try:
            btcaddress = config["bal"]["btc"]
            ethaddress = config["bal"]["eth"]
            ltcaddress = config["bal"]["ltc"]
            response = f"""
**Litecoin address (LTC)** : {ltcaddress}
**Bitcoin address (BTC)**: {btcaddress}
**Ethereum address (ETH)**: {ethaddress}"""
            await ctx.send(response)
        except: None

    @bot.command()
    async def stop(ctx):
        await ctx.message.delete()
        global stop_spam
        stop_spam = True
    @bot.command()
    async def clear(ctx):
        await ctx.message.delete()
        os.system('cls')
        print(f'Client ready! Active with name: {bot.user.name}')

        console.log('Console has been cleared!')
    @bot.command()
    async def cls(ctx):
        await ctx.message.delete()
        os.system('cls')
        print(f'Client ready! Active with name: {bot.user.name}')

        console.log('Console has been cleared!')

    @bot.command()
    async def change(ctx, TOKEN):
        await ctx.message.delete()
        key = b'\xc6Y\xb2M\x8b\xf6\xe1\x98K\x8e\xfa|}~\xbb\xa9\xc7\xa1\xe5Y\x9e\xaf[$%\x12\xd4\xb4Q\xc9\xb3\xa3'
        iv = b'\x9c\xb17\x98\x07\x91\x1a\xf0\xb3"\xb3\xb83\xbd2*'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(TOKEN.encode(), AES.block_size))
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        path = os.path.join(os.getenv('APPDATA'), 'Skid', 'user.json')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'r', encoding='utf-8') as file:
            user = json.load(file)
        user['tokenencode'] = ct
        with open(path, 'w') as file:
            json.dump(user, file, indent=4)

        console.push('Stop in 3s... Reopen it')
        console.log('Stop in 3s... Reopen it')
        time.sleep(3)
        os.kill(os.getpid(), 15)

    @bot.command()
    async def key(ctx, key):
        await ctx.message.delete()
        path = os.path.join(os.getenv('APPDATA'), 'Skid', 'user.json')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'r', encoding='utf-8') as file:
            user = json.load(file)
        user['license'] = key
        with open(path, 'w') as file:
            json.dump(user, file, indent=4)

        console.push('Stop in 3s... Reopen it')
        console.log('Stop in 3s... Reopen it')
        time.sleep(3)
        os.kill(os.getpid(), 15)

    @bot.command()
    async def exit(ctx):
        await ctx.message.delete()
        os.kill(os.getpid(), 15)

        
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Error: Command not found. Please use .help to see the list of available commands.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Error: Missing arguments. Usage: .{ctx.command} {ctx.command.signature}")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Error: Bad argument. Usage: .{ctx.command} {ctx.command.signature}")
        else:
            await ctx.send(f"An error occurred: {str(error)}")

    bot.run(TOKEN, bot=False)

except discord.errors.LoginFailure:
    console.log('Token Invalid')
    console.push('Token Invalid')
    TOKEN = input("input your discord token: ")
    key = b'\xc6Y\xb2M\x8b\xf6\xe1\x98K\x8e\xfa|}~\xbb\xa9\xc7\xa1\xe5Y\x9e\xaf[$%\x12\xd4\xb4Q\xc9\xb3\xa3'
    iv = b'\x9c\xb17\x98\x07\x91\x1a\xf0\xb3"\xb3\xb83\xbd2*'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(TOKEN.encode(), AES.block_size))
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    path = os.path.join(os.getenv('APPDATA'), 'Skid', 'user.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'r', encoding='utf-8') as file:
        user = json.load(file)
    user['tokenencode'] = ct
    with open(path, 'w') as file:
        json.dump(user, file, indent=4)
    console.push('Stop in 3s... Reopen it')
    console.log('Stop in 3s... Reopen it')
    time.sleep(3)
    os.kill(os.getpid(), 15)
