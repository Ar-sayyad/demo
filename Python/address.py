book = {}
book['tom'] = {
    'name':'tom',
    'address': '1 red street, NY',
    'phone': 9856263256
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 8855220124
}

import json
s = json.dumps(book)
print(s)
with open("d://Python//data//book.txt","w") as f:
    f.write(s)