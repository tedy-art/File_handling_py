fd = open('db.txt','a+')
data = input("Enter data to write into file: ")
data = data.split()
print('\n')
fd.writelines(data)
fd.close()