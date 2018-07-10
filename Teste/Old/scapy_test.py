#!/usr/bin/python3

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

# test call
var=[] 

for i in range(1, 255):

	s=str(i)
	h='10.1.1.'
	h += s
	
	var.append(ping(h))
	
for a in range (0, len(var)):
	tt = var[a]
	if (tt == True):
		print ("Host ",a," Está UP!")
	


