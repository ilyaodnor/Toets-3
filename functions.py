import time, os, sys
from data import* 
def input_check(text, type, expected: list = None): 
    while True:
        if type == int:
            try:
                getal = int(input(text))
                return getal
            except ValueError:
                print("Voer in een integer!")
        elif type == str:
            string = input(f"{text} ").lower()
            if expected: 
                if string in expected:
                    return string
                else:
                    print('sorry, dat snap ik niet. ')
                    print(f"Voer in een van de volgende opties: {expected}")
            else:
                return string
        elif type == bool:
            try:
                waarde = input(text).strip().lower()
                if waarde in ['true', '1', 'yes', 'y', 'ja']:
                    return True
                elif waarde in ['false', '0', 'no', 'n', 'nee']: 
                    return False
                else:
                    print("Voer 'true' of 'false' in!")
            except ValueError:
                print("Voer een geldige waarde in!")
        else:
            print("Ongeldig type opgegeven!")

def clear_screen():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

