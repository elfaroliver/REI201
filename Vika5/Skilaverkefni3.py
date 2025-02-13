class Skil(object):
    """Skilaverkefni 3 f. REI"""
    def arr_to_dict(self, arr):
        '''Skrifið fall arr_to_dict(arr) þar sem tekur inn fylki og skilar uppflettitöflu. 
        Lyklarnir í töflunni eru staðsetningar í fylkinu og eru tjáðir með tvenndinni (röð, dálkur). 
        Gildin í töflunni eru gildin í fylkinu með tilsvarandi staðsetningu. Ef d = arr_to_dict(arr) þá gildir að d[(i, j)] == arr[i][j].

        Inntak: arr er ferningsfylki sem tjáð er sem listi af listum (sjá að ofan).
        Skilar: Uppflettitöflu d sem geymir sérhvert stak arr[i][j] með lykli (i, j).
        '''


        return {(i, j): arr[i][j] for i in range(len(arr)) for j in range(len(arr[i]))}
        ...
    def dict_to_arr(self, d):


        ...
    def snuavid(self, d1):


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