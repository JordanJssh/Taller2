import turtle
import math

t=turtle.Pen()

angulo=0
x=int(input("Ingrese el valor de lados: "))
t.reset()
angulo=360//x
if x%2!=0:
    print("Impar")
    for i in range(x):
        t.right(((x-2)*180)/x)
        t.forward(100)
        t.right(((x-2)*180)/x)
else:
    print("Par")
    for i in range(x):
        t.forward(100)
        t.right(((x-2)*180)/x)
    

