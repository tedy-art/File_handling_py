fd = open('db.txt', 'a+')
data = input("Enter data to write into file: ")
fd.write(data)
fd.close()