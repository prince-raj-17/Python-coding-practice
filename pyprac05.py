print(10>9)
print(10==9)
print(10<9)

a = 10
b = 9

if b>a:
	print("b is greate rthan a")
if b<a:
	print("b is smaller than a")

print(bool("hello"))
x="hii"
print(bool(x))

print(bool(""))
print(bool(None))

class myclass():
	def __len__(self):
		return 0

x = myclass()
print(bool(x))

def myFunction():
	return True

if myFunction():
	print("yes!")
else:
	print("no!")

x=20
print(isinstance(x,int))

x=3
y=4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

x=5
x **=2
print(x)

x=2
y=3

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

x=5
print(x>2 and x<7)
print(x>6 and x<3)

a=3
print(a<1 or a<4)

b=4
print(not(b==4))

x=2
y=2

print(x is y)
print(x is not y)

fruits=["apple","banana"]
print("apple" in fruits)
print("cherry" not in fruits)