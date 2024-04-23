def e_primo(n):
  dividers = []
  i = 1
  while i <= n:
    if n % i == 0:
      dividers.append(i)
    i += 1
  return len(dividers) == 2 and n > 1

print(e_primo(1))
print(e_primo(2))


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
def lista_para_tupla(lista):
  tupla = ()
  count = 0

  while count <= (len(lista) - 1):
    tupla = (count, lista[count])
    count += 1

  return tupla

print(lista_para_tupla(numeros))


def maior_idade(pessoa):
  if type(pessoa) is tuple:
    if pessoa[1] >= 18:
      print(pessoa[0] + " é maior de idade.")
    else:
      print(pessoa[0] + " não é maior de idade.")

  if type(pessoa) is dict:
    if pessoa["idade"] >= 18:
      print(pessoa["nome"] + " é maior de idade.")
    else:
      print(pessoa["nome"] + " não é maior de idade.")

pessoa = ("Martina", 18)
pessoa2 = {"nome":"Jéssica","idade": 16}

maior_idade(pessoa)
maior_idade(pessoa2)


def lista_tem_elemento(lista, elemento):
  for item in lista:
    if item == elemento:
      return True
  return False

print(lista_tem_elemento([1, 2, 3, 4, 5], 3))
print(lista_tem_elemento([1, 2, 3, 4, 5], 6))


def fatorial(n):
  if n == 0 or n == 1:
    return 1
  else: 
    resultado = 1
    while n > 1:
      resultado = resultado * n
      n -= 1
    return resultado

print(fatorial(3))