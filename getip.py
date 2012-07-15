#! /usr/bin/env python
#coding=utf-8

import sys
import socket
import re

def getip(domain):
	ip = socket.gethostbyname(domain)
	#return ip
	print ip

if __name__ == '__main__' :
	if len(sys.argv) != 2:
		print 'Error: please supply a domain.'
		raise SystemExit(1)
	getip(sys.argv[1])
	
	