# app.py

import json # Import inutil
import os
from utils import safe_divide, process_data
from file_process import read_file_content, write_data
# Nu toate importurile sunt folosite (Problema 3: Import nefolosit)
import sys 

# Problema 4: Securitate - Vulnerabilitate la Command Injection
def run_command(filename):
    # DANGEROUS: Permite unui utilizator să injecteze comenzi suplimentare
    os.system("cat " + filename) 

def main():
    # Bug: Potențială ZeroDivisionError dacă divisor e 0
    result = safe_divide(10, 2)
    print(f"Result: {result}")
    
    # Folosim funcția cu problemă de stil
    numbers = [5, 10, 15]
    total_sum = process_data(numbers)
    print(f"Sum: {total_sum}")

    # Apelăm funcția periculoasă
    user_input = "file.txt; echo 'Hacked'" 
    run_command(user_input)

if __name__ == "__main__":
    main()