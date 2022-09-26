
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

"""First assignment for the CMEPDA course, 2022/23.
"""

import argparse
import re
import matplotlib.pyplot as plt




def process(file_path):
    """
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
#    print(text)
        find_frequency(text)
    print('Done.')

def histogram(dictionary):
    """Mostra l'istogramma dei valori presenti in un dizionario.

    Usato nella funzione findefrequency.
    """
    plt.title('Istogramma delle frequenze relative')
    plt.xlabel('Lettere')
    plt.ylabel('Frequenze [%]')
    dictionary = dictionary.items()
    dictionary = sorted(dictionary)
    x,y = zip(*dictionary)
    plt.bar(x,y)
    plt.show()


def find_frequency(file):
    """Trova la frequenza relativa delle lettere dell'input file e ne stampa il grafico a barre.

    Usato nella funzione process.
    """
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
   # print(letter_count)
    histogram(letter_count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    process(args.infile)
    
     
