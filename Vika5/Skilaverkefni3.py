class Skil(object):
    """Skilaverkefni 3 f. REI"""
    def arr_to_dict(self, arr):
        '''Skrifið fall arr_to_dict(arr) þar sem tekur inn fylki og skilar uppflettitöflu. 
        Lyklarnir í töflunni eru staðsetningar í fylkinu og eru tjáðir með tvenndinni (röð, dálkur). 
        Gildin í töflunni eru gildin í fylkinu með tilsvarandi staðsetningu. Ef d = arr_to_dict(arr) þá gildir að d[(i, j)] == arr[i][j].

        Inntak: arr er ferningsfylki sem tjáð er sem listi af listum (sjá að ofan).
        Skilar: Uppflettitöflu d sem geymir sérhvert stak arr[i][j] með lykli (i, j).
        '''


        return {(i, j): arr[i][j] 
                for i in range(len(arr)) 
                for j in range(len(arr[i]))}
    ...
    
    def dict_to_arr(self, d):
        '''
        Skrifið fallið dict_to_arr(d) sem gerir öfugt við fallið í 1. Fallið tekur inn uppflettitöflu d og skilar fylki sem lista af listum. 
        Ef arr = dict_to_arr(d) þá gildir að d[(i,j)] == arr[i][j].

        Inntak: Uppflettitafla d sem geymir sérhvert stak fylkis arr[i][j] með lykli (i, j).
        Skilar: arr, sem er ferningsfylki sem tjáð er sem listi af listum (sjá að ofan). Þannig er arr[i][j] == d[(i, j)].
        '''
        n = max(i for i, j in d.keys()) + 1  #Reiknar með fernings
    
        # Tómt fylki
        arr = [[None for _ in range(n)] for _ in range(n)]
        
        # Fyllir fylkið
        for (i, j), value in d.items():
            arr[i][j] = value
        
        return arr



        ...
    def snuavid(self, d1):
        '''Fall sem snýr við uppflettitöflu d1 og skilar d2 þar sem lyklarnir eru gildin úr d1 
        og gildin eru lyklarnir úr d1. Ef fleiri en einn lykill vísar á sama gildi, þá geymir 
        d2 lista af þeim lyklum í vaxandi röð.'''

        # Starta tómt d2
        d2 = {}

        # Tjékka öll lykil/gildi pör í d1
        for key, value in d1.items():
            # Ef gildi er þegar til í d2, bæta við lykli
            if value in d2:
                # Ef ekki listi, breyti í lista
                if isinstance(d2[value], list):
                    d2[value].append(key)
                else:
                    d2[value] = [d2[value], key]
            else:
                # Gildi í d2 með lykli
                d2[value] = key

        # Sortum lista ef það er til fleiri en einn lykill með sama gildi
        for key, value in d2.items():
            if isinstance(value, list):
                value.sort()  # Raða lyklum í vaxandi röð

        return d2



        ...

if __name__ == '__main__':
    skil = Skil()

    a, b, c, d = 1, 2, 3, 4
    arr = [[a, b], [c, d]]
    D = {(0,0):a,(0,1):b,(1,0):c,(1,1):d}
    
    assert D == skil.arr_to_dict(arr), "`arr_to_dict` er ekki rétt"
    assert arr == skil.dict_to_arr(D), "`dict_to_arr` er ekki rétt"

    d1 = {0: 1, 1: 2, 2: 1}
    assert {1: [0, 2], 2: 1} == skil.snuavid(d1), "`snuavid` er ekki rétt"