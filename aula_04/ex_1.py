

lista_1 = [1,2,3,4,5,6]

#def maior_entre_dois_numeros(a, b):#
#	if a > b:
#        	return a
#        return b


def  maior_num_com_lambda(a,b):
	return list(map(lambda a,b: a > b,lista_1)

lista_2 =  maior_num_com_lambda(lista_1)

print(lista_2)
