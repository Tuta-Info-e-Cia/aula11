"""
8 - Faça um Programa que converta metros para centímetros.
Faça um Programa que peça o
raio de um círculo, calcule e mostre sua área.
Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário.
"""

def converter_metros_para_centimetros():
    metros = float(input('Metros: '))
    centimetros = metros * 100
    print(f'{metros} m = {centimetros} cm') 



def calcular_area_circulo():
    raio = float(input('Informe o raio de um círculo: '))
    area = float((raio ** 2) * 3.14)  # (A = π r²) pi=3,1415
    print(f'Com um círculo de raio {raio} temos um círculo de área {area}.')   

def area_dobrada_do_quadrado():
    lado = float(input('Informe o lado de um quadrado: '))
    dobro = (lado**2) * 2                   
    area = lado**2  
    print(f'O dobro área do quadrado informado é de {dobro}')

def menu():
    while True:
        print('\n -- Menu de Opções --')
        print('1 - Converter metros para centímetros')
        print('2 - Calcular area do circulo')
        print('3 - Calcular area dobrada do quadrado')
        print(' 0 - Sair')

        opcao = input('Escolha uma opção:  ')
        if opcao == '1':
            converter_metros_para_centimetros()
        elif opcao == '2':
            calcular_area_circulo()
        elif opcao == '3':
            area_dobrada_do_quadrado()
        elif opcao == '0':
            print('Saindo do programa! Até logo!')
            break
        else:
            print('Opção Inválida!! - Tente Novamente....')

#iniciar o Menu
            
menu()