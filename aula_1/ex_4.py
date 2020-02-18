#Validar se o usuario e elegivel pela idade

idade = input("Digite sua idade?: ")

if int(idade) > 18:
	print("Voce  pode jogar")
else:
	print("Voce nao pode jogar")
