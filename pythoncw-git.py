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





