# ćwiczenia różnych miejsc - poziom podstawowy 

# CW1-za pomocą print wydrukuj  Ucz się!'
# %%
 
print('Ucz się!')


# CW2 uzywając funkcji print oraz arg sep ustawionego na # wydrukuj 
'New#York#city'
# %%
print('New', 'York', 'city', sep='#')


# CW3 Podano  liczbe pi = 3.1415926535. Używając formatowania
#     f-string wydrukuj przybliżenie do 2 miejsca po przecinku
# %%

pi = 3.1415926535
pi = str(round(pi,2))

print(f'Przybliżenie liczby pi: {pi}')

# %%
pi = 3.1415926535
print(f'Przybliżenie liczby pi: {str(round(pi,2))}')


# CW4- przypisz do zmiennej numer wart 14 i wydrukuj do konsoli: Andersa 14/5
# %%

numer = '14' 
print('Andersa '+ numer + '/5')

age = 14 
print('Andersa '+ str(numer) + '/5')


# CW5 Przypisz zmienne.1=Python 2='3.8'. Wydrukuj "Uczę się języka Python w
#    wersji 3.8"
# %%

a = 'Python'
b = '3.8'
print('Uczę się języka ' + a +' w wersji '+ b)

a = 'Python'
b = '3.8'
print(f'Uczę się języka {a} w wersji {b}')


# CW6 Używając funkcji print (jedna linia jedna funkcja wydrukuj)( 40 -)
#--------------------------------------
#Happy New Year !
#--------------------------------------

# %%
print('-'* 40)
print('Happy New Year !')
print('-'*40)


# CW 7 Oblicz średnią geometryczną następujących liczb: 7, 14, 4.7, 13.
# %% 

import math

a = 7
b = 14
c = 4.7
d = 13

x = a*b*c*d

y = math.pow(x,1/4)

print(f'Średnia geometryczna podanych liczb: {y:.2f}')


# Cw 8 Wyznacz środek odcinka o końcach w punktach: A = (2, 6), B = (-6, 8).
# %%
x1 = 2
y1 = 6 
x2 = -6
y2 = 8
sx = (x1+x2)/2
sy = (y1+ y2)/2
print(f'Środek odcinka AB: ({sx}, {sy})')


# CW 9  Dany jest ciąg arytmetyczny an = 10 + 4n. Oblicz sumę 6-ciu 
#       początkowych wyrazów tego ciągu 
# %% 

n= 6
an = 10 + 4*n
a1= 10 + 4 * 1
a6 = 10 + 4 * 6 
suma = ((a1 + a6)/2)*n
print(f'Suma pierwszych 6 wyrazów tego ciągu wynosi:{suma}')


# CW 10 Wyznacz wartoć przyszła kwoty 1000 PLN przy rocznej stopie procentowej
#       4.53% kapitalizacji rocznej i 10 letnim okresie inwestycji.
#       Wynik zaokrąglij do pełnych groszy. 
# %%

PV = 1000 
i = 0.045
n = 10 
FV = PV *(1+i)**n
FV1= str(round(FV,2))
print(f'Wartosć końcowa inwestycji wynosi:{FV1} PLN')


# CW 11 Znajdź pierwiastki równania kwadratowego: x^2 + 5x + 4 = 0 
# %%

import math

a = 1
b = 5
c = 4

delta = b**2 - 4*a*c
d1= math.sqrt(delta)

x1 = (-b-d1)/(2*a)
x2 = (-b+d1)/(2*a)

print(f'x1 = {x1}\nx2 = {x2}')


# CW 12 Dany jest nieskończony ciąg geometryczny:1, 1/2,1/4,1/8. Oblicz sume 
#       tego ciągu 
# %% 

a1 = 1
q = 1/2
s= a1/(1-q)
print(f'Suma ciągu wynosi: {s}')


# CW 13 Oblicz odchylenie standardowe (estymator obciążony) następującego 
#       zestawu danych: 15, 10, 7.
#
# %%

x1 = 15 
x2 = 10
x3 = 7 

sr= (x1 + x2 + x3) / 3
var= ((x1-sr)**2 + (x2-sr)**2 + (x3-sr)**2)/3
varp = var**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {varp:.2f}')


# CW 14 Z text = 'PKO-84444567789769415-PLN' wytnij kod sklejając trzy
#       pierwsze i trzy ostatnie znaki. Wydrukuj
# %% 

