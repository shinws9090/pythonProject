import turtle as t

t.shape('turtle')
t.speed('fastest')
a = 1

while True:
    a += 1
    if a<200:
        t.forward(a)
        t.right(91)
    if a > 200:
        t.circle(a)
