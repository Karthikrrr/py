try:
	print("done")
	with open("boss.txt","r")as re:
		with open("boss1.txt","w")as wr:
			for i in re:	
				wr.write(i)
except Exception as e:
	print(e)

try :
	with open("boss.txt","r") as readfile:
		with open("boss1.txt","r") as writefile:
			for i in readfile:
				writefile.write(z)

#except IOError:
#	print("io error")
#except FileNotFoundError:
#	print("not file")
#except io.UnsupportedOpertaion:
#	print("no support")
#except ValueError:
#	print("val")
except NameError:
	print("name error")
else:
	print("all good")
