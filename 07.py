ant = 1
santa = 20

while ant < santa:
    santa += 20
    ant *= santa/(santa-20)
    ant += 1

print(f'Length: {santa/100}m')