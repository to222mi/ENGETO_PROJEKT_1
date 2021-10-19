#!/usr/bin/env python
# coding: utf-8

# In[53]:


TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

cara = '-'*60
hlavicka = ('LEN','OCCURENCES','NR.' )

users = dict(
    bob = dict(
        password='123'
    ),
    ann = dict(
        password='pass123'
    ),
    mike = dict(
        password='password123'
    ),
    liz = dict(
        password='pass123'    
    )
)

# uzivatel zada jmeno + overeni
username = input('input username:')

# overit uzivatele
if username in users:
    passw = input('input password: ')
    if passw == str(users[f'{username}']['password']):
        print(
            cara,        
            f'Welcome to the app, {username}',
            f'We have {len(TEXTS)} texts to be analyzed',
            cara,
            sep= '\n'
        )
    else:
        print('invalid password, quitting...')
        quit()
else:
    print('username not in list of users, quitting...')
    quit()

    
# vyber text
text = int(input(f'Enter a number btw. 1 and {len(TEXTS)} to select: '))
if text in range(1,len(TEXTS)+1):
    print(cara)   
else:
    print(
        f'Such text not available, quitting...',
        cara,
        sep='\n'
    )
    quit()
    
# premenna na ulozenie slov z textu
vycistena_slova = list()

# rozdel text na slova
for slovo in TEXTS[text-1].split():
    vycistena_slova.append(
        slovo.strip(",.:;")
    )

# premenne na ukladanie titlecase, uppercase, lowercase, numeric a summ
titulni_prvni_pismeno = list()
velke_pismena = list()
male_pismena = list()
numericke = list()
suma = 0

# analyzuj text
for slovo in vycistena_slova:
    if slovo.istitle():
        titulni_prvni_pismeno.append(slovo)
    elif slovo.isupper():
        velke_pismena.append(slovo)
    elif slovo.islower():
        male_pismena.append(slovo)
    elif slovo.isnumeric():
        numericke.append(slovo)
        
#spocitaj vsetky cisla
for cislo in numericke:
    suma = suma +int(cislo) 
    
        
print(
    f'There are {len(vycistena_slova)} words in the selected text.',
    f'There are {len(titulni_prvni_pismeno)} titlecase words',
    f'There are {len(velke_pismena)} uppercase words',
    f'There are {len(male_pismena)} lowercase words',
    f'There are {len(numericke)} numeric strings',
    f'The sum of all numbers is: {suma}',
    sep='\n'
)

# spocitam vyskyty pre kazde slovo
pocty_slov: dict = dict()

for slovo in vycistena_slova:
    if len(slovo) not in pocty_slov:
        pocty_slov[len(slovo)] = 1
    else:
        pocty_slov[len(slovo)] = pocty_slov[len(slovo)] + 1

print(
    cara,
    f"{'     |     '.join(hlavicka)}",
    cara,
    sep='\n'
)

# zoradit slovnik vzostupne
pocty_slov_zoradene = sorted(pocty_slov.items())

# vypis pocty slov a zobraz graf
for pocet in pocty_slov_zoradene:
    print(pocet[0],(4-len(str(pocet[0])))*' ','|', int(pocet[1])*'*',' '*(20-int(pocet[1])),'|', pocet[1])

