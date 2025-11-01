# loop_example.py

# Problema 1: Stil - Nume variabilă neclar (x în loc de index sau i)
def print_loop():
    # Loop-ul rulează de la 0 la 9 (10 iteratii)
    for x in range(10): 
        # Problema 2: Stil - Utilizare funcție print ineficientă (folosirea operatorului +)
        output = "Numărul curent este: " + str(x)
        print(output)
        
    # Problema 3: Cod mort (Variabilă nefolosită)
    unused_limit = 10 

if __name__ == "__main__":
    print_loop()