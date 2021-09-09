try:
    file = open("readme.txt", "x")
except FileExistsError as file_exist_msg:
    print(file_exist_msg)
except Exception as exception_msg:
    print(exception_msg)
finally:
    file.close()
#file.write("This is a new line 04")

#data = file.read()
#print(data)

