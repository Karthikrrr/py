class student:
	def __init__(self,name=0,usn=0,age=0):
		#start
		self.usn=usn
		self.name=name
		self.age=age
	def getData(self):
		self.name=input("enter name")
		self.usn=input("enter usn")
		self.age=input("enter age")
	def display(self):
		print("name is ",self.name)
		print("age is ",self.age)
		print("usn is ",self.usn)

class ugStudent(student):
	def __init__(self,sem=0,fee=0):
		super().__init__()
		self.sem=sem
		self.fee=fee
	def getug(self):
		super().getData()
		#self.sem=input("ente sem")
		self.fee=input("enter fee")	
	def ugDis(self):
		super().display()
		print(self.fee)
		print(self.sem)

class pgStudent(student):
        def __init__(self,sem=0,fee=0):
                super().__init__()
                self.sem=sem
                self.fee=fee
        def getpg(self):
                super().getData()
                #self.sem=input("ente sem")
                self.fee=input("enter fee")     
        def pgDis(self):
                super().display()
                print(self.fee)
                print(self.sem)		


while True:
	ch=input("ente choice")
	if(ch==1):
		s=ugStudent()
		s.getug()
		s.ugDis()
		d[s.name]=s.__dict__
	elif (ch==2):
		pg=pgStudent()
		pg.getpg()
		pg.pgDis()
	else :
		print(d)
