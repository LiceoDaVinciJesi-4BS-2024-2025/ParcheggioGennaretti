import datetime
from auto import Auto
from moto import Moto
from autobus import Autobus
from camion import Camion
from veicolo import targaValida

mezziOK = ("auto", "moto", "camion", "autobus")

class PostoMezzo:
    def __init__(self, occupato: bool = None, tipoMezzo: str = None, targa: str = None, oreSosta: int = None, fineSosta: int = None):
    
        if occupato == None:
            raise ValueError("Specificare se il posto è libero o occupato")
        self.__occupato = occupato
        
        if tipoMezzo not in mezziOK:
            raise ValueError("Specificare la tipologia di posto")
        self.__tipoMezzo = str.lower(tipoMezzo)
        
        if not occupato and (targa != None or oreSosta != None):
            raise ValueError("Un posto libero non può avere targa o oreSosta")
        
        if occupato and (targa == None or oreSosta == None):
            raise ValueError("Un posto occupato deve avere targa e oreSosta")
        
        elif occupato and targa != None and oreSosta != None:
            if len(targa) != 7 or not targaValida(targa):
                raise ValueError("La targa inserita non è valida")
            self.__targa = targa
        
            self.__oreSosta = oreSosta
            self.__fineSosta = datetime.datetime.now() + datetime.timedelta(hours = oreSosta) # Calcola l'orario di fine sosta
            return
              
        self.__targa = targa
        
        self.__oreSosta = oreSosta
        
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    @property
    def occupato(self):
        """Restituisce se il posto è occupato o meno"""
        return self.__occupato
    
    @occupato.setter
    def occupato(self, value):
        self.__occupato = value
        return
    
    @property
    def tipoMezzo(self):
        """Restituisce il tipo di mezzo"""
        return self.__tipoMezzo
    
    @tipoMezzo.setter
    def tipoMezzo(self, value):
        self.__tipoMezzo = value
        return
    
    @property
    def targa(self):
        """proprietà sola lettura: la targa NON deve essere modificabile"""
        return self.__targa
    
    @targa.setter
    def targa(self, value):
        self.__targa = value
    
    @property
    def oreSosta(self):
        """Restituisce le ore di sosta"""
        return self.__oreSosta
    
    @oreSosta.setter
    def oreSosta(self, value):
        self.__oreSosta = value
        self.__fineSosta = datetime.datetime.now() + datetime.timedelta(hours = value) # Calcola l'orario di fine sosta
        return
    
    @property
    def fineSosta(self):
        """Restituisce l'orario di fine sosta"""
        return self.__fineSosta
    
    def parcheggia(self, V, oreSosta) -> bool:
        """Parcheggia un veicolo in un posto"""
        if self.occupato:
            return False
        if isinstance(V, Moto) and self.tipoMezzo == "moto":
            self.occupato = True
            self.targa = V.targa
            self.oreSosta = oreSosta

        elif isinstance(V, Auto) and self.tipoMezzo == "auto":
            self.occupato = True
            self.targa = V.targa
            self.oreSosta = oreSosta

        else:
            return False
        
        return True
    
    def libera(self) -> bool:
        """Libera un posto"""
        if self.occupato:
            self.targa = None
            self.oreSosta = None
            self.occupato = False    
            return True
        
        else:
            return False
