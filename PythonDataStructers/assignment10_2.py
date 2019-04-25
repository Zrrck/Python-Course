name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith("From "):
        
       ayrik = line.split()
       
       
       times = ayrik[5]
       
       time  = times.split(':')
       hours = time[0]
       
       counts[hours] = counts.get(hours,0) +1
        
abc = counts

abc = sorted([(k,v)for k,v in abc.items()])

for k,v in abc:
    
	print(k,v)for line in handle:
    if line.startswith('From:'):
        
       ayrik = line.split()
