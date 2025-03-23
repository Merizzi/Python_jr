# Desafio a Parte:
# for i in range (0, 21, 2):
#     if i % 2  == 0 :
#             print ( i )
#     else:
#         break

# 1. Faça um programa que imprima "Estou aprendendo Python!" na tela. - Feito
#>> print("Estou aprendendo python!") 

# 2. Faça um programa que peça ao usuário para digitar um número e, em seguida, imprima na tela a mensagem "O número digitado foi <numero>"
# numero = int(input("Digite o seu número favorito:"))
# print(f"O seu número favorito é: {numero}")

# 3. Faça um programa que peça ao usuário para digitar seu nome e, em seguida, imprima na tela a mensagem "Olá, <nome>!"
# nome = input("Digite o seu nome:")
# print(f"Olá, {nome}, tudo bem com você?")

# 4. Faça um programa que realize a soma e subtração de duas variáveis, sendo uma do tipo inteiro e outra do tipo decimal, 
# exibindo o valor da soma e da subtração no seguinte formato: "O valor da soma é: <soma>" & "O valor da subtração é: <subtracao>".
# x = int(input("Digite o seu número inteiro:"))
# y = float(input("Digite o seu número decimal:"))
# soma = x + y
# sub = x - y
# print(f"O valor da soma é: {soma}"+ f"\nO valor da subtração é: {sub}")


# 5. Faça um programa que receba a idade do usuário e retorne a idade dele somada em 10 anos no seguinte formato: Sua idade daqui a 10 anos será: <idade + 10 anos>.
# idade = int(input("Digite sua idade:"))
# idadefut = idade + 10
# print(f"Sua idade é: {idade}"+ f"\nSua idade daqui 10 anos será: {idadefut}")

# 6. Faça um programa que leia algo digitado pelo usuário, mostre seu tipo e tudo a respeito dele (dica: utiliza as funções is).
# x = input ("Digite alguma coisa: ")
# print(f"O tipo de {x} é: {type(x)}" + f"\nÉ númerico? {x.isnumeric()}" + f"\nÉ Alfabético? {x.isalpha()}" + f"\nÉ alfanumérico? {x.isalnum()}")

# 7. Faça um programa receba algo digitado pelo usuário e verifique se ele digitou alguma coisa, retornando True caso tenha e False caso não tenha.
# x = input("Digite alguma coisa: ")
# print(bool(x)) -> nesse trecho ele está transformando a variavel em booleana para dizer se é true ou false para se tem algo digitado - true, se não - false; eu tinha 
# a ideia de realizar um if isnull porém não precisava de tantas voltas

# 8. Faça um programa que receba os seguintes dados de um funcionário: nome, idade e salario. Na empresa que esse funcionário trabalha, 
# seu salário é aumentado de ano em ano em R$ 800,90. Sabendo disso, imprima o nome, idade e salário do funcionário daqui a 1 ano no seguinte formato: "O funcionário <nome>, 
# daqui a 1 ano, terá <idade> anos, recebendo um salário igual a R$<salario>.
# nome = input("Digite o seu nome:")
# idade = int(input("Digite a sua idade: "))
# salario = float(input("Digite o seu salário atual:"))
# print(f"\nDaqui 1 ano, o funcionário {nome}"+ f"\nTerá {idade + 1} anos de idade e salário apróximado de R${salario + 800.90}")

# 9. Faça um programa que peça ao usuário para digitar dois números e mostre na tela o resultado da soma, subtração, multiplicação, divisão e resto da divisão desses números.
# numero = float(input("Digite o primeiro número:"))
# numero2 = float(input("Digite o segundo número:"))

# soma = numero + numero2
# sub = numero - numero2
# multi = numero * numero2
# div = numero / numero2
# resto = numero % numero2
# print(f"O resultado da soma desses números é: {soma}, \nO resultado da subtração desses números é: {sub} \nO resultado da multiplicação desses números é: {multi} \nO resultado da divisão desses números é: {div} \nO resultado do resto da divisão desses números é: {resto}")

