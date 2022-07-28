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







