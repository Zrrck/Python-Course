fname = input("Enter file name: ")
fh = open(fname)
count = 0
toplam = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
        
    else:
        number =line[19:26]
        toplam = toplam + float(number)
        count = count + 1
        continue
        
result = toplam/count

print("Average spam confidence:",result)
