class Empregado:
  def __init__(self,matricula,nome,salarioFixo):
    self._matricula = matricula
    self._nome = nome
    self._salarioFixo = salarioFixo

  
  # GETTERS AND SETTER

  def getMatricula(self):
    return self._matricula

  def setMatricula(self,matricula):
    self._matricula = matricula

  def getNome(self):
    return self._nome

  def setNome(self,nome):
    self._nome = nome

  def getSalarioFixo(self):
    return self._salarioFixo

  def setSalarioFixo(self,salarioFixo):
    self._salarioFixo = salarioFixo


  # METHODS

  def calcularSalario(self):
    return self._salarioFixo



class Vendedor(Empregado):
  def __init__(self,matricula,nome,salarioFixo,vendasTotal,comissao):
    Empregado.__init__(self,matricula,nome,salarioFixo)
    self._vendasTotal = vendasTotal
    self._comissao = comissao

  # GETTERS AND SETTER

  def getVendasTotal(self):
    return self._vendasTotal

  def setVendasTotal(self,vendasTotal):
    self._vendasTotal = vendasTotal


  def getComissao(self):
    return self._comissao

  def setComissao(self,comissao):
    self._comissao = comissao


  # METHODS
  

  def calcularSalario(self):
    return self._salarioFixo + (self._vendasTotal*self._comissao/100)




class Gerente(Empregado):
  def __init__(self,matricula,nome,salarioFixo,numeroSubordinados):
    Empregado.__init__(self,matricula,nome,salarioFixo)
    self._numeroSubordinados = numeroSubordinados


  # GETTERS AND SETTERS

  def getNumeroSubordinados(self):
    return self._numeroSubordinados

  def setNumeroSubordinados(self,numeroSubordinados):
    self._numeroSubordinados = numeroSubordinados

  
  # METHODS

  def calcularSalario(self):
    return self._salarioFixo + 1000




class GerenteVendas(Vendedor,Gerente):
  def __init__(self,matricula,nome,salarioFixo,vendasTotal,comissao,numeroSubordinados):
    Vendedor.__init__(self,matricula,nome,salarioFixo,vendasTotal,comissao)
    Gerente.__init__(self,matricula,nome,salarioFixo,numeroSubordinados)


  def calcularSalario(self):
    return self._salarioFixo + (self._vendasTotal*self._comissao/100) + 1000







v1 = Vendedor(234,"Antonio",1500,3000,5)
g1 = Gerente(456,"Raimundo",2500,10)
gv = GerenteVendas(123,"Joao",2000,5000,10,15)




print("--------VENDEDOR-----------")
print(v1.getMatricula())
print(v1.getNome())
print(v1.getSalarioFixo())
print(v1.calcularSalario())
print("--------GERENTE-----------")
print(g1.getMatricula())
print(g1.getNome())
print(g1.getSalarioFixo())
print(g1.calcularSalario())
print("-------GERENTE DE VENDAS------")
print(gv.getMatricula())
print(gv.getNome())
print(gv.getSalarioFixo())
print(gv.getVendasTotal())
print(gv.getComissao())
print(gv.calcularSalario())

v1.setMatricula(987)
v1.setNome("Alexandre")
v1.setSalarioFixo(1800)

g1.setMatricula(579)
g1.setNome("Gustavo")
g1.setSalarioFixo(2750)
g1.setNumeroSubordinados(25)


gv.setMatricula(643)
gv.setNome("Kleberson")
gv.setSalarioFixo(5000)
gv.setVendasTotal(8000)
gv.setComissao(15)
gv.setNumeroSubordinados(30)
print("")
print("APÓS ATUALIZAR TODOS OS ATRIBUTOS")
print("--------VENDEDOR-----------")
print(v1.getMatricula())
print(v1.getNome())
print(v1.getSalarioFixo())
print(v1.calcularSalario())
print("--------GERENTE-----------")
print(g1.getMatricula())
print(g1.getNome())
print(g1.getSalarioFixo())
print(g1.calcularSalario())
print("-------GERENTE DE VENDAS------")
print(gv.getMatricula())
print(gv.getNome())
print(gv.getSalarioFixo())
print(gv.getVendasTotal())
print(gv.getComissao())
print(gv.calcularSalario())
