#  Write a program in python that reads a file and prints all its content

file_name = str(input("Enter the name of the file as a .txt extension: "))

# We open the file using the open() method
file = open(file_name)

#  We read the file using the method call readline()
read_content = file.readline()

# using the wile loop to read the content of the file
while(read_content != ""):
    print(read_content)
    read_content = file.readline()
file.close()    
    