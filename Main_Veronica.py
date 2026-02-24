import numpy as np
import random
from Main import salva_su_file

def somma_colonne(mat):
    sum_c = np.sum(mat, axis=0)
    print("La somma per colonne è: ", sum_c)
    salva_su_file("operazioni.txt", "\nSomma per colonne:\n" + str(sum_c))

def media_colonna(mat):
    media_c = np.mean(mat, axis=0)
    print("La media per colonna è: ", media_c)
    salva_su_file("operazioni.txt", "\nMedia per colonna:\n" + str(media_c))

def somma_righe(mat):
    sum_r = np.sum(mat, axis=1)
    print("La somma per righe è: ", sum_r)
    salva_su_file("operazioni.txt", "\nSomma per righe:\n" + str(sum_r))

def media_riga(mat):
    media_r = np.mean(mat, axis=1)
    print("La media per riga è: ", media_r)
    salva_su_file("operazioni.txt", "\nMedia per riga:\n" + str(media_r))

def prodotto_B_random(mat):
    righe = mat.shape[1]
    colonne = random.randint(0,10)
    B = np.random.randint(0,100,righe * colonne).reshape(righe, colonne)
    print("La nuova matrice generata è:\n", B)
    mat_prodotto = np.dot(mat, B)
    print("La matrice prodotto è:\n", mat_prodotto)
    salva_su_file("operazioni.txt", "\nNuova matrice generata:\n" + str(B) + "\nMatrice prodotto:\n" + str(mat_prodotto))

def trasponi(mat):
    trasp = np.transpose(mat)
    print("\nLa matrice trasposta è:\n", trasp)
    salva_su_file("operazioni.txt", "\nMatrice trasposta:\n" + str(trasp))

def norma(mat):
    norma = np.linalg.norm(mat)
    print("La norma della matrice è: ",norma)
    salva_su_file("operazioni.txt", "\nNorma della matrice:\n" + str(norma))

def covarianza(mat):
    cov = np.cov(mat.T)
    print("La matrice di covarianza è:\n", cov)
    salva_su_file("operazioni.txt", "\nMatrice di covarianza:\n" + str(cov))

while True:
    scelta = int(input("\nScrivi 1 per eseguire una nuova operazione, 0 per uscire: "))
    if scelta == 0:
        break

    elif scelta == 1:
        dim = int(input("\nScrivi 1 per lavorare su un array 1D, 2 per un array 2D: "))

        if dim == 1:
            pass

        elif dim == 2:
            mat = np.loadtxt("array2D.txt", dtype=int)
            print("L'array 2D del file è il seguente:\n", mat, "\n")

            salva_su_file("operazioni.txt", "\nArray 2D su cui effettueremo le operazioni:\n" + str(mat))

            operazione = int(input("\nSeleziona l'operazione che vuoi eseguire sulla matrice:\n1) Somma per colonne"
                               "\n2) Media per colonna\n3) Somma per righe\n"
                               "4) Media per riga\n"
                               "5) Genera un'altra matrice e fai il prodotto matriciale tra le due\n"
                               "6) Trasponi la matrice\n"
                               "7) Norma della matrice\n"
                               "8) Matrice di covarianza\n"))
            
            if operazione == 1:
                somma_colonne(mat)

            elif operazione == 2:
                media_colonna(mat)

            elif operazione == 3:
                somma_righe(mat)

            elif operazione == 4:
                media_riga(mat)

            elif operazione == 5:
                prodotto_B_random(mat)

            elif operazione == 6:
                trasponi(mat)

            elif operazione == 7:
                norma(mat)

            elif operazione == 8:
                covarianza(mat)
            
            else:
                print("Operazione selezionata inesistente.")

        else:
            print("\nOpzione non valida.")
            continue
    else:
        print("\nScelta non valida.")
        continue