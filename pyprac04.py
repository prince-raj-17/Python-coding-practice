x=5
x=float(x)
print(x)

x=float(1)
y=float(2.8)
z=float("3")
w=str("s1")
p=str(2)
m=int(2.6)

print(x)
print(y)
print(z)
print(w)
print(p)
print(m)

a="hello"
print(a)

b="""we can do whatever we want,
all we need to focus and
to choose right path."""
print(b)
print(b[3])
print(b[2:6])
print(b[-8:-1])

x="prince raj"
print(len(x))

x=" prince raj"
print(x)
print(x.strip())

a="PRINCE"
print(a)
print(a.lower())

print(x.upper())

print(a.replace("P","t"))

x="prince,raj"
print(x.split(","))

txt="elephants walk slow"
x="alk"in txt
y="alk" not in txt
print(x)
print(y)

a="hello"
b="world"
c=a+" "+b
print(c)

age=31
txt="my name is flana, and i am {} year old."
print(txt.format(age))

myorder="i want {} pieces of item no. {} for {} dollar."
quantity=4
itemno=345
price=19
order="I want {0} apple in {2} dollar"
print(myorder.format(quantity,itemno,price))
print(order.format(quantity,itemno,price))

a="we are so called \"VIKINGS\" from the north."
print(a)

b="it\'s allright"
print(b)

c="i have done\\ go now."
print(c)

d="hi \nhow are you?"
print(d)

e="hi\ttry"
print(e)

f="heyy\b you"
print(f)

#A backslash followed by an 'x' 
#and a hex number represents a hex value.

#A backslash followed by three integers 
#will result in a octal value.
