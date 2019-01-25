#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiíveis sobre ele.

a= input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))

print('Só tem espaço?', a.isspace())

print('É um número?', a.isnumeric())

print('É alfabético?', a.isalpha())

print('É alfanumérico?', a.isalnum())

print('Está em maiúscula?', a.isupper())

print('Está em minúscula?', a.islower())

print('Está capitalizada?', a.istitle())
