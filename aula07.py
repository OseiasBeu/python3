#Operadores aritiméticos--------------------------------------------------------
## + - * /
##  ** // %
## ==

#Todo o operador precisa de operandos----------------------------------------------
#EX: 5*2==10, 5+2 ==7, 5/2 == 2.5
#EX: 5**2 ==25 , 5//2 == 2 , 5%2 == 1

#Ordem de Precedência-------------------------------------------------------
## Primeiro: ()
## Segundo: ** (outra forma é usando a função de potência pow(base, expoente)
## Terceiro: *, / , // , %
## Quarto:  + , -

#RAIZ QUADRADA------------------------------------------------------
##É O MESMO QUE ELEVAR UM NÚMERO A UM MEIO EXPOÊNTE
##EX: 81**(1/2) == 9.0
##EX: 25**(1/2) == 5.0

## A MESMA LÓGICA SE APLICA A RAIZ CÚBICA
##EX: 127**(1/3) == 33.08


#REPLICAR INFORMAÇÕES: --------------------------------------------
## 'OI'*5
## '=' * 20
print('='*20)
nome = input('Qual é seu nome:')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

#EXERCÍCIO:
## 5 + 3 * 2 == 11
## 3 * 5 + 4 ** 2 == 31
## 3* (5 + 4) ** 2 == 243

##Exercícios
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
p = n1 ** n2
di = n1 // n2
d = n1 / n2
r = n1 % n2
sub = n1 - n2

print('A soma é {}'.format(s))
print('A multiplicação é: {}'.format(m))
print('O produto é: {}'.format(p))
print('A divisão inteira é: {}'.format(di))
print('A divisão é: {:.3f}'.format(d))
print('O resto da divisão é: {}'.format(r))
print('A subtração é: {}'.format(sub))


