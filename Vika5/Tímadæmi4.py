#https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

import matplotlib.pyplot as plt

ar = []
hiti = []
urkoma = []


lines = f.readlines()

with open("hiti-urkoma.txt") as f:
    for line in lines: 
        values = line.strip().split()
        ar.append(int(values[0]))
        hiti.append(float(values[1]))
        urkoma.append(float(values[2]))

plt.figure(figsize=(10, 10))
plt.scatter(ar, hiti, color="green", marker="o")
plt.xlabel("Ár")
plt.ylabel("Hitastig (°C)")
plt.title("Tenging árs og hitastigs")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 10))
plt.hist(urkoma, bins=10, color="red", edgecolor="black")  # Adjust bins as needed
plt.xlabel("Úrkoma (mm)")
plt.ylabel("Fjöldi mælinga")
plt.title("Dreifing úrkomu")
plt.grid(axis="y")
plt.show()