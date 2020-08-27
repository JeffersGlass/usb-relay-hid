#relayTest.py

import sys, os, time
import ctypes
from relayUtils import *

def jtest():
	closeAllRelays()
	time.sleep(1)
	openAllRelays()
	time.sleep(1)

	closeRelay(1)
	time.sleep(1)
	openRelay(1)
	time.sleep(1)

def ctest():
	relays = relayBoard(4)
	relays.loadLib()


def main():
	print("Starting test")
	ctest()
	print("Ending test")


'''def main():
	print("Test 4-ch relay")
	loadLib()
	getLibFunctions()
	try:
		print("Searching for compatible devices")
		global devids
		devids = enumDevs()
		if len(devids) != 0 :
			# Test any 1st found dev .
			print("Testing relay with ID=" + devids[0])
			openDevById(devids[0])
			ctest()
			closeDev()
	finally:  
		unloadLib()'''

if __name__ == "__main__" :
  main()