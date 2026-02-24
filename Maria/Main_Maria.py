#leggo prima il filetxt Array1D.txt

#per aprire e leggere il file

import numpy as np


file_risultati = "risultati_array1D.txt"

#funzione per salvare i risultati sul file
def salva_su_file(testo):
    with open(file_risultati, "a") as f:
        f.write(testo + "\n")


#funzione per leggere l'array del file
def leggi_arrayfile(nome_file):
    try:
        arr = np.loadtxt(nome_file, dtype=int)  # legge direttamente numeri separati da spazi
        print("Array letto dal file:", arr)
        salva_su_file(f"Array letto da {nome_file}: {arr}")
        return arr
    except:
        print("Errore nella lettura del file.")
        return None
    
#funzione per calcolare la media
def media_arr(arr):
    media = np.mean(arr)
    print("Media degli elementi:", media)
    salva_su_file("La media è:" + str(media))

#funzione per trovare min e max
def min_max_arr(arr):
    min = np.min(arr)
    max = np.max(arr)
    print("Valore minimo:", min)
    print("Valore massimo:", max)
    salva_su_file(f"Minimo: {min}, Massimo: {max}")

#funzione per calcolare la deviazione standard
def dev_std(arr):
    deviazione_std = np.std(arr)
    print("La standard deviation è:", deviazione_std)
    salva_su_file("Deviazione standard:" + str(deviazione_std))

#ANALISI POSIZIONALE
def indice_minimo(arr):   #indice del valore minimo
    indice_min = np.argmin(arr) #trova la posizione (indice) del valore minimo
    valore_min = arr[indice_min] #prende il valore minimo vero e proprio
    print("Indice valore minimo:", indice_min, ", il valore minimo è", valore_min)
    salva_su_file("Indice valore minimo: " + str(indice_min) + ", Valore minimo: " + str(valore_min))

def indice_massimo(arr):   #indice del valore minimo
    indice_max = np.argmin(arr)
    valore_max = arr[indice_max]
    print("Indice valore massimo:", indice_max, ", il valore massimo è", valore_max)
    salva_su_file("Indice valore massimo: " + str(indice_max) + ", Valore massimo: " + str(valore_max))

def trova_mediana(arr):
    pass

def trova_posizione_ordinata(arr):
    pass


#main CONTINUO STASERA.




