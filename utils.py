# utils.py

# Problema 1: Bug Logic (împarte la 0 dacă lista e goală)
def safe_divide(a, b):
    return a / b

# Problema 2: Stil (nume variabilă nepotrivit și ineficiență)
def process_data(data_list):
    total = 0
    # Nume variabilă 'idx' ar trebui să fie 'element' sau 'item'
    for idx in data_list:
        total = total + idx

    print ("Total procesat: " + str(total))
    return total