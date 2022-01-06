import bradesco = Conta(456, 1000)

class Conta:
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        return 'ID: %iSaldo: R$ %.2f'%(self.ID, self.saldo)

print(bradesco)