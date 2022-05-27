import sys
d=dict()
class emp:
	#start 1
	def input(self):
		#start 2
		self.name=input("enter name")
		self.basi=int(input("enter basic"))
		self.TDS=int(input("enter tds"))
		self.deduct=int(input("enter deduct"))
		self.HRA=int(input("enter hra"))
		self.DA=int(input("enter DA"))

		self.grossSalary=self.basi+self.HRA+self.DA+self.TDS
		self.netSalary=self.grossSalary-self.deduct
		self.addEmp()
		
		#end 2
	def addEmp(self):
		#start 3
		d.update({self.name:{self.name,self.netSalary}})
		#end 3
	def prin(self):
		print(d)
	
	def search(self):
		name=input("enter to ser")
		for i in d:
			if(name==i):
				print(d.get(i))	
			else:	
				print("not founf")
#end  1
while True:
	e=emp()
	ch=int(input("enter choice"))
	
	if(ch==1):
		e.input()
	elif(ch==2):
		e.prin()
	else:
		e.search()
