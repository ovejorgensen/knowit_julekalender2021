import requests
from copy import copy

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBNdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--0af4f790dec929a13e3615fdac11667323ea1597/tall.txt?disposition=inline')
data.encoding = 'utf-8'
data = data.text

numbers = {
    'en' : 1,
    'to' : 2,
    'tre' : 3,
    'fire' : 4,
    'fem' : 5,
    'seks' : 6,
    'sju' : 7,
    'åtte' : 8,
    'ni' : 9,
    'ti' : 10,
    'elleve' : 11,
    'tolv' : 12,
    'tretten' : 13,
    'fjorten' : 14,
    'femten' : 15,
    'seksten' : 16,
    'sytten' : 17,
    'atten' : 18,
    'nitten' : 19,
    'tjue' : 20,
    'tretti' : 30,
    'førti' : 40,
    'femti' : 50,
}

keys = list(numbers.keys())[::-1]

result = []
while len(data) > 1:
    for key in keys:
        if data.startswith(key):
            result.append(numbers[key])
            data = data[len(key):]
            break

print(sum(result))