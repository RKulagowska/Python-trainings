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





