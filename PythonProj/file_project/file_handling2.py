"""file = open("readme.txt", "r")

data = file.readlines()

while data != '':
    print(data)
    data = file.readline()
file.close()"""

try:
    with open("readme.txt", "r") as file:
        data = file.read()
        print(data)
except Exception as e:
    print(e)
