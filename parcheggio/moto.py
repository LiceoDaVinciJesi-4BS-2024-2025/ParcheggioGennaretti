from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, targa, maxPers, traspPers, marca = "", modello = ""):
        super().__init__(targa, marca, modello)
        self.__maxPers = maxPers
        if traspPers > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = traspPers
    
    def __str__(self):
        return "Moto:" + str(self.__dict__)
    
    @property
    def maxPers(self):
        return self.__maxPers

    @property
    def traspPers(self):
        return self.__traspPers
        
    @traspPers.setter
    def traspPers(self, value):
        if value > self.__maxPers:
            raise ValueError("Il numero di persone supera quello trasportabile")
        self.__traspPers = value
        return
