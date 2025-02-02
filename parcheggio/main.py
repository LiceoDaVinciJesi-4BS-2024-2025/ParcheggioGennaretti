from parcheggio import Parcheggio


nome = input("Inserire nome del parcheggio: ")
parcheggio = Parcheggio(nome)

while True:
    # print("Martino è un tontolone")
    scelta = input("Cosa vuoi fare? 'creaPosto / occupaPosto / liberaPosto / conteggioPostiOccupati / Chiudi / Salva: ")
    if scelta == "creaPosto": # Crea un posto per un mezzo specifico es. Auto e viene inserito nell'ogetto Parcheggio
        tipoMezzo = input("Inserire tipoMezzo: ")
        parcheggio.creaPosto(tipoMezzo)
    
    elif scelta == "occupaPosto": # Occupa un posto per un mezzo specifico es. Auto nell'oggetto Parcheggio
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = int(input("Quante ore vuoi sostare? "))
        parcheggio.occupaPosto(targa, tipoMezzo, oreSosta)
    
    elif scelta == "liberaPosto": # Libera un posto per un mezzo specifico es. Auto nell'ogetto Parcheggio
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        parcheggio.liberaPosto(targa, tipoMezzo)

    elif scelta == "Visualizza": # Restituisce il conteggio dei posti occupati per tipo di veicolo
        tipoMezzo = input("Inserire tipoMezzo: ")
        print(parcheggio.conteggioPostiOccupati(tipoMezzo))

    elif scelta == "Salva": # Da implementare
        break

    elif scelta == "Chiudi": # Chiude il programma
        break

    elif scelta == "Visualizza Parcheggio":
        print(parcheggio)

    else:
        scelta = input("Cosa vuoi fare? 'creaPosto / occupaPosto / liberaPosto / conteggioPostiOccupati / Chiudi / Salva ")