# 10. Faça um programa que peça ao usuário o raio de um círculo e exiba na tela a área e o perímetro desse círculo (considere pi = 3.14). Aproxime para 2 casas decimais.
# r = float(input("Digite o valor do raio do seu círculo: "))
# d = r*2
# a = 3.14 * (r**2)
# p = d * 3.14
# print(f"A área desse círculo é: {a} e o perímetro desse círculo é: {p}")

# 11. Faça um programa que peça ao usuário o preço de um produto e exiba o preço com um desconto de 10%.
# produto = float(input("Digite o preço do seu produto:"))
# desconto = (produto*10) / 100
# produto_final = produto - desconto
# print(f"O valor do seu produto com desconto de 10% é: {produto_final:.2f}")

# 12. Faça um programa que leia a temperatura em graus Celsius e exiba a temperatura em graus Fahrenheit. 
# A fórmula para converter de Celsius para Fahrenheit é: F = (9/5)*C + 32.
# c = float (input("Digite os graus Celsius na sua cidade agora: "))
# fah = (9/5)*c + 32
# print(f"Sua cidade apresenta no momento {fah} graus Fahrenheit nesse momento")

# 13. Faça um programa que peça ao usuário para digitar 3 números inteiros e exiba a média aritmética desses números. Aproxime para 1 casa decimal.
# a1 = int(input("Digite o seu primeiro número inteiro: "))
# a2 = int(input("Digite o seu segundo número inteiro: "))
# a3 = int(input("Digite o seu terceiro número inteiro: "))
# media = (a1+a2+a3)/3
# print(f"A sua média ponderada é: {media:.1f}")

# 14. Faça um programa que leia o peso e a altura de uma pessoa e exiba o índice de massa corporal (IMC) dela. 
# A fórmula para calcular o IMC é: IMC = peso/altura², com aproximação em 3 casas decimais.
# peso = float (input("Digite o seu peso atual: "))
# altura = float (input("Digite a sua altura: "))
# imc = peso/(altura**2)

# print(f"O calculo do seu imc é: {imc:.3f}")

# 15. Faça um programa que leia dois números inteiros do usuário e troque seus valores, ou seja, 
# se o primeiro número for 5 e o segundo número for 7, o programa deve fazer com que o primeiro número seja igual a 7 e o segundo número seja igual a 5.
# a1 = int(input("Digite o seu primeiro número inteiro: "))
# a2 = int(input("Digite o seu segundo número inteiro: "))
# x = a1
# a1 = a2
# a2 = x 

# print(f"O seu primeiro número foi invertido com o segundo então ele ficou: {a1}, e o seu segundo número ficou como: {a2}")

# 16. Escreva um programa Python que leia um número inteiro e verifique se ele é par ou ímpar.
# a1 = int(input("Digite o seu número inteiro: "))
# resto = a1 % 2

# if resto == 1:
#   print("O seu número é ímpar")
# else:
#   print("O seu número é par")

# 17. Escreva um programa Python que leia um número e retorne seu quadrado, sua raíz quadrada e sua raíz cúbica, com aproximação em 2 casas decimais.
# numero = float(input("Digite o seu número: "))
# quadrado = numero ** 2
# raizquadrada = numero ** (1/2)
# raizcubica = numero ** (1/3)

# print(f"O quadrado do seu número é: {quadrado:.2f}. \nA raiz quadrada do número é: {raizquadrada:.2f}. \nA raiz cubica do número é: {raizcubica:.2f}. ")

# 18. Escreva um programa Python que leia o valor de dois catetos e retorne o valor da hipotenusa, assumindo que seja possível formar um triângulo.
# a1 = float(input("Digite o número do seu primeiro cateto: "))
# a2 = float(input("Digite o número do seu segundo cateto: "))
# hipo = (a1 ** 2 + a2 ** 2) ** 0.5

# print(f"O valor da sua hipotenusa é: {hipo}. ")