import time
def cal(func):
	def sub():
		start=time.time()
		result=func()
		end=time.time()
		print("end is ",start-end)
		return result
	return sub

@cal
def fib(a=0,b=1):
	while True:
		yield a
		a,b=b,a+b
f=fib()
n=int(input("enter value"))
for i in range(n):
	print(next(f))
