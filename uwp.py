#!/usr/bin/env python
# -*- coding: utf-8 -*-

divider = "\n" + "-"*48 + "\n"

def translate_uwp(uwp):
  uwp = uwp.replace("A", "10")
  uwp = uwp.replace("a", "10")
  uwp = uwp.replace("B", "11")
  uwp = uwp.replace("b", "11")
  uwp = uwp.replace("C", "12")
  uwp = uwp.replace("c", "12")
  uwp = uwp.replace("D", "13")
  uwp = uwp.replace("d", "13")
  uwp = uwp.replace("E", "14")
  uwp = uwp.replace("e", "14")
  uwp = uwp.replace("F", "15")
  uwp = uwp.replace("f", "15")
  return uwp

port = ["A - hervorragend","B - gut","C - mittelmäßig","D - schlecht","E - lediglich eine Grenzinstallation","X - kein Raumhafen"]
port_out = "Raumhafenklasse: "
size = ["800 km", "1.600 km", "3.200 km", "4.800 km", "6.400 km", "8.000 km", "9.600 km", "11.200 km", "12.800 km", "14.400 km", "16.000 km"]
size_out = "Weltengröße: "
atmo = ["keine", "Spuren", "Verschmutzt, sehr dünn", "Sehr dünn", "Verschmutzt, dünn", "Dünn", "Standard", "Verschmutzt, Standard", "Dicht", "Verschmutzt, Dicht", "Exotisch", "Ätzend", "Aggressiv", "Dicht, Hoch", "Dünn, Niedrig", "Ungewöhnlich"]
atmo_out = "Atmosphäre: "
hydro = ["Wüstenwelt", "Trockene Welt", "Einige wenige kleine Meere", "Kleine Meere und Ozeane", "Feuchte Welt", "Große Ozeane", "Größere Ozeane", "Erdähnliche Welt", "Wasserwelt", "Nur einige kleine Inseln und Archipele", "Fast nur Wasser"]
hydro_out = "Hydrographie: "
pop = ["Keine", "Wenige", "Hunderte", "Tausende", "Zehntausende", "Huderttausende", "Millionen", "Zehnmillionenn", "Hundertmillionen", "Millarden", "Zehmillarden", "Hundertmilliarden", "Billionen"]
pop_out = "Population: "
gov = ["keine", "Firma/Konzern", "Partizipierende Demokratie", "Selbsterhaltende Oligarchie", "Repräsentative Demokratie", "Feudaltechnokratie", "Gefangene Regierung", "Balkanisierung", "Staatsdienst-Bürokratie", "Unpersönliche Bürokratie", "Charismatischer Diktator", "Uncharismatischer Führer", "Charismatische Oligarchie","Religiöse Diktatur"]
gov_out = "Regierngsform: "
just = ["ist quasi inexistent","schränkt kaum etwas ein","ist sehr permissiv","ist ausgewogen, aber permissiv","ist ausgewogen","ist restriktiv","ist streng","ist sehr streng","ist harsch","ist totalitär"]
just_out = "Justizgrad: "
tech = ['primitiv','primitiv','primitiv','primitiv','industriell','industriell','industriell','prä-stellar','prä-stellar','prä-stellar','früh-stellar','früh-stellar','stellar','stellar','stellar','hochstellar']
tech_out = "Technologielevel: "

print("\t\t\t\t\t-----")
print("\t\t\t\t-----")
print("\t\t\t-----")
print("\t\t-----")
print("\t-----\n")
print("Ein simpler UWP-Translator für Mongoose Traveller 1Ed.\n")
print("\t-----")
print("\t\t-----")
print("\t\t\t-----")
print("\t\t\t\t-----")
print("\t\t\t\t\t-----\n")

name = input("Bitte den Namen der Welt eingeben: ")

print(divider)

print("Bitte das gewünschte UWP nach und nach eingeben.")
port_in = input("1. Bitte die Raumhafenklasse (A-E, X) eingeben: ")
size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")
atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")
hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")
pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")
gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")
just_in = input("7. Bitte den Justizgrad (0-9+) eingeben: ")
tech_in = input("8. Bitte das Technologielevel (0-F) eingeben: ")

uwp = (port_in, size_in, atmo_in, hydro_in, pop_in, gov_in, just_in, tech_in)

translate_uwp(uwp)

int(uwp)

port_out += port[uwp[0]]
size_out += size[uwp[1]]
atmo_out += atmo[uwp[2]]
hydro_out += hydro[uwp[3]]
pop_out += pop[uwp[4]]
gov_out += gov[uwp[5]]
just_out += just[uwp[6]]
tech_out += tech[uwp[7]]

print(divider)

print(f"{name}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")