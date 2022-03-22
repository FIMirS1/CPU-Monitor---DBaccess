"""
    Das Programm schreibt eine SQL-Datenbank in eine CSV-Datei um.
 
    Einordnung:			FISI-LF5-LS3-Aufgabe-01
    Aufgabe: 			cpu_to_csv.py

    Name:				Thissen, Heil, Huppertz, von den Benken
    Organisaion:		BK-GuT

    Erstellt:			21.03.2022
    Letzte Änderung:	21.03.2022
"""


import pandas as pd
import pyodbc
from dblib import *

# Verbindung zur Datenbank aufbauen
print("Verbindung zur Datenbank aufbauen")
print("")
host, user, passwd, db = dbZugriffswerte()
connection = dbVerbindungAufbauen(host, user, passwd, db)

# Auswahl, welche Tabelle in der SQL-Datenbank in die CSV-Datei exportiert wird
sql_query = pd.read_sql_query(''' select * FROM t1_demo''',connection)

# Erstellung der CSV-Datei mit den Datensätzen aus der SQL-Datenbank 
df = pd.DataFrame(sql_query)
df.to_csv (r'cpu_to_csv.csv', index = False) 

# Verbindung mit der Datenbank wird beendet
dbVerbindungAbbauen(connection)