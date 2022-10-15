# Copyright (C) 2022 l.pierfederici@studenti.unipi.it

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Functions for the first assignment."""
import logging 
import re
import time
import matplotlib.pyplot as plt

logging.basicConfig(level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')

def process(file_path):
    """Apre e legge il file dato da input e stampa il grafico a barre delle frequenze delle lettere nel file.
    Stampa il numero di caratteri senza spazi e il numero di righe dell'inputi file."""

    logging.info('Opening input file %s...',(file_path))
    with open(file_path, 'r', encoding = 'utf-8') as input_file:
        text = input_file.read()
        find_frequency(text)
        input_file.seek(0)
        lines = input_file.readlines()
        righe = len(lines)
        totale = 0
        for riga in lines:
            totale += len(riga)    
    logging.info('Il numero di caratteri compresi gli spazi è %d',(totale - 2*(righe-1)))
    logging.info('Il numero di righe del testo è %d',righe)
    logging.info('Done.')

def histogram(dictionary):
    """Mostra l'istogramma dei valori ordinati presenti in un dizionario.
    Usato nella funzione findefrequency."""

    plt.title('Istogramma delle frequenze relative')
    plt.xlabel('Lettere')
    plt.ylabel('Frequenze [%]')
    dictionary = dictionary.items()
    dictionary = sorted(dictionary)
    lettere,frequenze = zip(*dictionary)
    plt.bar(lettere, frequenze)
    plt.savefig('freq.pdf')
    plt.show()
    
def find_frequency(file):
    """Trova la frequenza relativa delle lettere dell'input file e ne stampa il grafico a barre.
    Inoltre stampa in output il tempo necessario a trovare le frequenze relative.
    Usato nella funzione process."""

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
    logging.info("--- tempo trascorso : %f s ---",(time.time() - start_time))
    histogram(letter_count)