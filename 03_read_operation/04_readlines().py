fd = open('db.txt', 'r')
data = fd.readlines()
print(data)
fd.close()