text = 'PKO-84444567789769415-PLN'

# new = text[:3] + text[-3:], print(new)

print(text[:3] + text[-3:])


# CW 15 Z tekstu: string = '1 0 0 1 0 1'  usuń spacje. wynik potraktuj jako 
#       binarny i przedstaw w zapisie dziesiętnym. 
# %% 

string = '1 0 0 1 0 1'

new = string[::2]
new1 = int(new,2)
print(f'Wynik to : {new1}')


# CW 16 Podano zmienne: var1 = 13.5, var2 = 123, var3 = 'True'
#       Wydrukuj typ każdej zmiennej w osobnej linii. 
# %% 

var1 = 13.5
var2 = 123
var3 = 'True'

print(str(type(var1)))
print(str(type(var2)))
print(str(type(var3)))


# CW 17 text = 'sfhyebdfnfoguebsdmakolnnp dttdp nnt p at   pp' zlicz liczbę 
#       wystąpień litery 'p'. 
# %%

text = 'sfhyebdfnfoguebsdmakolnnp dttdp nnt p at   pp'
x = text.count('p')
print(f'Liczba wystąpień: {x}')

print(f"Liczba wystąpień: {text.count('p')}")


# CW 18  Odwróć kolejność znaków w: text = 'Happy New Year!'
# %% 

text = 'Happy New Year!'
# text1= text[::-1]
print(text[::-1])


# CW 19 Sprawdź, czy zmienna: x=False, jest obiektem typu bool.Wydrukuj wynik. (Użyj funkcji isinstance().
# %%

x = False
print(isinstance(x, bool))


# CW 20 podano: text = 'szkoła zaczna się.'Zmień pierwsza literę na dużą 
# %% 

text = 'szkoła zaczna się.'
print(text.capitalize())


# cw 21 Z adresu url: url = ('https://www.flynerd.pl/2018/12/darmowy-kurs-z-sieci-neuronowych)
#       wytnij nazwę ścieżki po ostatnim znaku '/'. Następnie zamień wszystkie
#       myślniki na spacje.
# %%

url = 'https://www.flynerd.pl/2018/12/darmowy-kurs-z-sieci-neuronowych'
url1 = url.split('/')[-1]
print(url1.replace('-',' '))


# CW 22 Podano:text = '    Nasz nowy dom      ' usuń biale znaki. 
#%%

text = '    Nasz nowy dom      '
print(text.strip())   


# CW 23 Podano: text = 'xxx-ccc--dd-123' usuń myślniki 
#%%

text = 'xxx-ccc--dd-123'
print(text.replace('-',''))


# CW 24 Dane są nazwy : a = 'nowy.jpg' b = 'nowy.docx'
#       sprawdź czy .jpg.   podaj wyniki za pomocą true i false
# %% 

a = 'nowy.jpg'
b = 'nowy.docx'

x = a.endswith('jpg')
y = b.endswith('jpg')
print(f'code1: {x}\ncode2: {y}')


# CW 25 Podano:text = 'New Year' zamień wszystkie duże litery na małe. 
#%%

text = 'New Year'
print(text.lower())  


# CW 26 Podano:text = 'New Year' zamień wszystkie litery na duże 
#%%

text = 'New Year'
print(text.upper())  


# CW 27 Podano: text = 'New,York,City' Podziel tekst według przecinka 
#       otrzymując listę. 
# %%

text = 'New,York,City'
print(text.split(','))


# Cw 28  Podano: num = 11  . Podaj jako numer 4 cyfrowy (0011)
#%% 

num = 11
print(str(num).zfill(4))


# CW 29 sprawdź czy dane:dane1 = 'Nowa Klasa-2a' dane2 = 'NowaKlasa2a'
#       składają się tylko ze znaków alfanumerycznych 
# %%

dane1 = 'Nowa Klasa-2a'
dane2 = 'NowaKlasa2a'
print(f'dane1: {dane1.isalnum()}\ndane2: {dane2.isalnum()}')


# CW 30 Dla zmiennej sentence= „Kurs Pythona jest prosty i przyjemny.”, :
#       Policz wszystkie znaki w napisie
#       Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
#       Wyświetl znaki: 8,czwarty od końca
#       Wprowadź do zdania 2 błędy ortograficzne 
#%%

