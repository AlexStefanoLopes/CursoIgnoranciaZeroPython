def find(frase, sub):
    for i in range(len(frase, sub) + 1 - len(sub)):
        if frase[i:i+ len(sub)] == sub:
            return True

        return False

    print(find('mississippi', 'ss'))

def find(frase, sub):
    for i in range(len(frase, sub) + 1 - len(sub)):
        if frase[i:i + len(sub)] == sub:
            return True

        return 'ERRO'

    print(find('mississippi', 'a'))

    id(find)
    print(id)