def flat_og_um(r):
    pi = 3.14159265
    F = r**2*pi
    U = 2*r*pi
    return F,U

(F,U) = flat_og_um(1)
print(f"Flatarmálið er {F:.3f} og ummálið {U:.3f} og ég heiti Elfar")