import requests

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBak1DIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d6d3984e0f603df1771ef6b699e6e86d6ee577a7/tree.txt?disposition=inline').text

# Find the index of the closing paranteces while skipping middle parenteces
def stop_index(tree, start):
    skip = 0
    first = False
    for i, el in enumerate(tree[start:]):
        if el == '(':
            first  = True
            skip += 1
        elif el == ')':
            skip -= 1
        elif skip == 0 and first:
            return i 
    return len(tree)-1

# Recusively check the depth of the tree
def depth(tree):
    if tree.count('(') == 1 and tree.count(')') == 1:
        return 0
    if tree.count('(') == 0:
        return 0
    else:
        start = tree.index('(') + 1
        stop = stop_index(tree, start) + start
        left, right = 0, 0

        add = 0 if tree.startswith('Grinch') else 1
        left = add + depth(tree[start:stop])

        add = 0 if tree[stop:-1].startswith('Grinch') else 1
        right = add + depth(tree[stop:-1])

        if left > right:
            return left
        else:
            return right

print(depth(data))