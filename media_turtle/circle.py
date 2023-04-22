# 원 그리기
import turtle as t

#t.circle(100) # 반지름이 100px
#t.circle(80)
t.bgcolor('black')
t.color('yellow')
t.speed(0) # 1~10 10이 가장 빠름, 0-더 빠름
n = 80
for x in range(n):
    t.circle(80)
    t.left(10)

t.mainloop()