# testskjal ekki notað í námi

def fun1(self,x):
    """Skrifa fall sem reiknar x^7 - (4 / 3)x^5 + 22x"""
#***
    fx = int(x**7 - (4/3) * x**5-22*x)
    return fx

def fun2(self,ls):
    """Skrifa fall fun2 sem tekur lista ls sem inntak og skilar meðaltali staka
    í ls, med for lykkju"""
#***
    testlist = [ls]
    for medaltal in ls:
        total_sum += medaltal
    return medaltal