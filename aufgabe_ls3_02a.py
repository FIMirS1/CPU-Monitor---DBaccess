"""
    Das Programm dient hauptsächlich der Ausgabe der Daten innerhalb der SQL-Datenbank.
 
    Einordnung:			FISI-LF5-LS3-Aufgabe-01
    Aufgabe: 			aufgabe_ls3_02b.py

    Name:				Thissen, Heil, Huppertz, von den Benken
    Organisaion:		BK-GuT

    Erstellt:			07.03.2022
    Letzte Änderung:	14.03.2022
"""


import psutil as ps     # Zeichnet CPU-Last auf
import pandas as pd     # Zum Konvertieren in eine CSV-Datei benötigt
import pyodbc           # Herstellen der Verbindung mit SQL mithilfe von pyodbc
from dblib import *

# Verbindung zur Datenbank aufbauen
print("Verbindung zur Datenbank aufbauen")
print("")
host, user, passwd, db = dbZugriffswerte()
connection = dbVerbindungAufbauen(host, user, passwd, db)

# Tabelleninhalt ausgeben
def dbWerteAusgeben():
    print("Tabelleninhalt ausgeben:")
    print("------------------------")
    print("Nr : Zeitpunkt : CPU-Last : CPU-Takt")
    counter = 0

    result = dbAbfrageAnweisung(connection, "SELECT * FROM t1_demo")    # Hier werden die zuvor eingetragegen Werte aus der Datenbank wieder ausgelesen 
    for zeile in result:                                                # Ergebnis zeilenweise durchlaufen und ausgeben
        print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]) + " : " + str(zeile[3]))
        counter +=1
    print("")


# Berechnen und Ausgeben des Durchschnittswerts
def dbMittelwertAusgeben():
    counter = 0
    sum = 0
    median = 0

    result = dbAbfrageAnweisung(connection, "SELECT * FROM t1_demo") # Hier werden die zuvor eingetragegen Werte aus der Datenbank wieder ausgelesen 
    for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
        counter +=1
        sum += zeile[2]
    median = sum/counter
    print("Durchschnittslast: ", "{:3.2f}".format(median), "%")

# Leere existierende Datenbank, sonst wird neue angelegt
def dbDatenbankLeeren():
    try:
        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE t1_demo")
    except:
        print("Es existiert bisher keine Datenbank t1_demo!")
        print("Erstelle neue Datenbank...")

        # Erzeuge neue Datenbank aus Skript
        sql_file = open("t1_demo.sql", "r", encoding="utf-8")
        sql_string = sql_file.read()
        cursor.execute(sql_string)
        sql_file.close()

# Exportiere SQL-Datenbank in CSV-Datei
def dbCSVExport():
    # Hier wird die Auswahl getroffen, welche Tabelle in der SQL-Datenbank in eine CSV-Datei exportiert wird.
    sql_query = pd.read_sql_query(''' select * FROM t1_demo''',connection)

    # Hier erfolgt die Erstellung der CSV-Datei mit den Datensätzen aus der SQL-Datenbank 
    df = pd.DataFrame(sql_query)
    df.to_csv (r'cpu_to_csv.csv', index = False) 


run = True
while run == True:
    print("----------")
    print("Menu")
    print("Datensätze ausgeben [1]")
    print("Durchschnittslast anzeigen [2]")
    print("Datensätze löschen [3]")
    print("Datensätze in CSV exportieren [4]")
    print("Beenden [5]")

    eingabe = input("")

    if eingabe == "1":
        dbWerteAusgeben()
    elif eingabe == "2":
        dbMittelwertAusgeben()
    elif eingabe == "3":
        dbDatenbankLeeren()
    elif eingabe == "4":
        dbCSVExport()
    elif eingabe == "5":
        run = False
        dbVerbindungAbbauen(connection)
    else:
        print("Die Eingabe ist nicht zulässig!")