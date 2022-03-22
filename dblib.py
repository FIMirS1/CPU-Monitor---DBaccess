"""
    Das Programm ist für die Verbindung zwischen dem Hauptprogramm und der Datenbank verantwortlich.
    Es ist zudem für die Ausführung von SQL-Anweisungen zuständig.
 
    Einordnung:			FISI-LF5-LS3-Aufgabe-01
    Aufgabe: 			dblib.py

    Name:				Thissen, Heil, Huppertz, von den Benken
    Organisaion:		BK-GuT

    Erstellt:			21.03.2022
    Letzte Änderung:	21.03.2022
"""


import mysql.connector
from random import random

# Verbindungsaufbau mit der MySQL-Datenbank
# Erstellte Verbindung wird als return zurückgegeben
def dbVerbindungAufbauen(host, user, passwd, db):
    verbindung = mysql.connector.connect(
        host="localhost", port=3306, user="root", passwd="", db="aufgabe_ls3_01"
    )
    return verbindung

# Funktion zum Beenden der Verbindung mit einer SQL-Datenbank
def dbVerbindungAbbauen(verbindung):
    verbindung.close()

# Funktion zur Ausführung einer Anweisung in einer SQL-Datenbank ohne Abfrage
def dbNichtAbfrageAnweisung(verbindung, anweisung):
    """ Funktion zur Ausführung einer Nicht-Abfrage-Anweisung bei MySQL-Datenbank """
    cursor = verbindung.cursor()         # Cursor öffnen
    cursor.execute(anweisung)            # Anweisung ausführen
    verbindung.commit()                  # Bestättigen
    cursor.close()                       # Cursor schliessen

# Funktion zur Ausführung einer Anweisung in einer SQL-Datenbank mit Abfrage
def dbAbfrageAnweisung(verbindung, anweisung):
    cursor = verbindung.cursor()         # Cursor öffnen
    cursor.execute(anweisung)            # Anweisung ausführen
    ergebnisMenge = cursor.fetchall()    # Ergebnismenge abholen
    cursor.close()                       # Cursor schliessen
    return ergebnisMenge

# Funktion die die Zugriffsdaten für die MySQL-Datenbank zurückgibt
def dbZugriffswerte():
    return "localhost", "root", "", "aufgabe_ls3_01"
