class empl:
	def __init__(self,name=0,age=0,pay=0):
		self.name=input("enter name")
		self.age=input("age")
		self.pay=input("enter pay")
	def pays(self):
		rais=100
		self.total=self.pay*self.rais
		print(self.total)
class manager(empl):
	rais=1
	def pays(self):
		self.total=self.pay*self.rais
		print(self.total)
class dev(empl):
	rais=99
	def pays(self):
		self.total=self.pay*self.rais
		print(self.total)
m1=manager()
m1.pays()
