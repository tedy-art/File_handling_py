fd = open('db.txt', 'r')
data = fd.readline()
print(data)
fd.close()