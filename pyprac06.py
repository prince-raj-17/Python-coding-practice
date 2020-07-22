thislist = ["apple","banana","cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])

l=["A","B","C","D","E","F"]
print(l[2:5])
print(l[:4])
print(l[2:])
print(l[-4:-1])

thislist[1] = "blackcurrent"
print(thislist)

for x in thislist:
	print(x)

for a in l:
	print(a)

if "apple" in thislist:
	print("yes,'apple' is in thislist. ")

print(len(l))
l.append("G")
print(l)

thislist.insert(1,"orange")
print(thislist)

thislist.remove("blackcurrent")
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

#del thislist , will delet the whole list.

l.clear()
print(l)

tl = ["apple","banana","cherry"]
mylist= tl.copy()
print(mylist)

shylist = list(mylist)
print(shylist)

list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
for x in list2:
	list1.append(x)
print(list1)

list1.extend(list2)
print(list1)

x= ("apple","banana","cherry")
y= list(x)
y[1]= "kiwi"
print(y)

x= tuple(y)
print(x)

thistuple = ("apple",)
print(type(thistuple))

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisdict = {"brand": "ford", "model":"mustang", "year":"1964"}
print(thisdict)
x= thisdict["model"]
print(x)
thisdict["year"]= 2018
print(thisdict)
for x in thisdict:
	print(thisdict[x])

for x,y in thisdict.items():
	print(x,y)

mydict= dict(thisdict)
print(mydict)

myfam = {
	  "child1" : {
	     "name" : "emil",
	     "year":2014
	     },
	"child2" : {
	    "name" : "raw", 
	    "year":2004
	    }
}
print(myfam)