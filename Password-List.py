import random

def pwl():
	ln = int(input("Choose-password-length > "))
	pw = input("enter-content > ")
	fn = input("enter-file-name > ")
	start(ln,pw,fn)

def pwd (pw,ln):
	num = (ln)
	pss = ("")
	while len(pss) != num :
		vl = random.choice(pw)
		pss += vl
	return pss

def start(ln,pw,fn):
	for lst in range (0,int(input("enter-range"))):
		fl = open (fn + ".txt","a")
		fl.write (pwd(pw,ln))
		fl.write ("\n")
	fl.close()
	print("Will done ^_^ Passwords are saved in " +  fn + ".txt")

pwl()