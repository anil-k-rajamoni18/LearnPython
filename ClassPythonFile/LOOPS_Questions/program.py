import json

fileObj = open('nobel.json',mode='r') #opening files 

data = json.loads(fileObj.read()) # converting str - json 


# print(len(data['prizes'])) 

chemistryCount = 0

for entry in data['prizes']:
    for k , v in entry.items():
        if k == 'category' and v == 'chemistry':
            print(entry)
            chemistryCount+=1
            break

print(f'nobel prize count for chemistry {chemistryCount}' )