sentence = 'Kurs Pythona jest prosty i przyjemny.'

print(len(sentence))
print(sentence[18:24])
print(sentence[7])
print(sentence[-4])

x = sentence.replace('u','ó')
print(x)


# CW 31 Podano zbiory: A = {2, 4, 6, 8, 10, 12}, B = {4, 10, 20, 40}
#       Wyznacz różnicę symetryczną zbiorów A i B. 
#%%

A = {2, 4, 6, 8, 10, 12} 
B = {4, 10, 20, 40}
x = A.symmetric_difference(B)

print(f'Wynik końcowy: {x}')


# CW 32 Podane są dwa zbiory X = {'1001', '1002', '1105'}, 
#       Y = {'77002', '9704', '1105'}
#       Podaj dane występujące w obu zbiorach 
#%%

x = {'1001', '1002', '1105'}
y = {'77002', '9704', '1105'}
z = x.intersection(y)
print(f'W obu zbiorach występują dane : {z}')


# CW 33 Tupla default = ('AA', 'A', 'AAA', 'A', 'AAA')
#       zwróć liczbę wystąpień znaków 'AA'
# %%

X = ('AA', 'A', 'AAA', 'A', 'AAA')
print(f"WYSTĘPUJE: {X.count('AA')}")


# CW 34 Polącz 2 podane tuple 
#%%

nowy = ('1a', '7a', '8a')
stary = ('1', '2', '3')

dane = nowy + stary
print(dane)


# CW 35 Zagnieźdź te obiekty w jeden obiekt typu tuple
#%% 
nowy = ('1a', '7a', '8a')
stary = ('1', '2', '3')

dane = (nowy, stary)

print(dane)


# CW 36 Istnieje tupla members = (('Dom', 1), ('Dach', 3))
#       Wstaw pomiędzy  krotkę ('Okno', 2) 
#%%

members = (('Dom', 1), ('Dach', 2))
x1 = members[0], ('Okno', 3), members[1]

print(x1)


# CW 37 Powstała w cw 36 tuple : (('Dom', 1), ('Okno', 3), ('Dach', 2))
#       Posortuj rosnąco  po drugim elemencie i alfabetycznie po pierwszym   
#%%

dane = (('Dom', 1), ('Okno', 3), ('Dach', 2))

x = tuple(sorted(dane, key=lambda item: item[1]))
y = tuple(sorted(dane))
print(f'Rosnąco: {x}')
print(f'Malejąco: {y}')


# CW 38 podano: text = 'Happy New Year!.' Wykonaj kroki:
#       Zamień wszystkie litery na małe.
#       Usuń spacje iwykrzzyknik.
#       Utwórz zbiór składający się z wszystkich liter w tak przetworzonym 
#       tekście.
#       usuń z tego zbioru litery 'e' i 'i' 
#       Wydrukuj liczbę elementów pozostałych elementó 
# %% 

text = 'Happy New Year!.'
x = {'a', 'i'}

text = text.lower()
text = text.replace(' ','')
text = text.replace('!','')

text1 = set(text)
result = text1.difference(x)

print(f' Pozostało: {len(result)} elementów.')


# CW 39 Z podanej tupli wciąg NEW
#%%

stocks = (('OLD', ('NEW', 'zws')), ('land', ('mean', 'zzz')))

x = stocks[0][1][0]
print(x)


# CW 40 porozdzielaj x = '1,2,3,4,5,6, y = 'python java php sql sas'
#       z = '#gym#fit#mood'
# %%

x = '1,2,3,4,5,6'.split(',')
y = 'python java php sql sas'.split()
z = '#gym#fit#mood'.split('#')
print(x)
print(y)
print(z)


# CW 41  Dodaj 2 listy i wydrukuj a = [4, 5, 3, 3], b = [9, 7]
# %%

a = [4, 5, 3, 3]
b = [9, 7]

a.extend(b)
print(a)


# CW 42 Podany jest: text = 'Programowanie jest miłe i przyjemne'
#       Zamień duże litery na małe, zastąp polskie znaki 
#       Utwórz listę składającą się z unikalnych znaków w tekście. 
#       Usuń spację z tej listy oraz posortuj od a do z. 
#       Wydrukuj 10 pierwszych elementów tej listy.
#%%

text = 'Programowanie jest miłe i przyjemne'

