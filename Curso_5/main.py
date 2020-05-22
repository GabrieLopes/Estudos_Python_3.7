from Estudos_Python_3.Curso_5.ExtratorArgumentosUrl import ExtratorArgumentosUrl

# # argumento = "www.bytebank.com/cambio?moedaorigem=real"
# # subString = argumento[5:11]
# # print(subString)
#
# # argumento = "moedaorigem=real"
# # index = argumento.find("=")
# # subString = argumento[index + 1:]
# # print(subString)
#
# # argumento = "moedaorigem=real"
# # index = argumento.split("=")
# # print(index)
#
# #
#
# #
# # argumentosUrl = ExtratorArgumentosUrl(url)
# #
# # moeda_origem, moeda_destino = argumentosUrl.extrair_argumentos()
# # print(moeda_destino, moeda_origem)
# url = "moedaorigem=real&moedadestino=dolar"

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moeda_origem, moeda_destino, valor)

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moeda_origem, moeda_destino, valor)