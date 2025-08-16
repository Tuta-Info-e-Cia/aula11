

""" 7 - Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário."""

def area_dobrada_do_quadrado():

    lado = float(input('Informe o lado de um quadrado: '))        
    dobro = (lado**2) * 2                   
    area = lado**2  
    print(f'O dobro área do quadrado informado é de {dobro}')
    