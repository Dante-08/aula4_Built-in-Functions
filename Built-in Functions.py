# # len(): mostra o comprimento de strings apenas

# palavra = 'Olá, como vai!'
# print(len(palavra))

# # list[]: transforma valores de variavéis em uma lista, para fazer uma lista de forma manual basta usar []

# palavra2 = 'Python'
# lista = list(palavra2)
# print(lista)

# # tuple(): transforma qualquer valor de uma variavel de forma automatica em tupla que é uma coleção de elementos
# #  ordenados que são imutáveis, ou seja, uma vez criada, não é possível alterar seus valores, para fazer uma tupla de forma manual basta usar ()

# tupla = (10,0,8,25,2008)
# tupla = (50)
# print(tupla)

# # set():tranforma valores de variaveis em sequências não ordenadas e de elementos únicos, para criar de forma manual um conjunto basta usar {}

# conjunto = {10,80,70,50,35,27}
# print(conjunto)

# # range: A função range em Python gera uma sequência de números dentro de um intervalo dado

# n = list(range(5,100,8))
# print(n)

# sum(): soma todos os numeros de uma lista, mas caso tenha alguma string é dado um erro
# minha_lista = list(range(1,101))
# print(sum(minha_lista))

# min(): traz como resultado o menor numero de uma lista
# lista = list(range(1,50))
# print(min(lista))

# # max(): traz como resultado o maior numero de uma lista
# print(max(lista))

# .sort(): organiza uma lista colocando os numeros do menor para o maior
# -------------------------------------------------------------------------------------
notas = []

n1, n2, n3 = float(input('Digite sua nota: ')),float(input('Digite sua nota: ')),float(input('Digite sua nota: '))
notas += (n1,n2,n3)
media = sum(notas)/len(notas)
print('Notas ->',notas)
print('Média ->',media)




