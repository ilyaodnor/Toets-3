import time, os, sys,math
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

def bereken_wachttijd(olibollen, appelflappen):
    wachttijd = 0
    olibollen_copy_bakken = olibollen
    olibollen_copy_verpakken = olibollen
  
    while olibollen_copy_bakken > 0:
        olibollen_copy_bakken -= 15  
        wachttijd += 75  

    while olibollen_copy_verpakken > 0:
        olibollen_copy_verpakken -= 10  
        wachttijd += 15  

    while appelflappen > 0:
        appelflappen -= 3  
        wachttijd += 20  

 
    wachttijd_in_minuten = math.ceil(wachttijd/60)
    return wachttijd_in_minuten
