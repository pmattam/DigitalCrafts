filename = raw_input("Enter file name: ")
openfile = open(filename, 'r')

print openfile.read()

openfile.seek(0)
print "\n"

print openfile.readline() 
openfile.close()


