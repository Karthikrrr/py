class magic:
	def __init__(self):
		self.l=[]
	def inpu(self):
		n=int(input("enter digit"))
		for i in range(0,n):
			x=int(input("enter number"))
			self.l.append(x)
	def __add__(self,other):
		ans=[]
		if len(self.l)==len(other.l):
			for i in range(len(self.l)):
				ans.append(self.l[i]+other.l[i])
			print(ans)

	def __sub__(self,other):
		ans=[]
		for i in (range(len(self.l))):
			ans.append(self.l[i]-other.l[i])
		print(ans)
	
	def __truediv__(self,other):
		ans=[]
		for i in range(len(self.l)):
			ans.append(self.l[i]/other.l[i])
		print(ans)
