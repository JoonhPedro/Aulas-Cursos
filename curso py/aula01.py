print('calculos operacional soma subtracao multiplicacao divisao')
#forma estatica
#a = 5 
#b = 15
#c = 4
#forma de interagir com o usuario 
a = int(input('digite um valor:'))
b = int(input('digite um segundo valor: '))
c = int(input('digite um terceiro valor: '))
print(type (a))
print(type (b))
print(type (c))
soma = a + b + c
subtracao = a - b - c
multiplicacao = a * b * c
divisao = a / b + c 
resto = a % b % c
# esse str tranforma para string 'nao se torna uma boa prática'
#print('soma = ' + str(soma))
#print('soma = {}' .format(soma))
#print('subtracao = {}' .format(subtracao))
#print('multiplicacao = {}'.format(multiplicacao))
#print('divisao = {}' .format (divisao))
#print('resto = {}' .format (resto))
#tambem posso deixa o codigo mais simplificado da maneira a seguir
resultados ='soma:  {soma} \nsubtracao:  {subtracao}  \nmultiplicacao:  {multiplicacao} \ndivisao:  {divisao}  \nresto: {resto}'.format(soma=soma,
         subtracao=subtracao,
         multiplicacao=multiplicacao,
         divisao=divisao,
         resto=resto,)
print(resultados)