import random

# apertura file
infile = open("domande.txt", "r", encoding="utf-8")
lines = infile.readlines()
dimensione = len(lines)

#definizione classe
class Prodotto:
    def __init__(self, domanda, punteggio, risposta1, risposta2, risposta3, risposta4):
        self.domanda = domanda
        self.punteggio = punteggio
        self.risposta1 = risposta1
        self.risposta2 = risposta2
        self.risposta3 = risposta3
        self.risopsta4 = risposta4

#creazione classe
lista = list()
for i in range (0, dimensione, 7):
    el = Prodotto(lines[i].strip("\n"), int((lines[i+1]).strip("\n")), lines[i+2].strip("\n"), lines[i+3].strip("\n"), lines[i+4].strip("\n"), lines[i+5].strip("\n"))
    lista.append(el)

#numero maggiore
punteggio_max = 0
count = -1
for el in lista:
    if el.punteggio > punteggio_max:
        punteggio_max = el.punteggio

#output console
for a in range (0, punteggio_max+1):
    lista_specifica = list()
    for elemento in lista:
        if elemento.punteggio == a:
            lista_specifica.append(elemento)

    numero = random.randint(0, len(lista_specifica)-1)
    print("Livello " + str(a) + ") " + lista_specifica[numero].domanda)

    lista_risposte = list()
    lista_risposte.extend([lista_specifica[numero].risposta1, lista_specifica[numero].risposta2, lista_specifica[numero].risposta3, lista_specifica[numero].risopsta4])
    risposte = random.sample(lista_risposte, 4)
    for i in range(0, len(risposte)):
        print(5 * " " + str(i+1) + ". " + risposte[i])

    risposta = int(input("Inserisci la risposta: "))
    if lista_specifica[numero].risposta1 != risposte[risposta-1]:
        valore = 0
        for r in range (0, 4):
            if risposte[r] == lista_specifica[numero].risposta1:
                valore = str(r+1)
        print("Risposta sbagliata! La risposta corretta era: " + valore)
        print("\nHai totalizzato " + str(a) + " punti")
        nickname = input("Inserisci il tuo nickname: ")
        punteggio = a
        break
    else:
        print("Risposta corretta!\n")
        count = count + 1

if count == punteggio_max:
    print("Hai risposto correttamente a tutte le domande! ")
    nickname = input("Inserisci il tuo nickname: ")
    punteggio = punteggio_max

#output file
file = open("punti.txt", "r", encoding="utf-8")
righe = file.readlines()
lista_agg = list()
for e in righe:
    e = e.strip("\n")
    valore = e.split()
    lista_agg.append(valore[0])
    lista_agg.append(valore[1])

contatore = 0
for i in range(1, len(lista_agg), 2):
    value = int(lista_agg[i])
    if int(lista_agg[i]) < punteggio:
        lista_agg.insert(i-1, punteggio)
        lista_agg.insert(i-1, nickname)
        contatore = 1
        break
if contatore == 0:
    lista_agg.append(nickname)
    lista_agg.append(punteggio)

lista_output = list()
for t in range (0, len(lista_agg), 2):
    lista_output.append(lista_agg[t] + " " + str(lista_agg[t+1]) + "\n")

file.close()

outfile = open("punti.txt", "w")
outfile.writelines(lista_output)
outfile.close()

infile.close()