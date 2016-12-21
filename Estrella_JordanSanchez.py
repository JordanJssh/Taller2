import turtle

t=turtle.Pen()

x=int(input("Ingrese el valor de lados: "))
t.reset()
for i in range(x):
    t.right(((x-2)*180)/x)
    t.forward(100)
    t.right(((x-2)*180)/x)
