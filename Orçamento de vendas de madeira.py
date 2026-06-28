print('Boas-vindas, Davi Wellington Ribeiro da Silva!')
print('[PIN] - Tora de Pinho --> R$ 150.40')
print('[PER] - Tora de Peroba --> R$ 170.20')
print('[MOG] - Tora de Mogno --> R$ 190.90')
print('[IPE] - Tora de Ipê --> R$ 210.10')
print('[IMB] - Tora de Imbuia --> R$ 200.70')

# Função para o Usuario escolher o tipo de madeira
def escolha_tipo ():
    while True:
        madeira = input('Qual tipo de madeira você deseja? ')
    
        if madeira == 'PIN':
            return 150.40
        elif madeira == 'PER':
            return 170.20
        elif madeira == 'MOG':
            return 190.90
        elif madeira == 'IPE':
            return 210.10
        elif madeira == 'IMB':
            return 200.70
        else:
            print('Tipo de madeira inválido. Tente novamente!')
        continue

# Recebe o tipo de madeira quê o Usuario escolheu
valor = escolha_tipo ()

# Função que calcula a quantidade e o desconto
def qtd_toras ():
    while True:
# esse trecho garante que o Usuario digite um numero valido (try/except)
        try:
            quantidade = int(input('Qual a quantidade de toras? '))
        except ValueError:
            print('Isso não é um número!')
            continue

        if quantidade < 100:
            desconto = 0
            return quantidade, desconto
        elif quantidade >= 100 and quantidade < 500:
            desconto = 0.04
            return quantidade, desconto
        elif quantidade >= 500 and quantidade < 1000:
            desconto = 0.09
            return quantidade, desconto
        elif quantidade >= 1000 and quantidade <= 2000:
            desconto = 0.16
            return quantidade, desconto
        else:
            print('Não é aceito essa quantidade de pedidos. Tente novamente!')
        continue

# Recebe os valores Quantidade e desconto            
quantidade, desconto = qtd_toras ()


print(' 1 --> Transporte Rodoviário - R$ 1000.00')
print(' 2 --> Transporte Ferroviário - R$ 2000.00')
print(' 3 --> Transporte Hidroviário - R$ 2500.00')

# Função que retorna o valor do transporte de acordo com a entrada do Usuario
def transporte ():
    while True:
        adTransporte = int(input('Qual tipo de transporte você deseja? '))

        if adTransporte == 1:
            return 1000
        elif adTransporte == 2:
            return 2000
        elif adTransporte == 3:
            return 2500
        else:
            print('Não existe essa opção digitada!')
transportar = transporte ()

# Calculo do valor total da compra considerando desconto e transporte
total = ((valor * quantidade)*(1- desconto)) + transportar
print(f'Total: {total}')

