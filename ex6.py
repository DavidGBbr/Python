lista = [1, 3, 2, 5]
i = 0
maior = lista[0]
while i < len(lista):
  if lista[i] > maior:
    maior = lista[i]
  i += 1

print("O maior número da lista é: " + str(maior))


user_word = input("Escreva uma string: ")
letters = {}

for letter in user_word:
  if(letter in letters):
    letters[letter] += 1
  else:
    letters[letter] = 1

print(letters)


def inverte_lista(lista):
  lista_invertida = []
  i = 0
  while i < len(lista):
    lista_invertida.append( lista[len(lista) - i - 1])
    i += 1

  return lista_invertida

lista2 = ["a", 5, {1}]
lista_invertida = inverte_lista(lista2)
print(lista_invertida)