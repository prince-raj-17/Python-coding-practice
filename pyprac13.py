#python RegEx begin here

import re

txt = "The rain in Spain at 2PM"
x = re.search("^The.*Spain", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

x = re.findall("[a-m]", txt)
print(x)

x = re.findall("\d", txt)
print(x)

txt = "hello world"
x = re.findall("he..o", txt)
print(x)

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#python tyr except

try:
  print(x)
except:
  print("An exception occurred")