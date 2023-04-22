# 2차원 리스트
d1 = [10, 20]
# print(d1[0])
d1.append(30)

for i in d1:
    print(i, end=' ')

d2 = [
    [10, 20],
    [30, 40],
    [50, 60]
]
print()
print(d2[0][0])  #10
print(d2[0][1])  #20
print(d2[1][0])  #30

d2.append([70, 80])
for x, y in d2:
    print(x, y)



