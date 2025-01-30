#class Tímadæmi2:
import math

def annadStig ():
    #import math

    #a,b,c = float(input("Sláðu inn a, b, og c fyrir annars stigs jöfnu: "))
    a = float(input("Sláðu inn gildi fyrir a: "))
    b = float(input("Sláðu inn gildi fyrir b: "))
    c = float(input("Sláðu inn gildi fyrir c: "))

    d = b**2-4*a*c

    if d < 0:
        print("Engin lausn")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        print("Ein lausn"), x
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
        print("Tvær lausnir"), x1, " og", x2

def Trapisa ():
    
    import math

    #global f_global
    #f_global = f

    f = lambda x: x**2

    a = float(input("Sláðu inn gildi fyrir a: "))
    b = float(input("Sláðu inn gildi fyrir b: "))
    n = int(input("Sláðu inn gildi fyrir n: "))

    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        sum += 2 * f(x_i)

    return sum * (h / 2)