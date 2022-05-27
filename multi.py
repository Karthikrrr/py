class student:
	def __init__(self,name=0,age=0,usn=0):
		self.name=name
		self.age=age
		self.usn=usn
	def display(self):
		print(self.name)
		print(self.age)
		print(self.usn)

class mca(student):
	def __init__(self):
		student.__init__(self)
		self.usn=input("enter name")
		self.age=input("enter age:")
		self.name=input("enter name")
	def dis(self):
		student.display(self)
		self.sub1=input("enter sub1")
		self.sub2=input("enter sub2")
		self.total=self.sub1+self.sub2
		print(self.total)
	
class bsec(mca):
	def __init__(self):
		mca.__init__(self)
		mca.dis(self)	
		self.percent=self.total/2
		print(self.precent)
	def fidis(self):
		print("Aa")		
		
		
s=bsec()	
