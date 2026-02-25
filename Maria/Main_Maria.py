#importo prima la libreria Numpy

import numpy as np    

#definisco il nome del file dove salveremo i risultati delle analisi
file_risultati = "risultati_array1D.txt"

#funzione per salvare i risultati sul file
def salva_su_file(testo):
    with open(file_risultati, "a") as f:  #apro il file in modalità append
        f.write(testo + "\n")  #scrive la riga e va a capo


#funzione per leggere il file
def leggi_arrayfile(nome_file):
    try:
        arr = np.loadtxt(nome_file, dtype=int)  # legge direttamente numeri separati da spazi e li mette in un array numpy
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
    salva_su_file("La media è:" + str(media))

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
def indice_minimo(arr):   #indice del valore minimo
    indice_min = np.argmin(arr) #trovo la posizione (indice) del valore minimo
    valore_min = arr[indice_min] #prendo il valore che si trova in quell'indice
    print("Indice valore minimo:", indice_min, ", il valore minimo è", valore_min)
    salva_su_file("Indice valore minimo: " + str(indice_min) + ", Valore minimo: " + str(valore_min))

def indice_massimo(arr):   #indice del valore minimo
    indice_max = np.argmax(arr)
    valore_max = arr[indice_max]
    print("Indice valore massimo:", indice_max, ", il valore massimo è", valore_max)
    salva_su_file("Indice valore massimo: " + str(indice_max) + ", Valore massimo: " + str(valore_max))

def trova_mediana(arr):
    mediana = np.percentile(arr,50)
    print("La mediana è", mediana)
    salva_su_file("Median: " + str(mediana))

def trova_posizione_ordinata(arr, valore = 19):   #mi trova la posizione dove inserire quel valore (di default 19) suggerito dall'utente
    arr_ordinato = np.sort(arr) #prima ordino l'array in modo crescente
    print("Array ordinato in maniera crescente:", arr_ordinato )
    ordinata = np.searchsorted(arr_ordinato, valore)  #trovo la giusta posizione di quel valore nell'array
    print("La posizione per inserire il valore ", valore, "è ", ordinata)

    salva_su_file("Array ordinato:" + str(arr_ordinato))
    salva_su_file("Posizione per inserire " + str(valore) + ":" + str(ordinata))



#main 
while True:
    scelta = int(input("\nScrivi 1 per eseguire una nuova operazione, 0 per uscire: "))
    if scelta == 0:
        print("Peccato, ti sei perso un programmino per nulla male. Ciao!")
        break

    elif scelta == 1:
        dim = int(input("\nScrivi 1 per lavorare su un array 1D, 2 per un array 2D: "))

        if dim == 1:
            nome_file = input("Inserisci il nome del file contenente l'array 1D: ")
            array = leggi_arrayfile(nome_file)

            if array is None:
                print("Errore nella lettura del file. Riprova.")
                continue
            
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
            pass
            
        else:
            print("Dimensione non valida, scegli 1 o 2")

    else:
        print("Dimensione non valida, scegli 0 o 1")


    




