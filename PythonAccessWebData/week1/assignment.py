import re
count = 0
sum = 0
al = open('regex_sum_208500.txt')
oku = al.read()


numbers = re.findall('[0-9]+',oku)
print(numbers)
for number in numbers:

    count = count + 1
    sum   = sum + int(number)
    
print(count)
    
print(sum)
