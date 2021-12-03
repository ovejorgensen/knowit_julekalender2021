import requests
from nltk import ngrams

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--31fa0c541c69eeb9063ccfc56e686f4768662004/input.txt?disposition=inline').text

for i in range(10, 100):
    grams = ngrams(data, i+1)
    for gram in grams:
        if gram.count('J') == len(gram)/2:
            print(f'{i+1}-gram, {data.index("".join(gram))}')
            break
