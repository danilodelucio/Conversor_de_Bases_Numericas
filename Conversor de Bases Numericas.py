from random import randint
from time import sleep

sleep(0.5)
CorVermelho = '\033[1:31m'
CorAmarelo = '\033[1:33m'
CorAzul = '\033[1:34m'
CorRoxo = '\033[1:35m'
SemCor = '\033[m'

while True:
    print(CorAmarelo + '=' * 30)
    print('CONVERSOR DE BASES NUMÉRICAS')
    print('=' * 30)
    print('''[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\n[ 0 ] FINALIZAR PROGRAMA''')
    print('=' * 30 + SemCor)
    start = int(input('Escolha a base numérica: '))

    # BINÁRIO
    if start == 1:
        while True:
            print('(Digite [0] para voltar ao menu principal.)')
            n = int(randint(0, 999))
            decimalParabinario = int(bin(n)[2:])
            binario = decimalParabinario

            # RESULTADO BINÁRIO
            #print(binario)

            user = int(input(f'\nQual é o valor BINÁRIO de {n}?  '))

            if user == binario:
                print(CorAzul + '\nParabéns, você acertou! Vamos para a próxima...' + SemCor)
            elif user == 0:
                sleep(0.5)
                print(CorRoxo + 'VOLTANDO AO MENU PRINCIPAL...' + SemCor)
                sleep(1)
                break
            elif user != binario:
                print(CorVermelho + f'\nVocê errou, que pena! A resposta correta é \33[4m{binario}' + SemCor + '.')
                print('Vamos tentar de novo...')
            else:
                print('Comando inválido! Vamos tentar novamente...')
            print('-' * 30)
    # OCTAL
    elif start == 2:
        while True:
            print('(Digite [0] para voltar ao menu principal.)')
            n = int(randint(0, 999))
            decimalParaOctal = int(oct(n)[2:])
            octal = decimalParaOctal

            # RESULTADO OCTAL
            #print(octal)

            user = int(input(f'\nQual é o valor OCTAL de {n}?  '))

            if user == octal:
                print(CorAzul + '\nParabéns, você acertou! Vamos para a próxima...' + SemCor)
            elif user == 0:
                sleep(0.5)
                print(CorRoxo + 'VOLTANDO AO MENU PRINCIPAL...' + SemCor)
                sleep(1)
                break
            elif user != octal:
                print(CorVermelho + f'\nVocê errou, que pena! A resposta correta é {octal}' + SemCor + '.')
                print('Vamos tentar de novo...')
            else:
                print('Comando inválido! Vamos tentar novamente...')
            print('-' * 30)

    # HEXADECIMAL
    elif start == 3:
        while True:
            print('(Digite [0] para voltar ao menu principal.)')
            n = int(randint(0, 999))
            decimalParaHexa = hex(n)[2:]
            hexa = decimalParaHexa

            # RESULTADO HEXADECIMAL
            #print(hexa)

            user = input(f'\nQual é o valor HEXADECIMAL de {n}?  ').strip()

            if user == hexa:
                print(CorAzul + '\nParabéns, você acertou! Vamos para a próxima...' + SemCor)

            elif user in '0':
                sleep(0.5)
                print(CorRoxo + 'VOLTANDO AO MENU PRINCIPAL...' + SemCor)
                sleep(1)
                break

            elif user != hexa:
                print(CorVermelho + f'\nVocê errou, que pena! A resposta correta é {hexa}' + SemCor + '.')
                print('Vamos tentar de novo...')

            else:
                print('Comando inválido! Vamos tentar novamente...')
            print('-' * 30)

    # SAIR
    elif start == 0:
        break
    else:
        print('Comando inválido. Por favor digite novamente!')

sleep(0.5)
print('-' * 30)
print(CorRoxo + 'FIM DO PROGRAMA!' + SemCor)
sleep(0.5)
print('\nPor: Danilo de Lucio')
