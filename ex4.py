number = int(input("Digite um número inteiro: "))

if number % 3 == 0 and number % 5 == 0: 
  print("FizzBuzz")
elif number % 3 == 0:
  print("Fizz")
elif number % 5 == 0:
  print("Buzz")
else:
  print("Número não múltiplo de 3 ou 5")


operando1 = float(input("Digite o 1º operando:"))
operando2 = float(input("Digite o 2º operando:"))
operador = int(input("Escolha (1-soma ou 2-subtração):"))

if operador == 1:
  print("O resultado da soma é: " + str(operando1 + operando2))
elif operador == 2:
  print("O resultado da subtração: " + str(operando1 - operando2))
else:
  print("Operador inválido")


USUARIO = "admin"
SENHA = "123123"

nome_usuario = input("Digite o nome do usuário: \n")
senha_usuario = input("Digite a senha do usuário: \n")

if nome_usuario == USUARIO and senha_usuario == SENHA:
  print("Autenticação foi bem-sucedida.")
elif nome_usuario != USUARIO:
  print("Nome de usuário inexistente.")
elif senha_usuario != SENHA:
  print("Senha incorreta.")


n = int(input("Digite um número inteiro: "))
sum = 0
count = 1

while n >= count:
  sum += count
  count += 1

print("A soma total foi: " + str(sum))


while n >= count:
  if count % 2 == 0:
    print(count)
  count += 1


dividers = []
while n >= count:
  if n % count == 0:
    dividers.append(count)
  count += 1

if len(dividers) == 2 and n > 1:
  print("O número " + str(n) + " é um primo")
else:
  print("O número " + str(n) + " não é um primo")


chances = 3
target_number = 5

while chances >= 0:
  
  if chances == 0:
    print("Você perdeu!")
    break

  guess = int(input("Acerte o número sorteado: "))

  if guess == target_number:
    print("Parabéns, você acertou!")
    break

  chances -= 1

  