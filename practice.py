# Python has several functions for creating , reading , updating and deleting files.
# here i am opening a demofile using python commands.
"""
Here is the text of demofile:

"Hello!
I am Prince Raj.
I am practicing Python file handling."


Now,
To open the file, we use the built-in open() function.

The open() function returns a file object,
 which has a read() method for reading the content of the file:
 """

f = open("demofile.txt", "r")
print(f.read())

# By default the read() method returns the whole text.
# but we can also specify how many characters we want to return:
f = open("demofile.txt", "r")
print(f.read(2))

# read one line of the file by using readline() method:
f = open("demofile.txt", "r")
print(f.readline())

# read multiple line of the file
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# read all line one by one:
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close the file when we are finish with it:
f = open("demofile.txt", "r")
print(f.read())
f.close()

# write to an existing file

"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

# Open the file and append content to the file:
r = open("demofile2.txt", "a")
r.write("Now the file has more content!")
r.close()

# open and read the file after the appending:
r = open("demofile.txt", "r")
print(r.read())

# Open the file and overwrite the content:
s = open("demofile3.txt", "w")
s.write("Woops! I have deleted the content!")
s.close()

# open and read the file after the appending:
s = open("demofile3.txt", "r")
print(s.read())

# Create a new file
"""
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
"""

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile.txt", "w")

# Delete a file

"""
To delete a file, 
we must import the OS module,
and run its os.remove() function:
"""
# Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

# Check if File exist:
"""
To avoid getting an error, 
we might want to check if the file exists before you try to delete it:
"""

# Check if file exists, then delete it:
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete Folder
"""
To delete an entire folder,
use the os.rmdir() method:
"""
# Remove the folder "myfolder":
import os

os.rmdir("myfolder")

# Note: You can only remove empty folders.
