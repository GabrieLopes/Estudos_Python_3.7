import array as arr
from abc import ABCMeta, abstractmethod
from operator import attrgetter
import numpy as np


# idade1 = 39
# idade2 = 29
# idade3 = 19
# idade4 = 9

# print(len(idades))
# idades.append(15)
# idades.remove(39)
# idades.clear()

# print(idades)
# print(15 in idades)

# if 15 in idades:
#     idades.remove(19)
#     print(19 in idades)


# for elemento in idades:
#     print("Recebi o elemento: ", elemento)

# for idade in idades:
#     print(idade + 1)

# idades_ano_que_vem = []
# for idade in idades:
#     idades_ano_que_vem.append(idade + 1)

# idades_ano_que_vem = [(idade+1) for idade in idades]
# idades_ano_que_vem = [(idade + 1) for idade in idades if idade > 21]
# print(idades_ano_que_vem)

# idades = [39, 29, 19, 9]
# idades.insert(0, 10)
# idades.extend([27, 16])
# print(idades)
#
#
# def proximo_ano(idade):
#     return idade + 1
#
#
# print([proximo_ano(idade) for idade in idades if idade > 21])


# def faz_processamento_de_visualizacao(lista):
#     print(len(lista))
#     lista.append(13)


# idades = [16, 21, 29, 56, 43]
# faz_processamento_de_visualizacao(idades)
# print(idades)


# def faz_processamento_de_visualizacao(lista = []):
#     print(len(lista))
#     print(lista)
#     lista.append(13)
# def faz_processamento_de_visualizacao(lista=None):
#     if lista is None:
#         lista = list()
#     print(len(lista))
#     print(lista)
#     lista.append(13)
#
#
# faz_processamento_de_visualizacao()
# faz_processamento_de_visualizacao()


# print(conta_do_gabriel)

# for conta in contas:
#     print(conta)
# conta_do_gabriel.deposita(100)
# class ContaCorrente():
#     def __init__(self, codigo):
#         self.codigo = codigo
#         self.saldo = 0
#
#     def deposita(self, valor):
#         self.saldo += valor
#
#     def __str__(self):
#         return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
#
#
# def deposita_para_todas(contas):
#     for conta in contas:
#         conta.deposita(100)
#
#
# conta_do_gabriel = ContaCorrente(15)
# conta_do_gabriel.deposita(500)
#
# conta_da_dani = ContaCorrente(47685)
# conta_da_dani.deposita(1000)
#
# contas = [conta_do_gabriel, conta_da_dani]

# print(contas[0], contas[1])
# deposita_para_todas(contas)
# print(contas[0], contas[1])

#
# gabriel = (15, 100)
# daniela = (75865, 1000)
#
#
# def depositar(conta):
#     novo_saldo = conta[1] + 100
#     codigo = conta[0]
#     return codigo, novo_saldo


# gabriel = depositar(gabriel)

# daniela = ("Daniela", 31, 1987)
# gabriel = ("Gabriel", 19, 2000)
#
# usuarios = [daniela, gabriel]
# usuarios.append(("Paulo", 39, 1979))
#
# print(usuarios)
# conta16 = ContaCorrente(16)
# conta16.deposita(1000)
#
# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)
#
# contas = [conta16, conta17]
#
# for conta in contas:
#     conta.passa_o_mes()
#     print(conta)


# arr.array('d', [1.0, 3.5])

# evitaremos usar array puro, se precisarmos de trabalho numérico, é costume usar o numpy
# numeros = np.array([1, 3.5])
# print(numeros + 3)

# print(list(range(len(idades))))
# print(list(enumerate(idades)))

# for indice, valor in enumerate(idades):
#     print(indice, "x" , valor)
# print(conta1 == conta2)
# print(conta1 in [conta2])
# print(conta2 in [conta1])

# print(isinstance(Conta(), Conta))
# print(isinstance(ContaCorrente(37), Conta))

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        return self._saldo < other._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {}  Saldo {}<<]".format(self._codigo, self._saldo)


# class ContaMultiploSalario(ContaSalario):
#
#
#
# conta1 = ContaSalario(37)
#
# conta2 = ContaMultiploSalario(37)
#
#
# idades = [9, 15, 20, 31, 35, 49, 56, 37]
#
# range(len(idades)) # lazy
#
# enumerate(idades) # lazy
#
#
#
# usuarios = [
#     ("Guilherme", 37, 1981),
#     ("Daniela", 31, 1987),
#     ("Paulo", 39, 1979)
# ]
#
# for nome, idade, nascimento in usuarios:
#     print(nome)
#
# print(list(reversed(idades)))
#
# print(sorted(idades, reverse=True))
#
# idades.sort()
# print(idades)


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_dani = ContaSalario(3)
conta_da_dani.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_dani, conta_do_paulo]


# def extrai_saldo(conta):
#     return conta._saldo


# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme > conta_da_dani)