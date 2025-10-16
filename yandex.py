import datetime
from decimal import Decimal


def add(items, title, amount, expiration_date=None):
    if expiration_date is None:
        if title in items:
            items[title] += [{'amount': amount, 'expiration_date': expiration_date}]
        else:
            items[title] = [{'amount': amount, 'expiration_date': expiration_date}]

    else:
        if title in items:
            dl = [int(elem) for elem in expiration_date.split('-')]
            fuihsfi = datetime.date(dl[0], dl[1], dl[2])
            items[title] += [{'amount': amount, 'expiration_date': fuihsfi}]
        else:
            dl = [int(elem) for elem in expiration_date.split('-')]
            fuihsfi = datetime.date(dl[0], dl[1], dl[2])
            items[title] = [{'amount': amount, 'expiration_date': fuihsfi}]


def add_by_note(items, note):
    if note.count('-') >= 2:
        l = note.split(' ')
        title = ' '.join(l[:-2])
        amount = Decimal(l[-2])
        expiration_date = l[-1]
        add(items, title, amount, expiration_date)
    else:
        l = items.split(' ')
        title = ' '.join(l[:-1])
        amount = l[-1]
        add(items, title, amount)
    


def find(items, needle):
    return [elem for elem in items.keys() if needle.lower() in elem.lower()]


def amount(items, needle):
    s = 0
    for name in items.keys():
        if needle.lower() in name.lower():
            for elem in items[name]:
                s += elem['amount']
                print(elem['amount'])
            break
    return s
        

# Холодильник пуст:
goods = {}


add_by_note(goods, 'Яйца гусиные 4 2023-07-15')

# Словарь goods должен стать таким:

# goods = {
#     'Яйца гусиные': [
#         {'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}
#     ]
# } 
print(goods)