text = text.lower().replace('ł','l')
x = list(set(text))
x.remove(' ')
x.sort()

print(x[:10])


# CW 43 Do listy: kolor = ['zielony', 'niebieski', 'biały'] dodaj 'granat'
#%% 

kolor  = ['zielony', 'niebieski', 'biały']
kolor.append('granat')
print(kolor)


# Cw 44 Podana jest lista: New = ['02', '03', '18']
#       Dodaj do tej listy  '01' na początku listy.
#       Następnie usuń nazwę pliku '18'.
#%%

New = ['02', '03', '18']
New.insert(0, '01')
New.remove('18')
print(New)


# CW 45 Podana jest lista = ['New', 'York', 'City'] Połącz 
#       elementy listy znakiem '@'. Dodaj # początku tekstu
#%%

lista = ['New', 'York', 'City']
print('#' + '@'.join(lista))


# CW 46 Posortuj tuple od z do a : a = ('C++', 'sql', 'java','python')
#%%

a = ('C++', 'sql', 'java','python')
a = tuple(sorted(a))
print(a)


# CW 47 Podana jest lista = ['1', '2', '1', '3', '1']
#       zlicz wystąpienia '1'. 
#%%

lista = ['1', '2', '1', '3', '1']
print(f"Występuje: {lista.count('1')}")


# CW 48 do podanego słownika dodaj Litwa:Wilno, utwórz listę stolic 
#       posotowaną od A do Z 
#%%

capitals = {'Polska': 'Warszawa', 'Ukraina': 'Kijów', 'Włochy': 'Rzym'}
capitals['Litwa'] = 'Wilno'
x = sorted(list(capitals.values()))
print(x)


# CW 49 Z podanego słownika wydrukuj wartosc '4'. Gdy klucz nie występuje w 
#       słowniku zwróć wartość 'brak'    
#%%

dane = {'1': 'A', '2': 'B', '3': 'C'}
x = dane.get('4', 'brak')
print(x)


# CW 50 Utwórz słownik z następujących par (klucz, wartość): 
#       1, 'a'; 2, 'b'  ;3, 'c' 
#%%

new = {1:'a', 2:'b', 3:'c'}
print(new)


# CW 51 Podany jest słownik, wyciąg wszystkie klucze.
#%%

new = {1:'a', 2:'b', 3:'c'}
print(new.keys())


# CW 52 Podany jest słownik, wyciąg wszystkie wartosci.
#%%

new = {1:'a', 2:'b', 3:'c'}
print(new.values())


# CW 53 Podany jest słownik, wyciąg wartosci dla 3.     
#%%

new = {1:'a', 2:'b', 3:'c'}
print(new[3])
print(new.get(3))


# CW 54 Podany jest słownik, wyciąg wszystkie wartosci klucze(tuple).     
#%%

new = {1:'a', 2:'b', 3:'c'}
print(new.items())


# CW 55 Podany jest słownik. Wydobądź cechę dla ten medium
# %%
items = {
    1: {'small': 's'},
    2: {'medium': 'm'},
    3: {'large': 'l'}
}
print(items[2]['medium'])


# CW 56 Podany jest słownik. Wydobądź wartosc klucza 1
# %%
items = {
    1: {'small': 's'},
    2: {'medium': 'm'},
    3: {'large': 'l'}
}
print(items[1])


# CW 57 Podany jest słownik. Wydobądź zmień ceche dla 'medium' na 'M'
# %%
items = {
    1: {'small': 's'},
    2: {'medium': 'm'},
    3: {'large': 'l'}
}
items[2]['medium']= 'M'
print(items[2])


# CW 58 Podany jest słownik. dodaj: 4:{'super large':'xl'}
# %%
items = {
    1: {'small': 's'},
    2: {'medium': 'm'},
    3: {'large': 'l'}
}
items['4'] = {'super large': 'xl'}
print(items.values())


# CW 59 Podany jest słownik. skasuj:  2: {'medium': 'm'},
# %%
items = {
    1: {'small': 's'},
    2: {'medium': 'm'},
    3: {'large': 'l'}
}
items.pop(2)
print(items)


# CW 60 Podany jest słownik.Znajdź posortowaną od a do z listę unikalnych 
#       wartości. 
#%%

items = {
    1: 'small',
    2: 'medium',
    3: 'large',
    4: 'medium',
    5: 'large'
}
    
