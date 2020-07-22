# python Date Tine begis here

import datetime

x = datetime.datetime.now()

print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#Python Math begins here

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

import math

x = math.sqrt(4)
print(x)

x = math.ceil(1.1)
y = math.floor(1.9)

print(x)
print(y)

x = math.pi
print(x)

#JSON begin here

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["age"])

y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(json.dumps(x, indent=4, sort_keys=True))
