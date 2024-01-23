import json
import random

def generateBook():
    titles = ['Noches Blancas', 'Harry Potter', 'Delirium', 'Crimen y Castigo']
    covers = ['Rústica.jpg', 'Bloomsbury.jpg', 'Portlan.jpg', 'Rústica.jpg']
    years = [1848, 1991, 2011, 1866]
    pages = [84, 309, 445, 948]

    random_index = random.choice(range(4))
    return {
        'book': {
            'title': titles[random_index],
            'cover': covers[random_index],
            'year': years[random_index],
            'pages': pages[random_index],
        }
    }

def generateSave(num_books):
    list = []

    for _ in range(num_books):
        list.append(generateBook()['book'])

    data = {'books': list}

    print(json.dumps(data, indent=2))

    with open('books.json', 'w') as file:
        json.dump(data, file, indent=2)

generateSave(4)
