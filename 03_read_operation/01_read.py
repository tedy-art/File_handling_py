fd = open('db.txt', 'r')
data = fd.read()
data = data.split()
# print(data)
for i in data:
    print(i)
fd.close()