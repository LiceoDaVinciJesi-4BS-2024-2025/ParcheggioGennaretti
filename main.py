from parcheggio import Parcheggio

while True:
    scelta = input("Cosa vuoi fare? 'Prenota/Libera/Visualizza Conteggio/Chiudi' ")
    if scelta == "Prenota":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        posto = Parcheggio.prenota(targa, oreSosta)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] -= 1
    elif scelta == "Libera":
        targa = input("Inserire targa: ")
        tipoMezzo = input("Inserire tipoMezzo: ")
        oreSosta = input("Quante ore vuoi sostare? ")
        posto = PostoMezzo.libera(targa, oreSosta)
        parcheggio.append(posto)
        contaPosti[tipoMezzo] += 1
    elif scelta == "Visualizza Conteggio":
        print(contaPosti)
    elif scelta == "Chiudi":
        break
    else:
        input("Cosa vuoi fare? 'Prenota/Libera/Visualizza Conteggio/Chiudi' ")