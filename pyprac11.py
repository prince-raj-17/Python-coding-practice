# python scope begin here

def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 325
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

x = 240

def myfunc():
  print(x)

myfunc()

print(x)

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

def myfunc():
  global x
  x = 3

myfunc()

print(x)

a = 30

def myfunc():
  global a
  a = 20

myfunc()

print(a)

#python modules begin here

import mymodule

mymodule.greeting("Samiksha")

import mymodule

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)
