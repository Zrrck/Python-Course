name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

bigcount =  None
bigword = None

counts = dict()

for line in handle:
    if line.startswith('From:'):
        
       ayrik = line.split()
        
       mails = ayrik[1]
       
       counts[mails] = counts.get(mails,0) +1
        
for word,count in counts.items():
    
    if bigcount is None or count > bigcount:
    
       bigword = word
       bigcount = count
    

print(bigword , bigcount)