x = list(set(items.values()))
x.sort()
print(x)


# CW 61 Podana jest lista. Przekształć tę listę w słownik (indeks, ticker).       
#%%

lista = ['A', 'C', 'E', 'F', 'N','X', 'K', 'L', 'T', 'Z']

print(dict(enumerate(lista)))


# CW 62 Podano hasło: x = 'mojehaslo!!!!' Sprawdź, czy ma odpowiednią długość
#       min 10 znaków. Jeżeli tak, wydrukuj 'OK', w przeciwnym razie
#       'Hasło zbyt krótkie'.
#%%

x = 'mojehaslo!!!!'
if len(x) >= 11:
    print('Hasło poprawne')
else:
    print('Hasło zbyt krótkie')

  
# CW 63 czy podany pliku: x = 'mojedane.xlsx'. jest z rozszerzeniem 'xlsx'. 
#       Wydrukuj 'TAK' lub 'NIE'.
# %% 

x = 'mojedane.xlsx'

if x.endswith('.xlsx'): 
    print('TAK')
else:
    print('NIE')

  
# CW 64 Podano hasło: x = 'mojehaslo!!!!' Sprawdź, czy ma odpowiednią długość
#       min 10 znaków oraz zwiera znak specjalny '!'. 
#       Jeżeli tak, wydrukuj 'Hasło poprawne', w przeciwnym razie 'Hasło 
#       niepoprawne'.
#%%

x = 'mojehaslo!!!!'
if len(x) >= 11 and '!' in x:
    print('Hasło poprawne')
else:
    print('Hasło zbyt krótkie')

  
# CW 65 Podany jest łańcuch znaków: x = 'DAAAGGTHTYYYY' Sprawdź czy Składa się
#       tylko z dużych liter. Jeśli tak wydrukuj 'TAK'.
#%%

x = 'DAAAGGTHTYYYY'
if x.capitalize():
    print('TAK')

  
# CW 66 Podana jest zmienna:x = 22.0 Zbadaj czy to typ int. Wydrukuj 'TAK'
#     lub 'NIE'.
#%%

x = 22.0
if isinstance(x,int):
   print('TAK')
else:
    print('NIE')


# CW 67 Podana jest lista: x = ['02134', '24253']. Sprawdź 
#       czy  y:  = '02135'występuje w liście x. Jeśli nie dodaj 
#%%

x = ['02134', '24253']
z = '02135'

if not z in x:
    x.append(z)
    print(x)
    
    
# CW 68 Podany jest słownik: project_ids = {'01': 'open','02': 'new',
#       '03': 'in progress','04': 'completed'}
#       Wykorzystując instrukcję warunkową sprawdź, czy status projektu z 
#       id = '02' jest ustawiony na 'new'. Jeśli tak, zmień ten status na 
#       'open'.
#%%
project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
    print(project_ids)

   
# CW 69 Napisz program, który sprawdzi czy podany element: item = '001' 
#       występuje w liście: items = ['001', '000', '003', '005', '006']
#       Jeżeli tak, to usuń ten element z listy. Wydrukuj otrzymaną listę. 
# %% 
item = '001'
items = ['001', '000', '003', '005', '006']

if item =='001':
    items.pop(0)
    print(items)

#%%
if item in items:
    items.remove(item)
 print(items)


# CW 70  Napisz program, który z podanej listy zwróci listę wartości powyżej
#        0.5:
# %%

data = [0.44, 0.51, 0.8, 0.57, 0.66, 0.12]
new = []

for i in data:
    if i > 0.5:
        new.append(i)
print(new)


# CW 71 Podana jest lista  = [1, 5, 3, 2, 2, 4, 2, 4]. Usuń duplikaty zachowaj 
#       kolejność. wynik: [1, 5, 3, 2, 4]      
# %% 

lista = [1, 5, 3, 2, 2, 4, 2, 4]
x = []
for i in lista:
    if not i in x:
        x.append(i)
print(x)


# CW 72 Podana jest lista = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
#       Usuń liczby nieparzyste i zwróć pozostałe. 
# %% 
    
lista = [1, 16, 4, 5, 41, 9, 10, 56, 23, 24]
x = []
for i in lista:
    if not i % 2 != 0:
        x.append(i)
print(x)


