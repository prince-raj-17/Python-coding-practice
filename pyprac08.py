print("Python Functions")
#runs when it is called.
#a function can result data as a result.

def my_function():
	print("hello from a function")

my_function()
my_function()

def my_function(fname):
	print(fname + " Raj")

my_function("Prince")
my_function("Himanshu")
my_function("dh")

def my_function(fnam , lnam):
	print(fnam + " " + lnam)

my_function("Prince" , "Raj")

def my_function(*child):
	print("The youngest child is " + child[1])

my_function("Bikash","Lucy","Dan")

def my_function(child1,child2,child3):
	print('The youngest child is ' + child3)

my_function(child1="Emil",child2="Tobis",child3="Nina")

def my_function(**kid):
	print("his last name is " + kid["lname"])

my_function(fname = "Tobis", lname = "Joseph")

def my_function(country = "Norway"):
	print("I am from " + country )

my_function("Sweden")
my_function("India")
my_function("Russia")
my_function()

def my_function(food):
	for x in food:
		print(x)

fruits = ["Apple", "Cherry","Banana"]
veg = ["Tomato","Chilli"]
my_function(fruits)
my_function(veg)

def my_function(x):
	return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function():
	pass

def tri_recursion(k):
	if(k>0):
		result=k + tri_recursion(k-1)
		print(result)
	else:
		result=0
	return result

print("\n\nRecursion Example Results")
tri_recursion(5)

