class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @staticmethod
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'

restaurate_praca = Restaurante('Praca', 'Gourmet')
restaurate_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()