# CW 73 Podany jest słownik> Kluczem jest 3-literowy kod spółki (ticker), 
#       wartością cena zamknięcia.
#       Przeprowadź iterację po słowniku. Wydrukuj kody (tickery) tych spółek, 
#       których cena zamknięcia jest większa niż 100.00 PLN.
#%%

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for i,y in gaming.items():
    if y > 100:
        print(i)


# CW 74 Znajdź wszystkie liczby dwucyfrowe podzielne przez 10 oraz 
#       niepodzielne przez 3. Wynik wydrukuj w postaci wartości 
#       rozdzielonych przecinkiem. 
# %% 
x = []
for i in range(10,100):
    if i % 10 == 0 and i % 3 != 0:
        x.append(str(i))
print(','.join(x))


# CW 75 Napisz program, który utworzy histogram - rozkład częstości w postaci 
#       słownika z podanych wartości: items = ['x', 'y', 'z', 'y', 'x', 'y', 
#       'y', 'z', 'x'] wynik: {'x': 3, 'y': 4, 'z': 2}
# %% 

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
new = {}
for i in items:
    if i not in new.keys():
        new[i] = 1
    else:
        new[i] += 1 
 print(new)


# CW 76 Podany jest poniższy tekst. Utwórz listę słów z podanego tekstu. 
#       Następnie dokonaj standaryzacji (zamień duże litery na małe, usuń znaki
#       interpunkcyjne). Wydobądź tylko wyrazy z długością powyżej 10 znaków.
#       wynik:['programowania', 'przeznaczenia', 'rozbudowanym', 'standardowych']
#%%

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

text1 = text.split()
text1 = [word.lower() for word in text1]
text1 = [word.replace('.','').replace(',','') for word in text1]
text1 = [word for word in text1 if len(word)>10]


# CW 77 Podana jest lista  = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]. 
#       Przypisz 0 dla wartości mniejszych niż 0.5 oraz 1 dla wartości większych 
#       lub równych 0.5. 
#%%

lista = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
new = []
for i in lista:
    if i < 0.5:
        i = 0
    else:
        i = 1
    new.append(i)
print(new)

# CW 78 Napisz program, który porówna dwie listy i zwróci wartość True w 
#       przypadku gdy listy będą zawierały co najmniej jeden ten sam element.
#       W przeciwnym razie zwróci wartość False. Użyj instrukcji break.
# %%

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
x = False
for item in list1:
    if item in list2:
        x = True
        break
print(x)

# CW 79 sprawdz czy podane hasło ma min 10 znaków, zawiera ! ( break ) 

ps = 'jnhvsoics!vd'
if len(ps) > 10:
    for i in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')
  
  
# CW 80 Zapytaj o imię. Sprawdź za pomocą funkcji while czy imię jest pow 3 
#       liter . Wydrukuj : Hej + imię 
#%%   
    
while True:
    name = input('Podaj imie: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Hej {}'.format(name))


# CW 81 Za pomocą while przeszukaj listę i zwróć jej elementy 
#%%   

lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False

idx = 0 
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1
    
    
# CW 82 Za pomocą while sprawdź czy zawiera 13. Jełi tak wydrukuj znaleziono
#%%

numbers = [23, 12, 53, 13, 65, 1, 45]
x = 13
idx = 0 
while idx < len(numbers):
    if numbers[idx] == x :
        flaga = True 
        break
    idx += 1
if flaga:
     print('Znaleziono')


# CW 83 Popros o podanie kodu Pin i sprawdż czy podano poprawny tj '0000' Jesli
#       tak poinformuj że zalogowano
#%%        

KOD_PIN = '0000'

pin = input('Podaj kod pin: ')
while pin != KOD_PIN:
    pin = input('sprobuj jeszcze raz: ')
print('Zalogowany')


# CW 84 Popros o podanie kodu Pin i sprawdż czy podano poprawny tj '0000' Jesli
#       tak poinformuj że zalogowano. Powtórz jesli zły kod i wyrzuć po 3 próbach
#%%   

KOD_PIN = '0000'
pin = ''
counter = 0 

while pin != KOD_PIN and counter < 3:
    pin = input('Podaj kod pin: ')
    if pin == KOD_PIN:
        print('zalogowany')
        break
    counter += 1 
else:
    print('Zbyt dużo prób')


