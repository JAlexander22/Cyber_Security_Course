import json
trainee = {'fname' : 'adam', 'lname' : 'smith', 'group' :'eng-94', 'year':'2021', 'subscription':'null', 'Something': False}

print("this is a dict format")
print(trainee)

print("This is a json object")
trainee_json_object = json.dumps(trainee)
print(trainee_json_object)

