import json
trainee = {'fname' : 'adam', 'lname' : 'smith', 'group' :'eng-94', 'year':'2021'}

print(trainee)

with open('trainee.json', 'w') as file:
    json.dump(trainee, file)
