# ALGORITMO CONTROLE REMOTO

class ControleRemoto:
  def __init__(self,canal,volume,estado,mudo):
    self.__canal = canal
    self.__volume = volume
    self.__estado = estado
    self.__mudo = mudo

  # GETTERS AND SETTERS

  def getCanal(self):
    return self.__canal

  def setCanal(self,canal):
    self.__canal = canal

  def getVolume(self):
    return self.__volume

  def setVolume(self,volume):
    self.__volume = volume

  def getEstado(self):
    return self.__estado

  def setEstado(self,estado):
    self.__estado = estado

  def getMudo(self):
    return self.__mudo

  def setMudo(self,mudo):
    self.__mudo = mudo


  #METHODS

  def aumentarVolume(self):
    if(self.getEstado() == False or self.getMudo() == True):
      return "Impossivel aumentar o volume"
    else:
      self.setVolume(self.getVolume() + 5)
      return "Volume: " ,self.getVolume()

  def diminuirVolume(self):
    if(self.getEstado() == False or self.getMudo() == True):
      return "Impossivel dimuir o volume!"
    else:
      self.setVolume(self.getVolume() - 5)
      return "Volume: ",self.getVolume()

  def trocarCanalCima(self):
    if(self.getEstado() == True):
      self.setCanal(self.getCanal() + 1)
      return "Canal: ",self.getCanal()
    else:
      return "Impossivel trocar canal"

  def trocarCanalBaixo(self):
    if(self.getEstado() == True):
      self.setCanal(self.getCanal() - 1)
      return "Canal: ",self.getCanal()
    else:
      return "Impossivel trocar canal"

  def ligar_desligar(self):
    if(self.getEstado() == True):
      self.setEstado(False)
      return "Desligando"
    else:
      self.setEstado(True)
      return "Ligando"

  
  def mutar_desmutar(self):
    if(self.getMudo() == False):
      self.setMudo(True)
      return "Televisao esta no mudo"
    else:
      self.setMudo(False)
      return "O som da TV esta ativado!"


  def trocarCanalManual(self,num_canal):
    if(num_canal>99):
      return "Canal indisponivel!"
    else:
      self.setCanal(num_canal)
      return "Canal: ",self.getCanal()



controle = ControleRemoto(5,50,False,False)

print(controle.aumentarVolume())
print(controle.ligar_desligar())
print(controle.aumentarVolume())
print(controle.aumentarVolume())
print(controle.diminuirVolume())
print(controle.trocarCanalCima())
print(controle.trocarCanalCima())
print(controle.trocarCanalBaixo())
print(controle.ligar_desligar())
print(controle.trocarCanalCima())
print(controle.ligar_desligar())
print(controle.trocarCanalBaixo())
print(controle.mutar_desmutar())
print(controle.aumentarVolume())
print(controle.mutar_desmutar())
print(controle.aumentarVolume())
print(controle.diminuirVolume())
print(controle.mutar_desmutar())
print(controle.aumentarVolume())
print(controle.mutar_desmutar())
print(controle.trocarCanalCima())
print(controle.mutar_desmutar())
print(controle.trocarCanalCima())
print(controle.trocarCanalManual(38))
print(controle.trocarCanalManual(150))
print(controle.trocarCanalManual(73))