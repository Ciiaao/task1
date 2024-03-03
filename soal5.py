import turtle

CIAO = turtle.Turtle()
print('enter the size and color of square')
a=input()
b=input()
try:
    a=int(a)
except ValueError:
    a=float(a)
CIAO.shape('turtle')
CIAO.color('black',b)

CIAO.begin_fill()
for i in range (4):
    CIAO.forward(a)
    CIAO.right(90)
CIAO.end_fill()
turtle.done()