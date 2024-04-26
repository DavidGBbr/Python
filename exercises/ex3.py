#number = input("Insira um número inteiro: ")
#is_even = int(number) % 2 == 0
#print("O número é par: " + str(is_even))

a = 5
b = 10
x = True
y = False
print((x or y) and (a < b)) #True
print((x or y) and not (a < b)) #False

resultado_1 = 2 + 3 * 2 ** 2
print(resultado_1)

resultado_2 = 2 + (3 * 2) ** 2
print(resultado_2)

resultado_3 = ((2 + 3) * 2) ** 2
print(resultado_3)

valor_de_compra = float(input("Valor de compra: "))
valor_do_frete = float(input("Valor do frete: "))
cliente_fiel = input("Cliente participa do programa de fidelidade (s) ou (n): ")

desconto = (valor_de_compra + valor_do_frete > 100) or (cliente_fiel == "s")

print("Cliente pode aplicar cupom de desconto: " + str(desconto))