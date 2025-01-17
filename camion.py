from veicolo import Veicolo

class Camion(Veicolo):
    def __init__(self, targa, maxKg, traspKg, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxKg = maxKg
        if traspKg > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = traspKg
        
    def __str__(self):
        return "Camion:" + str(self.__dict__)
    
    @property
    def maxKg(self):
        return self.__maxKg

    @property
    def traspKg(self):
        return self.__traspKg
        
    @traspKg.setter
    def traspKg(self, value):
        if value > self.__maxKg:
            raise ValueError("Il peso della merce supera quello trasportabile")
        self.__traspKg = value
        return
