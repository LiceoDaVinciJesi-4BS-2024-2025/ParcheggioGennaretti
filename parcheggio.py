from postomezzo import PostoMezzo

parcheggio = []
contaPosti = {"auto": 1000, "moto": 200, "camion": 50, "autobus": 200}
guadagnoGG = {"auto": 1.5, "moto": 1.2, "camion": 1.8, "autobus": 2.4}
class Parcheggio(PostoMezzo):
    def __init__(self):
        super().__init__(tipoMezzo, )

    @property
    def contaPosti(self):
        return self.__contaPosti

    @property
    def guadagnoGiornaliero(self):
        return self.__guadagnoGiornaliero

    def __str__(self):
        a = "Parcheggio: " + str(self.__dict__)
        return a

    def postiLiberi(self, tipoMezzo):
        if str.lower(tipoMezzo) not in mezziOK:
            raise ValueError("tipoMezzo non accettabile")
        return self.__contaPosti[tipoMezzo]

    def aggiornaFile(self, azione, postoMezzo):
        f = open("park.data", "w")
        if azione == "Prenota":
            f.write(postoMezzo)
        else:
            f.write(targa + " " + datetime.datetime.now())

while True:
    scelta = input("Cosa vuoi fare? 'Prenota/Libera/Visualizza Conteggio/Chiudi' ")
    if scelta == "Prenota":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        posto = PostoMezzo.prenota(targa, oreSosta)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] -= 1
