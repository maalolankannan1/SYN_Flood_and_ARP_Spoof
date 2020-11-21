import os
import time
import re
import keyboard

def arp_spoof():
    os.system('arp -a > .arp_dump')
    mac_list = []
    with open(".arp_dump","r") as f:
        for line in f.readlines():
            mac_add = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}([0-9A-Fa-f]{1,2})', line, re.I).group()
            if mac_add not in mac_list:
                mac_list.append(mac_add)
            else:
                print(mac_add)
                return mac_add,True
    os.system('rm .arp_dump')
    return "",False

def main():
    print("Installing arptables")
    os.system('apt-get install arptables')
    print('To end press "s" key')
    while True:
        if keyboard.is_pressed('s'):
            break
        add,out = arp_spoof()
        if(out):
            print("{}ARP Poisoning Detected".format('\033[1;31m'))
        else:
            print("{}Safe from ARP Spoofing".format('\033[1;32m'))
        time.sleep(1)

if __name__ == '__main__':
    main()