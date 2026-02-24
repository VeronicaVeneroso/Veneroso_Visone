'''Andare a creare un sistema che prenda in input dei file txt o csv (anche o uno o l’altro).
Deve poter eseguire una o più di tutti i tipi di analisi che sono presenti nella parte a destra,
quelle coerenti col tipo di dato fornito. Alla fine deve POTER salvare un file dello stesso tipo o
di tipo TXT (anche solo uno dei due) Deve Potersi ripetere.'''

#funzione per salvare i risultati sul file
def salva_su_file(file, testo):
    with open(file, "a") as f:
        f.write(testo + "\n")