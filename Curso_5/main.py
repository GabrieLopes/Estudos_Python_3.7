from Estudos_Python_3.Curso_5.ExtratorArgumentosUrl import ExtratorArgumentosUrl
# argumento = "www.bytebank.com/cambio?moedaorigem=real"
# subString = argumento[5:11]
# print(subString)

# argumento = "moedaorigem=real"
# index = argumento.find("=")
# subString = argumento[index + 1:]
# print(subString)

# argumento = "moedaorigem=real"
# index = argumento.split("=")
# print(index)


url = "moedaorigem=real&moedadestino=dolar"

argumentosUrl = ExtratorArgumentosUrl(url)

moeda_origem, moeda_destino = argumentosUrl.extrair_argumentos()
print(moeda_destino, moeda_origem)


