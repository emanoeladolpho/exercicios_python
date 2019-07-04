#-------------------------COMPOSIÇÃO------------------------------
'''
class Salario:
  def __init__(self,salario,bonus):
    self.salario = salario
    self.bonus = bonus


  def salarioAnual(self):
    return (self.salario*12) + self.bonus





class Funcionario:
  def __init__(self,nome,idade,salario,bonus):
    self.nome = nome
    self.iade = idade
    self.obj_salarioAnual = Salario(salario,bonus)


  def salariofinal(self):
    return self.obj_salarioAnual.salarioAnual()




joao = Funcionario("Joao",35,2000,700)

print(joao.salariofinal())
'''



#-------------------------AGREGAÇÃO------------------------------
'''
class Salario:
  def __init__(self,salario,bonus):
    self.salario = salario
    self.bonus = bonus


  def salarioAnual(self):
    return (self.salario*12) + self.bonus


sal1 = Salario(2000,700)

class Funcionario:
  def __init__(self,nome,idade,salario):
    self.nome = nome
    self.idade = idade
    self.obj_salario = salario


  def salarioFinal(self):
    return self.obj_salario.salarioAnual()



joao = Funcionario("Joao",35,sal1)
print(joao.salarioFinal())
'''