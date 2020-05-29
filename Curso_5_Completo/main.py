from Estudos_Python_3.Curso_5_Completo.ExtratorArgumentosUrl import ExtratorArgumentosUrl

# argumento = "www.bytebank.com/cambio?moedaorigem=real"
# subString = argumento[5:11]
# print(subString)
#
# argumento = "moedaorigem=real"
# index = argumento.find("=")
# subString = argumento[index + 1:]
# print(subString)
#
# argumento = "moedaorigem=real"
# index = argumento.split("=")
# print(index)
#
# moeda_origem, moeda_destino = argumentosUrl.extrair_argumentos()
# print(moeda_destino, moeda_origem)
# url = "moedaorigem=real&moedadestino=dolar"

# cambio = ExtratorArgumentosUrl(url)
# moeda_origem, moeda_destino = cambio.retorna_moedas()
# valor = cambio.retorna_valor()
# print(moeda_origem, moeda_destino, valor)
#
# url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
# cambio = ExtratorArgumentosUrl(url)
# moeda_origem, moeda_destino = cambio.retorna_moedas()
# valor = cambio.retorna_valor()
# print(moeda_origem, moeda_destino, valor)

url1 = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
url2 = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=500"
argumentosUrl1 = ExtratorArgumentosUrl(url1)
argumentosUrl2 = ExtratorArgumentosUrl(url2)
print(id(argumentosUrl1))
print(id(argumentosUrl2))
print(argumentosUrl1 == argumentosUrl2)
