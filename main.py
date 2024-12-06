from functions import*
from data import *

clear_screen()


print('Welkom in Olly & de Bolle !')
print('---------------------------')
time.sleep(2)

print('')
while True:
    olibollen = input_check('Hoeveel olibollen wilt u bestellen? (dat kost €1.15/stuk)', int)
    if olibollen>=0:
        break
    else:
        print('Ik snap dat niet.')
        time.sleep(1)

while True:
    appelflap = input_check('Hoeveel appelflapen wilt u? (dat kost €1.60/stuk)', int)
    if appelflap>=0:
        break
    else:
        print('Ik snap dat niet.')
        time.sleep(1)
text = '------ [UW BESTELLING] ------'
totaal = olibollen*OLIBOLLEN+appelflap*APPELFLAP

print(text)
if olibollen>0: print(f'Olibollen:   {olibollen} x €{OLIBOLLEN} = €{round(olibollen*OLIBOLLEN, 2)}')
if appelflap>0: print(f'Appelflap: {appelflap} x €{APPELFLAP} = €{round(APPELFLAP* OLIBOLLEN, 2)}')
print('-'*len(text)+'+')
print(f'Totaal:                €{round(totaal, 2)} ')  