# SYN-ARP ATTACKER AND ARP DETECTOR TOOL
A python Tool to generate SYN_Flood and ARP_Spoofing Attacks and Detect ARP_Spoofing Attacks

**DONE BY:**
1.  Maalolan K
2.  Somesh Kirthik
3.  Divya Kannan

## FEATURES:
* This tool can successfully create SYN-Flood Attack on any client in the same network and stall its resources as long as the User wants. It gives a flexibility to the number of attacks to be performed per iteration and also asks the user whether they want to continue the attack or not.
* This tool can also generate an ARP Spoofing attack. It gives a choice for the user to select either the SYN-Flood Attack or the ARP Spoofing Attack. If the user chooses the ARP Spoofing Attack and the IP address on which to attack, the user system will start sending ARP Packets continuously to the victim OS. The user now acts as a man-in-the-middle attacker and thus can intercept the traffic on the victim OS.
* There is another tool created to help detect the presence of ARP Attacks on the User OS. Once this tool is run, it continuously checks for an ARP attack. The user is shown the status through the terminal.

**In this project, we are going to be generating the two attacks mentioned, namely, SYN Flood attack and ARP spoofing attack. With this we will understand how the attack is carried out from both sides, the attacker and the victim. Apart from this, we will also create a tool to detect ARP spoofing which will be helpful in finding out such vulnerabilities.**

## PREREQUISITES:

* Attacker OS:
  1.  Nmap
  2.  Python 3
  3.  Scapy Python library
  4.  Subprocess Python library
  
* Victim OS:
  1.  Python3

## TO USE:

* For SYN FLOOD Attack:
  Run 'SYN_ARP.py' and choose 1.
* For ARP SPOOFING Attack:
  Run 'SYN_ARP.py' and choose 2.
* For ARP SPOOF DETECTION Tool:
  Run 'arp_detect.py'

##  BLOCK DIAGRAMS:

* **SYN_ARP ATTACKER:**

<p>
<img src="https://github.com/maalolankannan1/SYN_Flood_and_ARP_Spoof/blob/main/DCN_Attack.jpg", alt="Syn_Arp Attacker Tool">
</p>

* **ARP DETECTION:**

<p>
<img src="https://github.com/maalolankannan1/SYN_Flood_and_ARP_Spoof/blob/main/DCN_Detect.jpg", alt="Syn_Arp Attacker Tool">
</p>
