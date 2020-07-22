print("Hello , World!")

x = "john"
print(x)

x = lambda a : a + 10
print(x(3))

x= lambda a, b : a*b
print(x(4,3))

x= lambda a, b,c : a+b+c
print(x(4,3,1))

def myfunc(n):
	return lambda a : a*n

q = myfunc(3)
print(q(6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#arrays begin here
cars = ["Ford","Volvo","BMW"]
print(cars)

a = cars[0]
print(a)

cars[0] = "Toyota"
print(cars)

print(len(cars))

for x in cars:
	print (x)

cars.append("honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("honda")
print(cars)

#class begin here

class Myclass:
	x=5

print(Myclass)

p1 = Myclass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)




