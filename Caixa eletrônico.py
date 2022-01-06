saque = int(input('Digite a quantia que deseja saca:'))

if 10<= saque <= 600:
    notas_cem = saque //100
    saque = saque % 100

    notas_cinquenta = saque //50
    saque = saque % 50

    notas_dez = saque //10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_um = saque // 1
    saque = saque % 1

    if notas_cem >0:
        print(notas_cem, 'notas de R$ 100')
    if notas_cinquenta > 0:
        print(notas_cinquenta, 'notas de R$ 50')
    if notas_dez > 0:
        print(notas_dez, 'notas de R$ 10')
    if notas_cinco > 0:
        print(notas_cinco, 'notas de R$ 5')
    if notas_um > 0:
        print(notas_um, 'notas de R$ 1')
else:
    print('Não foi possível sacar')
