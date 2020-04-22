import os, sys, hashlib

hashed_code = ('32250170a0dca92d53ec9624f336ca24')
hex = hashlib.md5()

def repeat():
	global hex
	while hex.hexdigest() != hashed_code:
		hex = hashlib.md5()			
		hex.update(input('code >>\\').encode())		
		print('<<\nNone ??{}\n>>\\'.format(hex.hexdigest()))
		continue
		if input  == 'exit\\':
			sys.exit()
			break
	print('<<\n{}\nyou have been given authority\n>>\\'.format(hex.digest()))
	os.system(hashed_code)
	return

if __name__ == "__main__":
	repeat()
