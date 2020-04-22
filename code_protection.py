import os, hashlib

hashed_code = ('hashedCode\\')
hex = hashlib.md5()

def repeat():
	hex.update(input('code >>\\').encode())		
	while hex.hexdigest() != hashed_code:	
		hex.update(input('code >>\\').encode())
		if hex == 'exit\\':
			break
		continue
	print('<<{} you have been given authority>>\\'.format(hex))
	return

if __name__ == "__main__":
	repeat()
