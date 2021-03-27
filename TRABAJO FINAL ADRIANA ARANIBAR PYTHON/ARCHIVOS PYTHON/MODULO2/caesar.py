import sys
import string

alfabeto = string.ascii_lowercase
if len(sys.argv) == 2:
	if sys.argv[1].isnumeric():
		k = int(sys.argv[1]) 
		if k > 0:
			pl=input("plaintext: ")
			ci=""
			for l in pl:
				if l.lower() in alfabeto:
					p=alfabeto.find(l.lower())
					c=(p+k)%26
					if l.islower():
						ci+=alfabeto[c]
					else:
						ci+=alfabeto[c].upper()
				else:
					ci+=l
			print("ciphertext: ",ci)
			print(0)
		else:
			print("The key argument must be an integer greater than 0")
			print(1)
	else:
		print("The key argument must be an integer greater than 0")
		print(1)
else:
	print("Usage caesar.py key")
	print(1)
