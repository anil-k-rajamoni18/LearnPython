import json

fileObj = open('nobel.json',mode='r') #opening files 

data = json.loads(fileObj.read()) # converting str - json 


# print(len(data['prizes'])) 

chemistryCount = 0
physicsCount = 0

listOfCategory = {'economics', 'medicine', 'literature', 'chemistry', 'physics', 'peace'}



totalNobelChemistryPrizes = 0
for entry in data['prizes']:
    for k , v in entry.items():

        if k == "year" and (v >="1901"  and v<="2022"):
                if(entry['category'] == 'chemistry'):
                     #print(f'no of peoples got noble prizes in {entry["year"]}:  {len(entry["laureates"])}')
                    if entry.get('laureates') != None:
                         totalNobelChemistryPrizes += len(entry["laureates"])



print(f'total chemistry nobel prizes {totalNobelChemistryPrizes}')
# print(f'total number of categories.. {listOfCategory} and length is {len(listOfCategory)}')

# print(f'nobel prize count for chemistry {chemistryCount}' )

# print(f'nobel prize count for physics {physicsCount}' )