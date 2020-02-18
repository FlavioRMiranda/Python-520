#Coletar inputs do usuario e armazenar em um dicionario

nome = input('Digite seu nome  ')
idade = input('Digite sua idade  ')
email = input('Digite seu email  ')

dicionario =  { 
                'nome' : nome,
                'idade' : idade,
                'email' : email
                }

print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['email'])

idade2 = int(dicionario['idade'])

if idade2 < 18:
	print('Idade menor que 18 anos')
else:
	print('Idedade maior que 18 anos')


