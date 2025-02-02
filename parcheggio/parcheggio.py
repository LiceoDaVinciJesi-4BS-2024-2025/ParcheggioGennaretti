from postomezzo import PostoMezzo
import csv

mezziOK = ("auto", "moto", "camion", "autobus")

class Parcheggio:
    def __init__(self, nome: str):
        self.__parcheggio = {"auto": [], "moto": [], "camion": [], "autobus": []}

        self.__tariffaGG = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}
        self.__contaOre = {"auto": 0, "moto": 0, "camion": 0, "autobus": 0}
        self.__guadagnoTotaleGG = {"auto": self.__contaOre["auto"] * self.__tariffaGG["auto"], "moto": self.__contaOre["moto"] * self.__tariffaGG["moto"], "camion": self.__contaOre["camion"] * self.__tariffaGG["camion"], "autobus": self.__contaOre["autobus"] * self.__tariffaGG["autobus"]}

        self.__contaPostiOccupati = {"auto": 0, "moto": 0, "camion": 0, "autobus": 0}
        self.__postiMax = {"auto": 1000, "moto": 500, "camion": 100, "autobus": 200}

        self.__nome = nome

    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a

    @property
    def parcheggio(self):
        """Restituisce il parcheggio"""
        return self.__parcheggio
    
    @property
    def tariffaGG(self):
        """Restituisce la tariffa giornaliera per tipo di veicolo"""
        return self.__tariffaGG
    
    @property
    def contaOre(self):
        """Restituisce il conteggio delle ore per tipo di veicolo"""
        return self.__contaOre

    @property
    def guadagnoTotaleGG(self):
        """Restituisce il guadagno giornaliero per tipo di veicolo"""
        return self.__guadagnoTotaleGG

    @property
    def contaPostiOccupati(self):
        """Restituisce il conteggio dei posti occupati per tipo di veicolo"""
        return self.__contaPostiOccupati
    
    @property
    def nome(self):
        """Restituisce il nome del parcheggio"""
        return self.__nome


    def guadagnoGiornaliero(self):
        """Restituisce il guadagno giornaliero totale del parcheggio"""
        return self.__guadagnoGG
    
    def creaPosto(self, tipoMezzo):
        """Crea un posto per un mezzo specifico es. Auto e viene inserito nell'ogetto Parcheggio"""
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        self.__parcheggio[tipoMezzo].append(PostoMezzo(False, tipoMezzo))

    def parcheggiaPosto(self, V, tipoMezzo, oreSosta) -> bool:
        """Occupa un posto per un mezzo specifico es. Auto nell'oggetto Parcheggio"""
        for posto in self.__parcheggio[tipoMezzo]:
            if not posto.occupato:
                posto.parcheggia(V, oreSosta)
                self.__contaPostiOccupati[tipoMezzo] += 1
                self.__contaOre[tipoMezzo] += oreSosta
                return True
        else:
            raise ValueError("Non ci sono posti disponibili")
        
    def liberaPosto(self, targa, tipoMezzo) -> bool:
        """Libera un posto per un mezzo specifico es. Auto nell'ogetto Parcheggio"""
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        for posto in self.__parcheggio[tipoMezzo]:
            if posto.occupato and posto.targa == targa:
                posto.libera()
                self.__contaPostiOccupati[tipoMezzo] -= 1
                return True

    def conteggioPostiOccupati(self, tipoMezzo = None) -> dict:
        """Restituisce il conteggio dei posti occupati per tipo di veicolo"""
        if tipoMezzo != None:
            if str.lower(tipoMezzo) not in mezziOK:
                raise ValueError("tipoMezzo non accettabile")
            return self.__contaPostiOccupati[tipoMezzo]
        else:
            return self.__contaPostiOccupati
        
        # conteggio = {}
        # for tipoMezzo in self.__parcheggio:
        #     conteggio[tipoMezzo] = 0
        #     for posto in self.__parcheggio[tipoMezzo]:
        #         if posto.occupato:
        #             conteggio[tipoMezzo] += 1
        # for tipoMezzo in mezziOK:
        #     self.__contaPostiOccupati[tipoMezzo] = conteggio[tipoMezzo]
        # return conteggio

    def postiLiberi(self, tipoMezzo) -> int:
        """Restituisce il numero di posti liberi per tipo di veicolo"""
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        return len(self.__postiMax[tipoMezzo]) - self.conteggioPostiOccupati()[tipoMezzo]

    def salvaFile(self):
        """Salva i dati del parcheggio in un file csv"""
        file = open("park.data", "w", newline="")
        scrittore = csv.DictWriter(file, mezziOK)
        scrittore.writeheader()
        for tipoMezzo in mezziOK:
            for riga in self.__parcheggio[tipoMezzo]:
                scrittore.writerow(riga)
        file.close()

    def caricaFile(self):
        """Carica i dati del parcheggio da un file csv"""
        file = open("park.data", "r")
        lettore = csv.DictReader(file)
        for riga in lettore:
            self.__parcheggio.append(riga)
        file.close()
