import datetime
from auto import Auto
from moto import Moto
from autobus import Autobus
from camion import Camion
from veicolo import targaValida

mezziOK = ("auto", "moto", "camion", "autobus")

class PostoMezzo:
    def __init__(self, occupato: bool = None, tipoMezzo: str = None, veicolo: object = None, oreSosta: float = None):
    
        if occupato == None:
            raise ValueError("Specificare se il posto è libero o occupato")
        self.__occupato = occupato
        
        if tipoMezzo not in mezziOK:
            raise ValueError("Specificare la tipologia di posto")
        self.__tipoMezzo = str.lower(tipoMezzo)
        
        if not occupato and (veicolo != None or oreSosta != None):
            raise ValueError("Un posto libero non può avere targa o oreSosta")
        
        if occupato and (veicolo == None or oreSosta == None):
            raise ValueError("Un posto occupato deve avere targa e oreSosta")
        
        elif occupato and veicolo != None and oreSosta != None:
            if not targaValida(veicolo):
                raise ValueError("La targa inserita non è valida")
            self.__veicolo = None
            self.__oreSosta = oreSosta
            self.__fineSosta = datetime.datetime.now() + datetime.timedelta(hours = oreSosta) # Calcola l'orario di fine sosta
            return
        
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
    def veicolo(self):
        """proprietà sola lettura: il veicolo NON deve essere modificabile"""
        return self.__targa
    
    @veicolo.setter
    def veicolo(self, value):
        self.__veicolo = value

    @property
    def mezzo(self):
        """Restituisce l'oggetto del mezzo"""
        return self.__mezzo
    
    @mezzo.setter
    def mezzo(self, value):
        self.__mezzo = value
        return
    
    @property
    def oreSosta(self):
        """Restituisce le ore di sosta"""
        return self.__oreSosta
    
    @oreSosta.setter
    def oreSosta(self, value):
        self.__oreSosta = value
        return
    
    @property
    def fineSosta(self):
        """Restituisce l'orario di fine sosta"""
        return self.__fineSosta

    @fineSosta.setter
    def fineSosta(self, value):
        self.__fineSosta = value
        return
    
    def parcheggia(self, V, oreSosta) -> bool:
        """Parcheggia un veicolo in un posto"""
        if self.occupato:
            return False
        if isinstance(V, Moto) and self.tipoMezzo == "moto":
            self.occupato = True
            self.veicolo = V
            self.oreSosta = oreSosta

        elif isinstance(V, Auto) and self.tipoMezzo == "auto":
            self.occupato = True
            self.veicolo = V
            self.oreSosta = oreSosta
        
        elif isinstance(V, Camion) and self.tipoMezzo == "camion":
            self.occupato = True
            self.veicolo = V
            self.oreSosta = oreSosta
        
        elif isinstance(V, Autobus) and self.tipoMezzo == "autobus":
            self.occupato = True
            self.veicolo = V
            self.oreSosta = oreSosta

        else:
            return False
        
        return True
    
    def libera(self) -> bool:
        """Libera un posto"""
        if self.occupato:
            self.veicolo = None
            self.oreSosta = None
            self.occupato = False 
            self.fineSosta = None  
            self.mezzo = None 
            return True
        
        else:
            return False
