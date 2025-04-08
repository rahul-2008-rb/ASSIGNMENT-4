file1=open("Sample.txt",'r+')
writing=file1.write("Line 1: This is a sample text file")
file1.close()

file1=open("Sample.txt",'r+')
reading=file1.read()
print(reading)
file1.close()

file1=open("Sample.txt",'r+')
writing=file1.write("Line 2: It contains multiple lines")
file1.close()

file1=open("Sample.txt",'r+')
reading=file1.read()
print(reading)
file1.close()
