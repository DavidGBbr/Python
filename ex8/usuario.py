class Usuario:
  quantidade_instancias = 0
  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    Usuario.quantidade_instancias += 1
  
  def imprime_usuario(self):
    print(f"{self.nome} ({self.email})")

