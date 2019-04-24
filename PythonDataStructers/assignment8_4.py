fname = input("Enter file name: ")
fh = open(fname)
fh = fh.read()
lst = list()
fh = fh.split()
fh.sort()
for line in fh:
    
    if line in lst: continue

    lst.append(line)
    

print(lst)
