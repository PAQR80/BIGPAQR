"""
largest = None
smallest = None
while True :
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        num = int(num)
        if largest is None:
            largest = num
        elif num > largest :
            largest = num
        if smallest is None:
            smallest = num
        elif num < smallest :
            smallest=num
    except :
        print('Invalid input')
        continue
    
print('Maximum is', largest)
print('Smallest is', smallest)
"""
'''
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0.')
print(pos)
num=float(text[pos:])
print(num)
'''

""" 
fname = input("Enter file name: ")
count = 0
lst = list()
fh = open(fname)

for line in fh: 
    line = line.rstrip()
    if line.startswith('From '):
        words=line.split()
        if len(words)>1:
            email=words[1]
            print(email)
            count = count + 1
#for email in lst:
#    if email not in lst:
#        lst.append(email)
#        count = count + 1 
print("There were", count, "lines in the file with From as the first word")
""" 
"""

#Creates a histogram for a specofoc hour in the text file.

fname = input("Enter file name: ")
count = dict()
fh = open(fname)
bigcount = None 
bigword = None 
if len(fname) < 1:
    fname = "text.txt"
for line in fh: 
    line = line.rstrip()
    if line.startswith('From '):
        words=line.split()
        if len(words)>1:
            email=words[5] 
            email = email.split(":")
            email = email[0]
            count[email]= count.get(email,0)+1
"""

#Print out the sorted by hour and the value in the histogram. 
"""
sorted_hour = sorted(count.items()) 

for k,v in sorted_hour:
    print(k,v)
"""
    
#Prints out the most common word and the value in the histogram
"""
for email,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
print (bigword,bigcount)
"""


