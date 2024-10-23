nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media = (nota1 + nota2 + nota3)/3
situacao = media >= 7
nome = input('Digite seu nome: ')

print(f'''
Situação do aluno {nome}
Média ->  {media:.2}
Aprovado? -> {situacao}
''')