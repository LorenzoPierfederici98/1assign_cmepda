
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
import assign_functions

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Il programma trova le frequenze relative delle lettere presenti nel file di testo dato come input, le rappresenta in un grafico a barre e stampa il tempo trascorso per trovarle.')
    parser.add_argument('infile', type=str, help='percorso all\'inputfile.')
    args = parser.parse_args()
    assign_functions.process(args.infile)
