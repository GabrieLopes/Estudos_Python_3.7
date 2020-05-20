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


url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

print(ExtratorArgumentosUrl.ExtratorArgumentosUrl(url))
