file = open("readme.txt", "r")

data = file.read(10)
print(data)

data2 = file.read(10)
print(data2)

file.close()

