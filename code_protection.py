import os, hashlib

hashed_code = ('hashed_Code\\')
hex = hashlib.md5()

def repeat():		
	while hex.hexdigest() != hashed_code:
		hex.update(input('code >>\\').encode())		
		print('<<\nNone ??{}\n>>\\'.format(hex.hexdigest()))
		continue
		if input  == 'exit\\':
			break
	print('<<\n{}\nyou have been given authority\n>>\\'.format(hex))
	return

if __name__ == "__main__":
	repeat()
