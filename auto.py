import random

valor_pedagio_carro = 4.5
valor_pedagio_moto = 2.3
km_rodados_carro = 1.5
km_rodados_moto = 1
valor_gasolina = 5.8

lista_carro = []
lista_moto = []


class Automovel:
    numero_total_locacoes = 0

    def __init__(self, montadora, modelo, alugado, consumo):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.consumo = consumo
        self.valor_fatura = 0
        self.nome_cliente = ""
        self.consumo_automovel = 0
        print(f' O automovel {self.montadora} {self.modelo} foi adqueriado pela locadora')

    def alugar(self, nome_cliente):
        Automovel.numero_total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O aultomovel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente} !')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O automovel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente} !')

    def gerar_valor_fatura(self, numero_pedagio, km_rodados):
        raise NotImplementedError


class Car(Automovel):
    number_total_location_car = 0
    valur_total_location = 0.0

    def __init__(self, montadora, modelo, alugado, consumo):
        super(Car, self).__init__(montadora, modelo, alugado, consumo)
        print('the Automotive add it is one Car')

    def alugar(self, nome_cliente):
        super(Car, self).alugar(nome_cliente)
        Car.number_total_location_car += 1

    def gerar_valor_fatura(self, numero_pedagio, km_rodados):
        self.consumo_automovel = km_rodados / self.consumo
        self.valor_fatura = \
            numero_pedagio * valor_pedagio_carro + km_rodados * km_rodados_carro + valor_gasolina * self.consumo_automovel

        print(f'O valor da fatura do Carro {self.montadora} {self.modelo}'
              f' é de R$ {self.valor_fatura:.2f} foram rodados {km_rodados}Km e gastos {self.consumo_automovel:.1f}L'
              f' de Gasolina e passou em {numero_pedagio} Pedagios')
        Car.valur_total_location += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.number_total_location_car != 0:
            media_locacoes = cls.valur_total_location / cls.number_total_location_car
            print(f'O Valor medio de locações de carro estão em R${media_locacoes}')

        else:
            print('O número total de locações é igual a zero')


class Moto(Automovel):
    numero_total_locacoes_moto = 0
    valor_total_locacoes = 0.0

    def __int__(self, montadora, modelo, alugado, consumo):
        super(Moto, self).__init__(montadora, modelo, alugado, consumo)
        print(' O automovel adquirido foi uma Moto')

    def alugar(self, nome_cliente):
        super(Moto, self).alugar(nome_cliente)
        Moto.numero_total_locacoes_moto += 1

    def gerar_valor_fatura(self, numero_pedagio, km_rodados):
        self.valor_fatura = numero_pedagio * valor_pedagio_moto + km_rodados * km_rodados_moto
        print(f'O valor da fatura da Moto {self.montadora} {self.modelo}'
              f' é de R$ {self.valor_fatura:.2f}')
        Moto.valor_total_locacoes += self.valor_fatura

    @classmethod
    def calcular_media_locacoes(cls):
        if cls.numero_total_locacoes_moto != 0:
            media_locacoes = cls.valor_total_locacoes / cls.numero_total_locacoes_moto
            print(f'O Valor medio de locações de moto estão em R${media_locacoes}')

        else:
            print('O número total de locações é igual a zero')


def mostrar_fatura(Automovel):
    print(
        f'O valor da fatura do Automóvel {Automovel.montadora} {Automovel.modelo} alugado por {Automovel.nome_cliente} '
        f'ficou no valor de R${Automovel.valor_fatura:.2f}')


# ******************************************************

print('inclua os dados do veiculo:')

fiesta = Car(input('Montadora: '), input("Modelo: "), False, random.randint(int(input('Consumo cidade Km/L: ')),
                                                                            int(input('consumo rodovia Km/L: '))))
fiesta.alugar("João")
fiesta.devolver_automovel()

fiesta.gerar_valor_fatura(km_rodados=random.randint(500, 1000), numero_pedagio=random.randint(3, 10))

mostrar_fatura(fiesta)
