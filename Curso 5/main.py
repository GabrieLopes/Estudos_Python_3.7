# argumento = "www.bytebank.com/cambio?moedaorigem=real"
# subString = argumento[5:11]
# print(subString)

# argumento = "moedaorigem=real"
# index = argumento.find("=")
# subString = argumento[index + 1:]
# print(subString)

argumento = "moedaorigem=real"
index = argumento.split("=")
print(index)