# CW 85 # z podanej listy wyprintuj wszystkie oprócz 99 
# %%

lista = [1, 2, 99, 4, 5]
for i in lista:
    if i == 99:
        continue
    print(i)
    
    
# CW 86 Za pomocą continue zastąp # ' ' i wudrukuj 
#%% 

hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result+ char
print(result) 


# CW 87 Podana jest lista spółek z indeksu WIG.GAMES wraz z ceną zamknięcia i 
#       walutą. Używając instrukcji continue zbuduj pętlę, która zmieni cenę 
#       zamknięcia wyrażoną w USD na PLN. Przyjmij kurs USDPLN = 4.0.
#       Słownik gaming wydrukuj do konsoli.
#%%

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for ticker, info in gaming.items():
    if info[1] =='PLN':
        continue
    info[0] = info[0]* 4.0
    info[1] = 'PLN'
print(gaming)


# CW 88 Podana jest lista imion (jednego brak):
#        names = ['Jack', 'Leon', 'Alice', None, 'Bob']. Lista składa się tylko
#        z obiektów typu str lub wartości None. Posługując się instrukcją
#        continue wydrukuj  imiona (obiekty typu str).
#%%

names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if not isinstance(name, str):
        continue 
    print(name)
    
    
# CW 89 Sprawdz, czy podana liczba jest liczbą pierwszą:
#       number = 13. Jeśli jest pierwsza wydrukuj do konsoli 
#       '13 - liczba pierwsza'. W rozwiązaniu użyj instrukcji break.
#%%

number = 13

if number >1:
    for i in range(2,number):
        if number % i == 0:
            print(f'{number} - nie jest pierwsza')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} - nie jest pierwsza')
  
      
# CW 90 Napisz program, który wydrukuje do konsoli 10 pierwszych liczb 
#        pierwszych rozdzielonych przecinkiem. W rozwiązaniu użyj pętli while 
#        oraz instrukcji break.Oczekiwany wynik:2,3,5,7,11,13,17,19,23,29
#%%

counter = 0
number = 2
wynik = []

while counter < 10:
    for i in range(2,number):
        if number % i == 0 :
            break
    else:
        wynik.append(str(number))
        counter +=1
    number += 1
print(','.join(wynik))


# CW 91 Wykorzystując pętlę while policz ile trzeba czekać lat, aby zwrot z
#       ponizej opisanej inwestycji co najmniej się podwoił (pod uwagę bierzemy
#       tylko pełne okresy).Oznaczenia:
#       n - liczba okresów (w latach)
#       pv - present value - wartość obecna
#      r - stopa procentowa (roczna)
#       fv - future value - wartość przyszła
#       Opis inwestycji: pv = 1000 , r= 0.04
#       Oczekiwany wynik: Wartość przyszła: 2025.82 PLN. Liczba okresów: 18 lat
# %%

n = 1
pv = 1000
r = 0.04
fv = pv*(1+r)

while fv <= 2*pv:
    fv = fv*(1+r)
    n += 1
print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')    
    

# CW 92 Użyj algorytmu stochastycznego spadku wzdłuż gradientu do znalezienia
#       minimum funkcji straty określonej wzorem: L(w) = w^2- 4w. 
#       Pochodna tej gunkcji to 2 * w - 4. Przybliżona
#       zasada działania algorytmu:1. Zaczynamy od punktu startowego należącego
#       do dziedziny funkcji, weźmy:w_0 = -1
#       2. Określamy z góry maksymalną liczbę iteracji: max_iters = 10000 
#       3. Określamy zmienną, która pomoże nam kontrolować rozmiar kroku w
#       kierunku minimum, ustalmy jej wartość na 1: previous_step_size = 1
#       4. Określamy wskaźnik uczenia: learning_rate = 0.01
#       5. Określamy precyzję jaka wystarczy do znalezienia minimum:
#       precision = 0.000001
#       6. Definiujemy pochodną jako funkcję: derivative = lambda w: 2 * w - 4
#       Aby znaleźć minimum funkcji L należy poruszać się wzdłuż kierunku 
#       przeciwnego do kierunku wyznaczanego przez gradient funkcji L aktualizując 
#       wartość w_0 następująco: w_0 = w_0 - learning_rate * derivative(w_prev)
#       gdzie w_prev jest punktem z poprzedniej iteracji. Dla pierwszego korku 
#       jest to po prostu w_0. Zbuduj pętlę while, która pozwoli zatrzymać 
#       działanie algorytmu w momencie, gdy minimum zostanie odnalezione z 
#       zakładaną przez nas wartością precyzji lub gdy przekroczymy maksymalną 
#       liczbę iteracji.Oczekiwany wynik: Minimum lokalne w punkcie: 2.00
# %% 

