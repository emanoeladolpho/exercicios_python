class Empregado:
  def __init__(self,matricula,nome,salarioFixo):
    self.matricula = matricula 
    self.nome = nome
    self.salarioFixo = salarioFixo



  def calcularSalario(self):
    return self.salarioFixo




class Vendedor(Empregado):
  def __init__(self,matricula,nome,salarioFixo,vendasTotal,comissao)  :
    Empregado.__init__(self,matricula,nome,salarioFixo)
    self.vendasTotal = vendasTotal
    self.comissao = comissao


  def calcularSalario(self):
    return self.salarioFixo + (self.vendasTotal*self.comissao/100)




class Gerente(Empregado):
  def __init__(self,matricula,nome,salarioFixo,numeroSubordinados):
    Empregado.__init__(self,matricula,nome,salarioFixo)
    self.numeroSubordinados = numeroSubordinados


  def calcularSalario(self):
    return self.salarioFixo + 1000




class GerenteVendas(Vendedor,Gerente):
  def __init__(self,matricula,nome,salarioFixo,vendasTotal,comissao,numeroSubordinados):
    Vendedor.__init__(self,matricula,nome,salarioFixo,vendasTotal,comissao)
    Gerente.__init__(self,matricula,nome,salarioFixo,numeroSubordinados)

  
  def calcularSalario(self):
    return self.salarioFixo + (self.vendasTotal*self.comissao/100) + 1000






v = Vendedor(123,"Antonio",1000,2500,10)
g = Gerente(123,"Raimundo",1500,10)
gv = GerenteVendas(123,"Jose",2000,5000,10,4)
print("-----------VENDEDOR---------------")
print("Matricula: ",v.matricula)
print("Nome: ",v.nome)
print("Salario Fixo: ",v.salarioFixo)
print("Vendas Total: ",v.vendasTotal)
print("Comissao: ",v.comissao)
print("salario: ",v.calcularSalario())
print("-----------GERENTE---------------")
print("Matricula: ",g.matricula)
print("Nome : ",g.nome)
print("Salario Fixo: ",g.salarioFixo)
print("Numero de subordinados: ",g.numeroSubordinados)
print("Salario: ",g.calcularSalario())
print("-----------GERENTE DE VENDAS---------------")
print("Matricula: ",gv.matricula)
print("Nome: ",gv.nome)
print("Salario Fixo: ",gv.salarioFixo)
print("Vendas Total: ",gv.vendasTotal)
print("Comissao: ",gv.comissao)
print("Numero de subordinados: ",gv.numeroSubordinados)
print("Salário: ",gv.calcularSalario())
