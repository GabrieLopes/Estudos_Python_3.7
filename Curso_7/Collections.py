usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

len(assistiram)

set(assistiram)

set([1, 2, 3, 1])

{4, 1, 2, 3, 1}

type({1, 2})

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# usuarios_machine_learning
#
# usuarios_machine_learning[3]

# for usuario in set(assistiram):
#     print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# print(usuarios_data_science | usuarios_machine_learning)
#
# print(usuarios_data_science & usuarios_machine_learning)
#
# print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
# 15 in fez_ds_mas_nao_fez_ml
#
# 23 in fez_ds_mas_nao_fez_ml
#
# usuarios_data_science ^ usuarios_machine_learning

usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios)

usuarios.add(13)
len(usuarios)

usuarios.add(765)
len(usuarios)

# usuarios

usuarios = frozenset(usuarios)
# usuarios

type(usuarios)

# usuarios.add(134)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()

set(meu_texto.split())

"""# Dicionário (Mapa etc)"""

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

type(aparicoes)

# aparicoes["Guilherme"]
#
# aparicoes["cachorro"]
#
# aparicoes["xpto"]

aparicoes.get("xpto", 0)

aparicoes.get("cachorro", 0)

aparicoes = dict(Guilherme=2, cachorro=1)
# aparicoes

aparicoes = {"Guilherme": 1, "cachorro": 2, "nome": 2, "vindo": 1, "Carlos": 1}

# aparicoes

aparicoes["Carlos"] = 2

# aparicoes

del aparicoes["Carlos"]

# aparicoes
#
# "cachorro" in aparicoes
#
# "Carlos" in aparicoes
#
# for elemento in aparicoes:
#   print(elemento)
#
# for elemento in aparicoes.keys():
#   print(elemento)
#
# for elemento in aparicoes.values():
#   print(elemento)

# 1 in aparicoes.values()

# for elemento in aparicoes.keys():
#   valor = aparicoes[elemento]
#   print(elemento, valor)
#
# for elemento in aparicoes.items():
#   print(elemento)
#
# for chave, valor in aparicoes.items():
#   print(chave, "=", valor)

["palavra {}".format(chave) for chave in aparicoes.keys()]

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

# aparicoes

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

# aparicoes

int()

dicionario = defaultdict(int)
# dicionario['guilherme']

dicionario['guilherme'] = 15
# dicionario['guilherme']

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1


# aparicoes

class Conta:
    def __init__(self):
        pass


contas = defaultdict(Conta)
contas[15]

contas[17]

contas[15]

from collections import Counter

# aparicoes = Counter()
# for palavra in meu_texto.split():
#     aparicoes[palavra] += 1

# aparicoes

# aparicoes = Counter(meu_texto.split())

# aparicoes

texto1 = """ 
Em certas situações, queremos apenas algumas informações que estão nesse arquivo, porém, os dados costumam mudar frequentemente. Utilizando uma API conseguiremos ir direto ao ponto, evitando baixar arquivos desnecessários e economizando tempo.

E foi exatamente o que aconteceu durante essa semana, quando eu recebi uma tarefa para listar somente os repositórios do github de uma funcionária da empresa onde trabalho.
 """

texto2 = """ 
Maravilha! Alcançamos nosso objetivo. Não tinha ideia que fosse tão simples assim, não é?! Você pode encontrar o código completo aqui.

Esta é apenas uma das inúmeras funcionalidades da poderosa biblioteca de requests e você pode saber mais sobre ela acessando a documentação da mesma.

Gostou deste artigo e quer conhecer mais sobre os poderes da linguagem python? Que tal dar uma olhada em nossos cursos de Python aqui na Alura? Bons estudos e até o próximo artigo!

"""


def analisa_frequencia_de_letras(texto):
    # texto1.split()
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))

    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto2)
