'''Andare a creare un sistema che prenda in input dei file txt o csv (anche o uno o l’altro).
Deve poter eseguire una o più di tutti i tipi di analisi che sono presenti nella parte a destra,
quelle coerenti col tipo di dato fornito. Alla fine deve POTER salvare un file dello stesso tipo o
di tipo TXT (anche solo uno dei due) Deve Potersi ripetere.'''

import numpy as np
import random

# Funzione somma colonne
def somma_colonne(mat):
    sum_c = np.sum(mat, axis=0)
    print("La somma per colonne è: ", sum_c)
    salva_su_file("\nSomma per colonne:\n" + str(sum_c))

# Funzione media per colonne
def media_colonna(mat):
    media_c = np.mean(mat, axis=0)
    print("La media per colonna è: ", media_c)
    salva_su_file("\nMedia per colonna:\n" + str(media_c))

# Funzione somma righe
def somma_righe(mat):
    sum_r = np.sum(mat, axis=1)
    print("La somma per righe è: ", sum_r)
    salva_su_file("\nSomma per righe:\n" + str(sum_r))

# Funzione media per riga
def media_riga(mat):
    media_r = np.mean(mat, axis=1)
    print("La media per riga è: ", media_r)
    salva_su_file("\nMedia per riga:\n" + str(media_r))

# Funzione che crea una nuova matrice (con numero di righe = numero di colonne di quella data) e fa il prodotto con quella data
def prodotto_B_random(mat):
    righe = mat.shape[1]
    colonne = random.randint(0,10)
    B = np.random.randint(0,100,righe * colonne).reshape(righe, colonne)
    print("La nuova matrice generata è:\n", B)
    mat_prodotto = np.dot(mat, B)
    print("La matrice prodotto è:\n", mat_prodotto)
    salva_su_file("\nNuova matrice generata:\n" + str(B) + "\nMatrice prodotto:\n" + str(mat_prodotto))

# Funzione che fa la trasposta della matrice
def trasponi(mat):
    trasp = np.transpose(mat)
    print("\nLa matrice trasposta è:\n", trasp)
    salva_su_file("\nMatrice trasposta:\n" + str(trasp))

# Funzione che restituisce la norma della matrice
def norma(mat):
    norma = np.linalg.norm(mat)
    print("La norma della matrice è: ",norma)
    salva_su_file("\nNorma della matrice:\n" + str(norma))

# Funzione che restituisce la covarianza della matrice
def covarianza(mat):
    cov = np.cov(mat.T)
    print("La matrice di covarianza è:\n", cov)
    salva_su_file("\nMatrice di covarianza:\n" + str(cov))


#funzione per leggere il file
def leggi_arrayfile(nome_file): 
    try:
        arr = np.loadtxt(nome_file, dtype=int)  # metto in un array il contenuto di del file ovvero numeri separati da spazi
        print("Array letto dal file:", arr)
        salva_su_file("Array letto da " + nome_file + ": " + str(arr))  #str trasforma l'array in stringa, altrimenti non posso concatenare un array a una str
        return arr   #restituisce l’array
    except:  #se succede qualche errore nel try
        print("Errore nella lettura del file.")
        return None   #segnala al main che non c’è array valido da usare
    
#funzione per calcolare la media
def media_arr(arr):
    media = np.mean(arr)  #media dei valori nell'array
    print("Media degli elementi:", media)
    salva_su_file("Media dell'array:" + str(media))

#funzione per trovare min e max
def min_max_arr(arr):
    minimo = np.min(arr)
    massimo= np.max(arr)
    print("Valore minimo:", minimo)
    print("Valore massimo:", massimo)
    salva_su_file("Minimo:" + str(minimo) + ". Massimo: " + str(massimo))

#funzione per calcolare la deviazione standard
def dev_std(arr):
    deviazione_std = np.std(arr)
    print("La standard deviation è:", deviazione_std)
    salva_su_file("Deviazione standard:" + str(deviazione_std))

