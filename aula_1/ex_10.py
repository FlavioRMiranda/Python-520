lista = [1,2,3,4,5,6]
def mapa(numero):
	if numero % 2 == 0:
		return numero * 2
	return numero * 3

def meu_mapa(lista):
	return list(map(mapa, lista))

minha_lista = meu_mapa(lista)

print(minha_lista)
