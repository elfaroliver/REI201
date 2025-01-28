import math

class Skil(object):
    """Skiladaemi 1 f. REI
"""
    #Daemi 1
    def fun1(self,x):
        """Skrifa fall sem reiknar x^7 - (4 / 3)x^5 + 22x"""
    #***
        fx = int(x**7 - (4/3) * x**5-22*x)
        return fx


    #Daemi 2
    def fun2(self,ls):
        """Skrifa fall fun2 sem tekur lista ls sem inntak og skilar meðaltali staka
        í ls, med for lykkju"""
    #***
        
        total_sum = 0

        for num in ls:
            total_sum += num
        return total_sum / len(ls) if len(ls) > 0 else 0


    #Daemi 3
    def fun3(self,S):
        """Skrifa fall fun3 sem skilar lista af tekur in streng S og skilar fjölda
        sérhljóða í strengnum"""
    #***
        vowels = "aeiouAEIOU"

        #S = (input("Strenginn hingað inn, por favor"))

        fjoldi = sum(S.count(vowel) for vowel in vowels)
        return fjoldi


    #Daemi 4
    def fun4(self,S):
        """tekur sem tekur in streng S og skilar True ef S er eins afturábak og
        áfram, false annars."""
        if (S == S[::-1]):
            print("Palindrome")
        else:
            print("Ekki palindrome")


    #Daemi 5
    def fun5(self,u):
    #Skila radius hrings med ummal u
        u = float(input("Gemmér ummál"))
        radius = (u/(2*math.pi))
        return radius