#ANALISI POSIZIONALE
#funzione per trovare l'indice del valore minimo
def indice_minimo(arr):   #indice del valore minimo
    indice_min = np.argmin(arr) #trovo la posizione (indice) del valore minimo
    valore_min = arr[indice_min] #prendo il valore che si trova in quell'indice
    print("Indice valore minimo:", indice_min, ", il valore minimo è", valore_min)
    salva_su_file("Indice valore minimo: " + str(indice_min) + ", Valore minimo: " + str(valore_min))

#funzione per trovare l'indice del valore massimo
def indice_massimo(arr):   #indice del valore minimo
    indice_max = np.argmax(arr)
    valore_max = arr[indice_max]
    print("Indice valore massimo:", indice_max, ", il valore massimo è", valore_max)
    salva_su_file("Indice valore massimo: " + str(indice_max) + ", Valore massimo: " + str(valore_max))

#funzione per calcolare la mediana dell'array
def trova_mediana(arr):
    mediana = np.percentile(arr,50)
    print("La mediana è", mediana)
    salva_su_file("Median: " + str(mediana))

#funzione per trovare la posizione di un numero da inserire in un array ordinato scelto dall'utente
def trova_posizione_ordinata(arr, valore = 19):   #mi trova la posizione dove inserire quel valore (di default 19) suggerito dall'utente
    arr_ordinato = np.sort(arr) #prima ordino l'array in modo crescente
    print("Array ordinato in maniera crescente:", arr_ordinato )
    ordinata = np.searchsorted(arr_ordinato, valore)  #trovo la giusta posizione di quel valore nell'array
    print("La posizione per inserire il valore ", valore, "è ", ordinata)

    salva_su_file("Array ordinato:" + str(arr_ordinato))
    salva_su_file("Posizione per inserire " + str(valore) + ":" + str(ordinata))

#funzione per salvare i risultati sul file
def salva_su_file(testo):
    with open("risultati.txt", "a") as f:
        f.write(testo + "\n")

while True:
    scelta = int(input("\nScrivi 1 per eseguire una nuova operazione, 0 per uscire: "))
    if scelta == 0:
        break

    elif scelta == 1:
        dim = int(input("\nScrivi 1 per lavorare su un array 1D, 2 per un array 2D: "))

        if dim == 1:
            array = leggi_arrayfile("array1D.txt")

            if array is None:
                print("Errore nella lettura del file. Riprova.")
                continue # Non entra nel menu successivo, torna al principale
            
            while True:
                print("\n--- MENU ANALISI DATI ARRAY 1D ---")
                print("1 - Media")
                print("2 - Minimo e Massimo")
                print("3 - Deviazione Standard")
                print("4 - Indice minimo")
                print("5 - Indice massimo")
                print("6 - Mediana")
                print("7 - Posizione ordinata di un valore")
                print("0 - Torna al menu principale")

                op = input("Scegli un'opzione: ")

                if op == "1":
                    media_arr(array)
                elif op == "2":
                    min_max_arr(array)
                elif op == "3":
                    dev_std(array)
                elif op == "4":
                    indice_minimo(array)
                elif op == "5":
                    indice_massimo(array)
                elif op == "6":
                    trova_mediana(array)
                elif op == "7":
                    valore = int(input("Inserisci il valore di cui vuoi trovare la posizione nell'array ordinato:  "))
                    trova_posizione_ordinata(array, valore)
                elif op == "0":
                    break
                else:
                    print("Scelta non valida, riprova.")

        elif dim == 2:
            mat = leggi_arrayfile("array2D.txt")

            if mat is None:
                print("Errore nella lettura del file. Riprova.")
                continue # Non entra nel menu successivo, torna al principale

            while True:
                operazione = int(input("\nSeleziona l'operazione che vuoi eseguire sulla matrice:\n1) Somma per colonne"
                                "\n2) Media per colonna\n3) Somma per righe\n"
                                "4) Media per riga\n"
                                "5) Genera un'altra matrice e fai il prodotto matriciale tra le due\n"
                                "6) Trasponi la matrice\n"
                                "7) Norma della matrice\n"
                                "8) Matrice di covarianza\n"
                                "0) Per tornare al menu principale\n"))
                
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
                
                elif operazione == 0:
                    break
                
                else:
                    print("Operazione selezionata inesistente.")

        else:
            print("\nOpzione non valida.")

    else:
        print("\nScelta non valida.")