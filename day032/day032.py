# Day 32

a = [3,5,7,9,11,13,15,17]
b = [2,4,6,8,10,12,14,16]


for x in range(len(a)):
    for y in range(len(b)):
        print(f'{a[x]} <---> {b[y]}')
    print('--------------------')