import sys
sys.path.append('parcheggio/')
from parcheggio import Parcheggio
from auto import Auto
from moto import Moto
from camion import Camion
from autobus import Autobus

nome = "ParcheggioGennaretti"
parcheggio = Parcheggio(nome)
print(f"Benvenuto in {parcheggio.nome}!")

while True:
    # print("Martino è un tontolone") #PROF: è vero!!!!
    # PROF: un menù interattivo testuale... welcome back to the 80s... :D
    scelta = str.lower(input("Cosa vuoi fare? 'crea / occupa / libera / contaPostiOccupati / salva / carica / parcheggio: "))
    if scelta == "parcheggio":
        print(parcheggio)


    elif scelta == "crea": # Crea il posto nell'oggetto parcheggio
        tipoMezzo = str.lower(input("Inserire tipoMezzo: "))
        parcheggio.creaPosto(tipoMezzo)
    

    elif scelta == "occupa": # Occupa un posto per un mezzo specifico es. Auto nell'oggetto Parcheggio
        tipoMezzo = input("Inserire tipoMezzo: ")
        targa = input("Inserire targa: ")
        oreSosta = int(input("Quante ore vuoi sostare? "))
        if tipoMezzo == "auto":
            parcheggio.parcheggiaPosto(Auto(targa, 4, 1), tipoMezzo, oreSosta) # N.B Gli attributi dell'oggetto veicolo oltre la targa prendono valori "default" (per risparmiare tempo)
        elif tipoMezzo == "moto":
            parcheggio.parcheggiaPosto(Moto(targa, 2, 1), tipoMezzo, oreSosta)
        elif tipoMezzo == "camion":
            parcheggio.parcheggiaPosto(Camion(targa, 300, 10), tipoMezzo, oreSosta)
        elif tipoMezzo == "autobus":
            parcheggio.parcheggiaPosto(Autobus(targa, 80, 35), tipoMezzo, oreSosta)


    elif scelta == "libera": # Libera un posto per un mezzo specifico es. Auto nell'ogetto Parcheggio
        tipoMezzo = input("Inserire tipoMezzo: ")
        targa = input("Inserire targa: ")
        parcheggio.liberaPosto(targa, tipoMezzo)


    elif scelta == "visualizza": # Restituisce il conteggio dei posti occupati per tipo di veicolo
        print(parcheggio.conteggioPostiOccupati(tipoMezzo))


    elif scelta == "salva": # Da implementare
        parcheggio.salvaFile()
    

    elif scelta == "carica": # Da implementare
        parcheggio.caricaFile()
    
    else: 
        break