number_list = []

while True:
  number = int(input("Digite um número inteiro: "))
  if number < 0:
    break
  number_list.append(number)

for number in number_list:
  print(number)


lista = [1, 10, 20, 35, 22, 12]
count = 0
total = 0

while count < len(lista):
  total += lista[count]
  count += 1

print(total)


average = sum(lista)//len(lista)
print(average)


alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

total_nota = 0

for aluno in alunos:
  total_nota += aluno[1]

print("A média dos alunos é:",str(total_nota / len(alunos)))


alunos2 = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

total_nota2 = 0

for aluno in alunos2:
  total_nota2 += int(aluno['nota'])

print("A média dos alunos é:",str(total_nota2 / len(alunos2)))