class Tamagotchi:
  def __init__(self,nome,fome,sono,tedio,estado_sono):
    self.__nome = nome
    self.__fome = fome
    self.__sono = sono
    self.__tedio = tedio
    self.__estado_sono = estado_sono


  def getNome(self):
    return self.__nome

  def setNome(self,nome):
    self.__nome = nome

  def getFome(self):
    return self.__fome

  def setFome(self,fome):
    self.__fome = fome

  def getSono(self):
    return self.__sono

  def setSono(self,sono):
    self.__sono = sono

  def getTedio(self):
    return self.__tedio

  def setTedio(self,tedio):
    self.__tedio = tedio

  def getEstadoSono(self):
    return self.__estado_sono
  
  def setEstadoSono(self,estado_sono):
    self.__estado_sono = estado_sono




  def alimentar(self):
    if(self.getFome() <= 0):
      return "O",self.getNome()," nao esta com fome"
    elif((self.getFome() - 15) < 0):
      self.setFome(0)
      return "O ",self.getNome()," foi totalmente alimentado"
    else:
      self.setFome(self.getFome() - 15)
      return "Indice de fome: ",self.getFome()



  def dormir_acordar(self):
    if(self.getEstadoSono() == True and self.getSono() > 50):
      self.setEstadoSono(False)
      self.setSono(0)
      return "Dormindo"
    elif(self.getEstadoSono() == True and self.getSono() <= 50):
      return "O ",self.getNome()," nao esta com sono"
    else:
      self.setEstadoSono(True)
      return "Acordando..."



  def brincar(self):
    if(self.getTedio() <= 0 and self.getEstadoSono() == True):
      return "O ",self.getNome()," nao quer brincar"
    elif((self.getTedio() - 15 < 0) and self.getEstadoSono() == True):
      self.setTedio(0)
      return "O ",self.getNome()," ja brincou o bastante"
    elif(self.getEstadoSono() == False):
      return "O",self.getNome()," nao pode brincar"
    else:
      self.setTedio(self.getTedio() - 15)
      return "Indice de tedio: ",self.getTedio()
        



t1 = Tamagotchi("Joao",50,50,50,True)


print(t1.getFome())
print(t1.alimentar())
print(t1.alimentar())
print(t1.alimentar())
print(t1.alimentar())
print(t1.alimentar())
print(t1.alimentar())
print("------------------------")
print("")

print(t1.dormir_acordar())
t1.setSono(60)
print(t1.dormir_acordar())
print(t1.getSono())
print(t1.dormir_acordar())
print("----------------------------")
print("")

print(t1.getTedio())
print(t1.brincar())
print(t1.brincar())
print(t1.brincar())
print(t1.brincar())
print(t1.brincar())
print(t1.brincar())
t1.setEstadoSono(False)
print(t1.brincar())