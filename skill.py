import random
from datetime import datetime

projetos = ['Site', 'controle_estoque', 'data_base']
time = []

lista_liguagem_programacao: tuple[str, str, str, str] = ('java', 'c++', 'python', 'html')
lista_projetos_envolvidos = []


class Empregado:
    numero_empregados: int

    def __init__(self, nome_completo: str, email: str, matricula_funcionario: str, salario: float):
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcionario = matricula_funcionario
        self.salario = salario

        print(f"{self.nome_completo} foi contratado pela empreza alsafe")

    def iniciar_jornada(self):
        print(f"O funcionario {self.nome_completo} metricula {self.matricula_funcionario}"
              f" inicializou a jornada de trabalho as {datetime.now()} ")

    def finalizar_jornada(self):
        print(f"O funcionario {self.nome_completo} metricula {self.matricula_funcionario}"
              f" finalizou a jornada de trabalho as {datetime.now()} ")

    def receber_aumento(self):
        raise NotImplementedError


class Desenvolvedor(Empregado):
    procentagem_aumento = 1.08

    def __init__(self, nome_completo, email, matricula_funcionario, salario):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcionario, salario)
        self.linguagem_programacao = ''
        self.litros_cafe = 0.0
        self.bournout = False

    def adicionar_linguagem(self):
        self.linguagem_programacao = random.choice(lista_liguagem_programacao)

    def beber_cafe(self):
        self.litros_cafe += 0.2
        if self.litros_cafe >= 2:
            self.bournout = True
            print(f"Funcionario {self.nome_completo} passou mal e foi para casa")
            Empregado.finalizar_jornada(self)

    def receber_aumento(self):
        self.salario = self.salario * Desenvolvedor.procentagem_aumento
        print(
            f'Parabéns {self.nome_completo} você recebeu aumento no salario, agora seu salario novo é '
            f'{self.salario:.2f}')


class GerenteProjeto(Empregado):
    pocentagem_aumento = 1.12

    def __init__(self, nome_completo: str, email: str,
                 matricula_funcional: str, salario: float,
                 time: list, projetos_envolvidos: list):
        # Chamada ao construtor da classe superior
        super().__init__(nome_completo, email, matricula_funcional, salario)

        # # Incrementa o número de empregados, definido na classe superior
        # super().numero_empregados += 1

        self.time = time
        self.projetos_envolvidos = projetos_envolvidos

    def adicionar_desenvolvedor(self, dev: Desenvolvedor):
        self.time.append(dev)
        print(f'O Dev {dev.nome_completo} matricula{dev.matricula_funcionario} foi adicionado ao time ')

    def remover_desenvolvedor(self, dev: Desenvolvedor):
        self.time.remove(dev)
        print(f'O Dev {dev.nome_completo} matricula{dev.matricula_funcionario} foi removido do time ')

    def participar_projeto(self):
        self.projetos_envolvidos.append(projetos)
        print(f'O Gerente {self.nome_completo} matricula{self.matricula_funcionario} foi está participando do projeto ')

    def sair_projeto(self):
        self.projetos_envolvidos.remove(projetos)
        print(f'O Gerente {self.nome_completo} matricula{self.matricula_funcionario} foi está saindo do projeto ')

    def receber_aumento(self):
        self.salario = self.salario * GerenteProjeto.pocentagem_aumento
        print(
            f'Parabéns {self.nome_completo} você recebeu aumento no'
            f' salario, agora seu salario novo é {self.salario:.2f}')


Thiago = Desenvolvedor("Thiago M.Montes", "thigo@gmail.com", "m3245", 2134.00)
Gustavo = GerenteProjeto('gustavo', 'gust@gmail', 'm21312', 3544.5, time, projetos)

GerenteProjeto.adicionar_desenvolvedor(Gustavo, Thiago)

GerenteProjeto.receber_aumento(Gustavo)
