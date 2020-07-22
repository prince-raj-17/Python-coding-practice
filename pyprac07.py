a=3
b=33

if a > b :
	print("a is greater than b")
elif a == b:
	print("a is equal to b")
else:
	print("a is smaller than b")

x = 5
y = 6
print ("X") if x>y else print("Y")

i = 1
while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")

i= 1
while i < 7:
	print(i)
	if i == 4:
		break
	i += 1

	#python for loop :

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	
	if x == "banana":
		break
	print(x)

fruit = ["apple", "banana", "cherry"]
for x in fruit:
	if x == "banana":
		continue
	print(x)
