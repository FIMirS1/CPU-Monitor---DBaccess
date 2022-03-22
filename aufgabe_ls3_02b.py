"""
    Das Programm baut eine Verbindung zu einer Datenbank auf.
	Anschließend wird die CPU-Auslastung sowie der CPU-Takt ausgelesen.
    Die ausgelesenen Werte werden dann in die verknüpfte Datenbank geschrieben.
 
    Einordnung:			FISI-LF5-LS3-Aufgabe-01
    Aufgabe: 			aufgabe_ls3_02b.py

    Name:				Thissen, Heil, Huppertz, von den Benken
    Organisaion:		BK-GuT

    Erstellt:			07.03.2022
    Letzte Änderung:	14.03.2022
"""

import psutil as ps
from dblib import *


# Verbindung zur Datenbank aufbauen
print("Verbindung zur Datenbank aufbauen")
print("")
host, user, passwd, db = dbZugriffswerte()
connection = dbVerbindungAufbauen(host, user, passwd, db)

# Funktion zum Aufzeichnen der CPU-Auslastung
# Zeichnet "limit" viele Sekunden auf
def anzeigenRessourcenVerbrauch(limit):
    counter = 0
    while counter < limit:
        cpuAuslastung = ps.cpu_percent(interval=1) # Eintragung der CPU Last in einem Intervall von 1 Sekunde.
        cpuTakt = ps.cpu_freq(percpu=False)
        print( "CPU-Auslastung:", cpuAuslastung, "%")
        print("CPU-Takt:", cpuTakt[0], "MHz")
        sqlStatement = "INSERT INTO t1_demo (t1_Last, t1_Takt) VALUES ("+str(cpuAuslastung)+", "+ str(cpuTakt[0])+")" # Werteintrag in die DB.
        dbNichtAbfrageAnweisung(connection, sqlStatement)
        counter += 1
    dbVerbindungAbbauen(connection)
    return

# Ausführen der eigentlichen Aufgaben - Festlegen eines Limits durch den Benutzer und Messen der Werte
limit = int(input("wie viele Sekunden lang soll die CPU überwacht werden? "))
anzeigenRessourcenVerbrauch(limit)



