trainee = {'fname' : 'Jordan', 'lname' : 'Alexander', 'group' : {'G1': 'Eng-94', 'G2':'Eng-92'}, 'year' : 2021}

trainee = dict(fname = 'Jordan', lname=  'Alexander', group= {'G1': 'Eng-94', 'G2':'Eng-92'}, year= 2021)


print('fname: ', trainee['fname'])
print('lname: ', trainee['lname'])
print('group: ', trainee['group'])
print('year:  ', trainee['year'])

trainee['fname'] = 'Shariah'
print('fname: ', trainee['fname'])

print("printering using a loop")
for i in trainee:
    print(i)

print('Print keys')
for i in trainee.keys():
    print(i)

print('Print values')
for i in trainee.values():
    print(i)

print('Printing keys and values')
for key, value in trainee.items():
    print(key, ':', value)

print('Print keys and values loop method 2')
for key in trainee:
    print(key, ':',trainee[key])
