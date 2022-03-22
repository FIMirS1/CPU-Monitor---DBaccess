/*
    Das SQL-Skript erzeugt eine neue Beispieldatenbank.
	  In dieser wird eine Tabelle mit einigen Einträgen angelegt.
 
    Einordnung:			  FISI-LF5-LS3-Aufgabe-01
    Aufgabe:          aufgabe_ls3_03.sql

    Name:				      Thissen, Heil, Huppertz, von den Benken
    Organisaion:		  BK-GuT

    Erstellt:			    14.03.2022
    Letzte Änderung:	21.03.2022

*/
DROP DATABASE IF EXISTS aufgabe_ls3_01;                       # Evtl. vorhandene Datenbank löschen

CREATE DATABASE aufgabe_ls3_01 default character set utf8;    # Neue Beispieldatenbank anlegen

USE aufgabe_ls3_01;                                           # Mit neuer Datenbank verbinden

CREATE TABLE t1_demo (
  t1_ID INT AUTO_INCREMENT PRIMARY KEY,
  t1_Zeit datetime NOT NULL DEFAULT current_timestamp(),
  t1_Last float NOT NULL,
  t1_Takt float NOT NULL
)
