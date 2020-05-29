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

daniela = ("Daniela", 31, 1987)
gabriel = ("Gabriel", 19, 2000)

usuarios = [daniela, gabriel]
usuarios.append(("Paulo", 39, 1979))

print(usuarios)
