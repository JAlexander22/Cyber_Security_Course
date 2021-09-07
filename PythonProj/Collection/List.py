colors = ['black', 'green', 'red', 'blue']

print(colors)
print(colors[0])
colors.append('Orange')
colors.remove('black')

for i in colors:
    print(i)

print('colors index = ', colors.index('green'))
colors.sort()
print(colors)


print("red in colors? ", "black" in colors)
print("red in colors? ", "grey" in colors)



print("-----------------------------")


items = ['black', 1.5 , 'red', True]
for item in items:
    print (item)

print(len(items))
