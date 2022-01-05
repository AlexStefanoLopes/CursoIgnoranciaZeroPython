evento2 = [15, -15, 46, -12]

cargaatual = int(input('Digite a carga atual:'))
tempocarregado = int(input('Digite o tempo de carregamento:'))
tempojogando = int(input('Digite o tempo jogado:'))

bateria_carregando = cargaatual + tempocarregado
bateria_descarregando = bateria_carregando - tempojogando

if tempocarregado > 0:
	print('A bateria está com carga de:', bateria_descarregando, '%')
elif tempojogando > 0:
	print('A bateria está com carga de:', bateria_carregando, '%')
