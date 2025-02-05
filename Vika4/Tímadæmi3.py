import math

def tolfraedi(d):

    lyklar = list(d.keys())
    gildi = list(d.values())
    
    # Meðaltöl beggja gilda
    mean_k = sum(lyklar) / len(lyklar)
    mean_v = sum(gildi) / len(gildi)

    print(f"Meðaltal lykla: {mean_k}")
    print(f"Meðaltal gilda: {mean_v}")
    
    # Staðalfrávik lykla
    s_k = math.sqrt(sum((k - mean_k) ** 2 for k in lyklar) / (len(lyklar) - 1))
    # Staðalfrávik gilda
    s_v = math.sqrt(sum((v - mean_v) ** 2 for v in gildi) / (len(gildi) - 1))

    '''sum_k = 0
    for x in lyklar:
        sum_k += (x - mean_k) ** 2
    s_k = math.sqrt(sum_k / len(lyklar))

    sum_v = 0
    for x in gildi:
        sum_v += (x - mean_v) ** 2
    s_v = math.sqrt(sum_v / len(gildi))'''

    print(f"Staðalfrávik lykla: {s_k}")
    print(f"Staðalfrávik gilda: {s_v}")
    
    return s_k, s_v

#print(s_k, s_v)

# Dæmitest kennara
d = {1:3, 2:3, 3:1}
print(tolfraedi(d))