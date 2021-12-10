import requests

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBallDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--20b29549a475416a15aa81ff11b00da4c4103e67/pakker.txt?disposition=inline').text

data = data.split('\n')
data.pop()

row = [1] * 20
rows = [row]
falls = 0

for package in data:
    x0, x1 = package.split(',')
    x0 = int(x0)
    x1 = int(x1)

    row = [0] * 20
    row[x0:x0+x1] = [1] * x1

    placed = False
    fall = False

    current_row = 0
    while (not placed) or current_row == len(rows)-1:
        if x1 == 1 and rows[current_row][x0] == 1:
            if current_row > 0:
                rows[current_row-1][x0] = 1
            else:
                rows.insert(0, [0] * 20)
                rows[0][x0] = 1
            placed = True
        elif x1 % 2 == 1 and rows[current_row][x0+int(x1/2)] == 1 and (any(rows[current_row][x0:x0+int(x1/2)]) or any(rows[current_row][x0+int(x1/2):x0+x1])):
            if current_row > 0:
                rows[current_row-1][x0:x0+x1] = [1] * x1
            else:
                rows.insert(0, row)
            placed = True
        elif any(rows[current_row][x0:x0+int(x1/2)]) and any(rows[current_row][x0+int(x1/2):x0+x1]):
            if current_row > 0:
                rows[current_row-1][x0:x0+x1] = [1] * x1
            else:
                rows.insert(0, row)
            placed = True
        elif any(rows[current_row][x0:x0+int(x1/2)]) and not any(rows[current_row][x0+int(x1/2):x0+x1]):
            falls += 1
            fall = True
            placed = True
        elif not any(rows[current_row][x0:x0+int(x1/2)]) and any(rows[current_row][x0+int(x1/2):x0+x1]):
            falls += 1
            placed = True
            fall = True
        current_row += 1

    if not placed:
        rows[current_row-1][x0:x0+x1] = [1] * x1

print("\nFallen packages:", falls)
