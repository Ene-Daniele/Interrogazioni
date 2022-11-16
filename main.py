import pickle
import time

from colorama import Fore
from colorama import Style

from studente import Studente, Class
import datetime


#TODO: Ene > Colorare i print un pochino

print(Style.BRIGHT + Fore.GREEN + " « Programmatore di interrogazioni » ")
print(Fore.WHITE + "💭 Usa 'help' per una lista di comandi", Fore.WHITE)

while True:
    choice = input(" > ").split(" ")
    if choice[0] == "help":
        print(Fore.CYAN + Style.BRIGHT + "help:" + Style.NORMAL + " Fa vedere i comandi disponibili\n" + Style.BRIGHT +
                             "extract:" + Style.NORMAL + " Estrae uno studente dalla classe selezionata\n" + Style.BRIGHT +
                             "adds [name] [surname]:" + Style.NORMAL + " Aggiunge uno studente nella classe selezionata\n" + Style.BRIGHT +
                             "list:" + Style.NORMAL + " Mostra tutti gli studenti della classe selezionata\n")
    elif choice[0] == "extract":
        print("WIP")
        pass
    elif choice[0] == "adds":
        try:
            nuovo_studente: Studente = Studente(
                choice[1],
                choice[2],
                Class.QUARTA_F_INF if input(Fore.WHITE + "Quarta F Inf? [Y]: yes, [*]: no, Quarta A Mech\n > ").lower() == "y" else Class.QUARTA_A_MEC)
            nuovo_studente.save()
            print("Studente aggiunto, per vedere il nuovo studente riavviare il programma.")
        except IndexError:
            print(Fore.RED + Style.BRIGHT + "Uno o piu parametri necessari mancanti! Prova 'adds nome cognome'")
    elif choice == "list":
        print("WIP")
    else:
        print(Fore.RED + Style.BRIGHT + "Comando inesistente")