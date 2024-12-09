from functions import *
from data import *
import math
import time, os

clear_screen()

print('Welkom in Olly & de Bolle !')
print('---------------------------')
time.sleep(2)
while True:

    while True:
        olibollen = input_check('Hoeveel olibollen wilt u bestellen? (dat kost €1.15/stuk)', int)
        if olibollen >= 0:
            break
        else:
            print('Ik snap dat niet.')
            time.sleep(1)

    while True:
        appelflap = input_check('Hoeveel appelflapen wilt u? (dat kost €1.60/stuk)', int)
        if appelflap >= 0:
            break
        else:
            print('Ik snap dat niet.')
            time.sleep(1)

    zaken_olibollen = olibollen // 10
    totaal = (zaken_olibollen * OLIBOLLEN_ZAK + (olibollen - 10 * zaken_olibollen) * OLIBOLLEN + appelflap * APPELFLAP) if zaken_olibollen > 0 else (olibollen * OLIBOLLEN + appelflap * APPELFLAP)

    if totaal >= 50:
        korting = True
        verschil = totaal / 100 * KORTING
        totaal_voor_btw = totaal-verschil
    bereken_btw = totaal_voor_btw-(totaal_voor_btw/(1+BTW/100))

    print(text)
    if zaken_olibollen > 0:
        print(f'Olibollen (zak):   {zaken_olibollen:2} x €{OLIBOLLEN_ZAK:.2f} = €{round(zaken_olibollen * OLIBOLLEN_ZAK, 2):6.2f}')
        print(f'Olibollen (los):   {olibollen - 10 * zaken_olibollen:2} x €{OLIBOLLEN:.2f} = €{round((olibollen - 10 * zaken_olibollen) * OLIBOLLEN, 2):6.2f}')
    elif olibollen > 0 and zaken_olibollen == 0:
        print(f'Olibollen (los):   {olibollen:2} x €{OLIBOLLEN:.2f} = €{round(olibollen * OLIBOLLEN, 2):6.2f}')

    if appelflap > 0:
        print(f'Appelflap:         {appelflap:2} x €{APPELFLAP:.2f} = €{round(appelflap * APPELFLAP, 2):6.2f}')



    print('-' * len(text) + '+')
    print(f'Subtotaal:           {round(totaal, 2):6.2f}')
    if korting:
        print(f'Korting(7.5%):      -€{round(verschil, 2):6.2f}')

    print('-' * len(text) + '+')
    print(f'Totaal:                 €{round(totaal - verschil, 2):6.2f}')
    print(f'BTW (9%):               €{bereken_btw:>6.2f}')

    print(f'Wachtijd: {bereken_wachttijd(olibollen, appelflap)} minuten')

    if input_check('Wilt u nog iets bestellen?',bool):
        continue
    else:
        break

