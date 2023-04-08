# 중첩 for문
"""
for i in range(0, 5): #0,1,2,3,4
    for j in range(0, 5):
        print('*', end='')
    print()  # 줄바꿈
    
*
**
***
****
*****
for i in range(0, 5): #0,1,2,3,4
    for j in range(0, i+1):
        print('*', end='')
    print()  # 줄바꿈

*****
****
***
**
*
for i in range(0, 5): #0,1,2,3,4
    for j in range(0, 5-i):
        print('*', end='')
    print()  # 줄바꿈


1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20

i=0 j=1, 2, 3, 4, 5      -> 5 * 0 + 1
i=1 j=6, 7, 8, 9, 10     -> 5 * 1 + 1
i=2 j=11, 12, 13, 14, 15 -> 5 * 2 + 1
"""
for i in range(0, 4):
    for j in range(1, 5):
        num = (4*i)+j
        print(num, end=' ')
    print()












    
