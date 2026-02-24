import numpy as np
import random

for i in range(10):
    righe = random.randint(0,10)
    colonne = random.randint(0,10)
    mat = np.random.randint(0,100,righe * colonne).reshape(righe, colonne)

    with open("array.txt", "a") as file:
        file.write("\n" + str(mat) + "\n")