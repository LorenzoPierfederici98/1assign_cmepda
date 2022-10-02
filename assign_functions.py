import logging 
import re
import time
import matplotlib.pyplot as plt


def process(file_path):
    """Apre e legge il file dato da input e stampa il grafico a barre delle frequenze delle lettere nel file.
    
    Stampa il numero di caratteri senza spazi e il numero di righe dell'inputi file.
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
        find_frequency(text)
        input_file.seek(0)
        lines = input_file.readlines()
        print(lines)
        totale = 0
        r = 0
        for riga in lines:
            totale += number_lines(riga)
            r += 1     

    print(f'Il numero di caratteri senza spazi è {totale}')
    print(f'Il numero di righe del testo è {r}')
    print('Done.')

def histogram(dictionary):
    """Mostra l'istogramma dei valori ordinati presenti in un dizionario.

    Usato nella funzione findefrequency.
    """
    plt.title('Istogramma delle frequenze relative')
    plt.xlabel('Lettere')
    plt.ylabel('Frequenze [%]')
    dictionary = dictionary.items()
    dictionary = sorted(dictionary)
    x,y = zip(*dictionary)
    plt.bar(x,y)
    plt.savefig('freq.pdf')
    plt.show()
    
def find_frequency(file):
    """Trova la frequenza relativa delle lettere dell'input file e ne stampa il grafico a barre.
    
    Inoltre stampa in output il tempo necessario a trovare le frequenze relative.
    
    Usato nella funzione process.
    """
    start_time = time.time()
    letter_count = {}
    file = file.lower()
    n = float(len(file))
    for letter in file:
        match = re.search("[a-z]", letter)
        boolean = bool(match)
        if boolean:
            if letter in letter_count:
                letter_count[letter] +=1
            else : letter_count[letter] = 1
    for letter in letter_count:
        letter_count[letter] = float(letter_count[letter]*100/n)
    print(f"--- tempo trascorso : {(time.time() - start_time)} s ---" )
    histogram(letter_count)

def number_lines(strn):
    """Inserisce gli elementi di una stringa separati da spazi in una lista e ne restituisce la lunghezza.
    """
    lista = re.split(r'',strn)
    return len(lista)