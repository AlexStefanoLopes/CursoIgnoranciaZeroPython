base = int(input('Digite o numero base:'))
expoente = int(input('Digite o expoenteç:'))

cont = 0
produto = 1
while cont < expoente:
    produto = produto*base
    cont = cont + 1

print(produto)