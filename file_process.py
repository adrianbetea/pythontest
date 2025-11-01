# file_processor.py

import os

# Problema 1: Securitate - Lipsa de validare a căii (Path Traversal)
def read_file_content(path):
    # DANGEROUS: Permite citirea fișierelor din afara directorului de lucru
    with open(path, 'r') as f:
        return f.read()

# Problema 2: Stil - Folosirea unei variabile globale pentru a ține minte starea
FILE_COUNTER = 0

def write_data(data):
    global FILE_COUNTER
    # Numele fișierului este codat fix, lipsă de flexibilitate
    filename = "output.log"
    with open(filename, 'a') as f:
        f.write(data + '\n')
    FILE_COUNTER += 1
    return f"Scris în {filename}. Total operații: {FILE_COUNTER}"