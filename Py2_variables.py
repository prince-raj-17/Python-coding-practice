x=5
y="john"
print(x)
print(y)

x=4#x is int here
x="sally"#x is str here
print(x)
#variables are interconvertible.

a="john"
print(a)
a='john'
print(a)

myvar='john'
print(myvar)
my_var = "Joseph"
print(my_var)
#these are legal variable names.

x,y,z='apple',"mango","cherry"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

x="awesome"
print("python is "+x)

x="python is "
y="awesome"
z=x+y
print(z)

x=1
y=6
print(x+y)

x='awesome'

def myfunc():
	print('python is '+x)
myfunc()

def myfunc():
	x='fantastic'
	print(x)
myfunc()

print(x)

def myfunc():
    global q
    q='sirname'
myfunc()

print(q)

r='prince'

def myfunc():
	global r
	r='raj'
myfunc()

print(r)