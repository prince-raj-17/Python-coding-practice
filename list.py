
x = [1,2,3,4,5,6,7,8,9,10]
print(len(x))

print("getting even numbers" )
count = 0

for i in x:
	if i % 2 == 0:
		count = count+1
		print(i)

print(count)
