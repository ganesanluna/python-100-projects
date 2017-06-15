_author="BalaGanesan"
import hashlib
i = int(raw_input("hashing value : "))
e=raw_input("enter your password : ")
while i >= 0:
	a=hashlib.md5(str(e)).hexdigest()
	b=hashlib.sha1(str(a)).hexdigest()
	c=hashlib.sha224(str(b)).hexdigest()
	d=hashlib.sha384(str(c)).hexdigest()
	e=hashlib.sha512(str(d)).hexdigest()	
	i = i - 1
print e

	
