import math

class Skil(object):
    """Skilaverkefni 2 f. REI
    """
def simpson(self,f,a,b,n):
    f = lambda x: x**2

    a = float(input("Sláðu inn gildi fyrir a: "))
    b = float(input("Sláðu inn gildi fyrir b: "))
    n = int(input("Sláðu inn gildi fyrir n: "))

    if n % 2 == 1:
        raise ValueError("n verður að vera slétt tala")

    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x_i)
        else: 
            sum += 4 * f(x_i)

    return sum * (h / 2)

print(simpson(a,b,n))

def vextir(self,u,p,k,m):
    u = int(input("Sláðu inn gildi fyrir u: "))
    p = int(input("Sláðu inn gildi fyrir p: "))
    k = int(input("Sláðu inn gildi fyrir k: "))
    m = int(input("Sláðu inn gildi fyrir m: "))
    a = p/100
    v = u((1+a)**2) * ((1 + (a*m/12))-u)

    lokasvar = int(v)

    return lokasvar

print(vextir())
def vextir2(self,u,p,k,m):
# her er haegt ad kalla self.vextir(u,p,k,m) til ad nota fyrri fallid
    u = int(input("Sláðu inn gildi fyrir u: "))
    p = int(input("Sláðu inn gildi fyrir p: "))
    #k = int(input("Sláðu inn gildi fyrir k: "))
    #m = int(input("Sláðu inn gildi fyrir m: "))
    a = p/100
    v = u((1+a)**2) * ((1 + (a*m/12))-u)
    lokaupphaed = u * 2

    '''
    #upphaed = int(input("Sláðu inn gildi fyrir upphæð: "))
    upphaed = v
    while upphaed < upphaed * 2:
        upphaed *= p
    '''
    
    while u < lokaupphaed:
        u *= (1 + a / 12)
        man += 1
        if man == 12:
            man = 0
            ar += 1

    return ar, man


def dict_creator(self,ls1,ls2,null_val):



    
    ls1 = [23,2,1,6,7,3,4,6,7]
    ls2 = ["kale","enia","hewg","roderika","marika","thops","rogier","iji","millicent"]

    print(dict_creator(ls1,ls2,2) )
    #skilar
    {1: 'enia', 3: 'iji', 4: 'kale', 6: 'millicent', 7: 'rogier', 23: 'thops'}
    if __name__ == '__main__':
        
#her er haegt ad profa klassann
# getid keyrt tetta allt i kodacellu i vscode(i einu)
#eda keyrt skil_s2.py i command line.
#daemi ad nedan
        skil = Skil()
        val = skil.vextir(300000,20,10,1)
#print(val)
