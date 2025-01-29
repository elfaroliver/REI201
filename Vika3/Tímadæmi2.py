#class Tímadæmi2:
def annadStig ():
    import math

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