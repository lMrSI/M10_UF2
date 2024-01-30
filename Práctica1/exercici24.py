import json

def readJson(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=2))

readJson('exercici23/books.json')
