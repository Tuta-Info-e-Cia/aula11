

""" 4. Faça um Programa que peça as 4 notas bimestrais
    e mostre a média."""

def calcular_media_notas():

    notas = []
    for i in range(1, 5):
        nota = float(input(f'Digite a {i}ª nota bimestral: '))
        notas.append(nota)
    media = sum(notas)/ len(notas)
    print(f'A média das notas é {media:.2f}')



#corpo principal do progama
#chamada da função

calcular_media_notas()


# n1 = float(input('Digite a primeira nota bimestral: '))
# n2 = float(input('Digite a segunda nota bimestral: '))
# n3 = float(input('Digite a terceira nota bimestral: '))
# n4 = float(input('Digite a quarta nota bimestral: '))
# media = float((n1 + n2 + n3 + n4) / 4)
# print(f'A média das notas informadas é {media:.2f}')    


