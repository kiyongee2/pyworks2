import turtle as t # 별칭

t.shape('turtle')
# 사각형
t.forward(100)  #직진 - 100px 이동
t.left(90)  # 각도를 90도 설정
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

for i in range(4): #0, 1, 2, 3
    t.forward(100)
    t.right(90)

# 삼각형
t.color('blue')
t.shapesize(2)
t.left(120)
t.forward(80)
t.left(120)
t.forward(80)
t.left(120)
t.forward(80)

for i in range(3):
    t.right(120)
    t.forward(80)

t.mainloop()