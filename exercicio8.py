# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self.titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self.titular.ljust(25)} | {str(self.valor).ljust(15)} | {self.ativo}'

    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return '■' if self._ativo else '□'

    @property
    def valor(self):
        return f'R${self._saldo:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.')

conta1 = ContaBancaria('Matheus Henrique Machado', 5000)
conta2 = ContaBancaria('Patricia Carvalho Santos', 10000)

print(conta1, conta2, sep='\n')
conta2.ativar_conta()
print(conta1, conta2, sep='\n')