max_iters = 10000 
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_prev - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1
 
print(f'Minimum lokalne w punkcie: {w_0:.2f}')


# CW 93 Napisz program, który sprawdzi czy podany element (target) znajduje 
#       się w posortowanej liście (numbers). Podane są:
#       numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 7
#       Zasada działania algorytmu:
#       1. Ustalamy indeks startowy (start) oraz końcowy (end) oraz flagę 
#       flag = None.
#       2. Dopóki indeks startowy jest nie większy niż indeks końcowy wybieramy
#       środkowy indeks (mid) listy (średnia arytmetyczna indeksu startowego i 
#       końcowego -> należy pamiętać o skonwertowaniu wyniku funkcją int). 
#       Jeżeli indeks startowy jest większy niż indeks końcowy kończymy 
#       działanie algorytmu.
#       3.  Sprawdzamy czy element listy dla tak obliczonego indeksu jest 
#       naszym szukanym (target). Jeżeli tak, ustawiamy flagę flag na wartość 
#       True  i kończymy działanie algorytmu. Jeżeli nie -> krok 4.
#       4. Sprawdzamy, czy wartość elementu listy dla indeksu mid jest mniejsza
#       niż target. Jeśli tak, to zwiększamy indeks startowy o 1. Jeśli nie, 
#       zmniejszamy indeks końcowy o 1 i przechodzimy do kroku 2.
#       Po wykonaniu pętli while w zależności od wartości flagi flag wydrukuj 
#       tekst: 'Znaleziono', 'Nie znaleziono'.
#%%

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
  mid = int((start + end) / 2)
  if numbers[mid] == target:
        flag = True
        break
  else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
 
if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')

    
# CW 94 Podane są zmienne: suma = 3000, counter = 0
#       Chcemy podzielić zmienną suma przez zmienną counter. W czasie działania 
#       pewnego programu zmienna counter może się zmieniać i przyjmować różne 
#       wartości.Używając klauzuli try... except... obsłuż wyjątek dzielenia 
#       przez zero. Jeżeli dzielenie zostanie wykonane poprawnie wynik wydrukuj
#       do konsoli. W momencie błędu do konsoli niech zostanie wydrukowany 
#       tekst:'Dzielenie przez zero.'
#%%

suma = 3000
counter = 0

try:
    result= suma/counter
    print(result)
except ZeroDivisionError:
    print('Dzielenie przez zero. ')
    
    
# CW 95 Czasem potrzebujemy otworzyć plik o pewnej nazwie nie wiedząc czy taki
#       plik istnieje. Zbuduj klauzulę try... except... obsługującą ten problem.
#       Fragment kodu do odczytania zawartości pliku:
#       with open('file.txt', 'r') as file:
#       content = file.read()
#       Jeżeli podany plik file.txt nie istnieje wydrukuj do konsoli: 
#       Nie znaleziono pliku.
#%%

try:
    with open('file.txt','r') as file:
        content = file.read()
except FileNotFoundError:
    print('Nie znaleziono pliku.')
    
    
# CW 96 Podany jest poniższy słownik: users = {'001': 'Marek', '002': 'Monika',
#        '003': 'Jakub'}. Spróbuj wydrukować wartość dla klucza:user_id = '004'
#       W przypadku błędu KeyError wydrukuj do konsoli tekst:
#       Klucz 004 nie występuje w słowniku. Dodawanie klucza...
#       Następnie dodaj ten klucz do słownika z wartością None i wydrukuj 
#       słownik users do konsoli. 
#       Oczekiwany wynik: Klucz 004 nie występuje w słowniku. Dodawanie klucza...
#       {'001': 'Marek', '002': 'Monika', '003': 'Jakub', '004': None}
#%%

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try: 
    print(users[user_id])
except KeyError:
    print(f'Klucz {user_id} nie występuje w słowniku. '
        'Dodawanie klucza...')
    users[user_id]= None
print(users)
  
