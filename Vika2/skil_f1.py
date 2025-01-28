class Skil():
    """Fyrirlestraaefing 1 f. REI

    """

    #Daemi 1
    def fun1(self,ls):
        # Skrifa fall sem tekur inn lista ls af heiltolum,
        # og ber saman fyrsta og seinasta staki i lista ls
        # og skilar staerra gildinu, ef tau eru jafnstor ta skilid tid gildinu(i odru hvoru saeti).
        # fun1([5,2,3,4]) skilar 5
        # fun1([4,2,3,4]) skilar 4

        # testlist = [ls]

        '''if ls[0] > ls[-1]:
            listi = ls[0]
        elif ls[-1] > ls[0]:       
            listi = ls[-1]
        else: 
            listi = ls[0]'''

        fyrsta = ls[0]
        seinasta = ls[-1]
        
        if fyrsta >= seinasta:
            svar = fyrsta
        else: 
            svar = seinasta


        return svar