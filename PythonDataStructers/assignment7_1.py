
fname = input("Enter file name: ")
fh = open(fname)

text = fh.read()
for line in text:
 	line = line.rstrip()
print(text.upper())

