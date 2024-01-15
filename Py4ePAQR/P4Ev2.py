'''
fname = 'texto-prueba.txt'
new_lst = []

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        #line = line.replace("(","")
        #line = line.replace(")","")
        line = line.split(",")
        line[5] = line[5].replace("'","")
        line[0] = line[0].replace("'","")
        line[4] = line[4].replace("'","")
        line[6] = line[6].replace("'","")
        new_line = ",".join(line)
        print(new_line)
        new_lst.append(new_line)
print(new_list)
'''
fname = 'test2.txt'
new_lst = []

with open(fname) as fh:
    for line in fh:
        line = line.rstrip()
        #line = line.replace("(","")
        #line = line.replace(")","")
        line = line.split(",")
        line[1] = line[1].replace("'","")
        line[2] = line[2].replace("'","")
        line[4] = line[4].replace("'","")
        new_line = ",".join(line)
        print(new_line)
        new_lst.append(new_line)
print(new_list)