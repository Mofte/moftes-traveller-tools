#!/usr/bin/env python
# -*- coding: utf-8 -*-

divider = "\n" + "-"*48 + "\n"

def translate_code(code):
  code = code.replace("A", "10")
  code = code.replace("a", "10")
  code = code.replace("B", "11")
  code = code.replace("b", "11")
  code = code.replace("C", "12")
  code = code.replace("c", "12")
  code = code.replace("D", "13")
  code = code.replace("d", "13")
  code = code.replace("E", "14")
  code = code.replace("e", "14")
  code = code.replace("F", "15")
  code = code.replace("f", "15")
  return code

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

print(divider)

print("Ein simpler UWP-Translator für Mongoose Traveller 1Ed.\n")

print(divider)

name = input("Bitte den Namen der Welt eingeben: ")

print(divider)

print("Bitte das gewünschte UWP nach und nach eingeben.")

print(divider)

port_true = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "X", "x"]

port_in = ""

while port_in not in port_true:
  port_in = input("1. Bitte die Raumhafenklasse (A-E, X) eingeben: ")

if port_in == "A" or port_in == "a":
    port_out += port[0]
elif port_in == "B" or port_in == "b":
    port_out += port[1]
elif port_in == "C" or port_in == "c":
    port_out += port[2]
elif port_in == "D" or port_in == "d":
    port_out += port[3]
elif port_in == "E" or port_in == "e":
    port_out += port[4]
elif port_in == "X" or port_in == "x":
    port_out += port[5]
    
print(port_out)

print(divider)

size_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a"]

size_in=""

while size_in not in size_true:
  size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")

size_out += size[int(translate_code(size_in))]

print(size_out)

print(divider)

atmo_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]

atmo_in=""

while atmo_in not in atmo_true:
  atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")

atmo_out += atmo[int(translate_code(atmo_in))]
    
print(atmo_out)

print(divider)
  
hydro_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a"]

hydro_in=""

while hydro_in not in hydro_true:
  hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")

hydro_out += hydro[int(translate_code(hydro_in))]

print(hydro_out)

print(divider)

pop_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c"]

pop_in=""

while pop_in not in pop_true:
  pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")

pop_out += pop[int(translate_code(pop_in))]

print(pop_out)

print(divider)

gov_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d"]

gov_in=""

while gov_in not in gov_true:
  gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")

gov_out += gov[int(translate_code(gov_in))]
  
print(gov_out)

print(divider)

just_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

just_in=""

while just_in not in just_true:
  just_in = input("7. Bitte den Justizgrad (0-9) eingeben: ")

just_out += just[int(just_in)]
    
print(just_out)

print(divider)

tech_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]

tech_in=""

while tech_in not in tech_true:
  tech_in = input("8. Bitte das Technologielevel (0-F) eingeben: ")

tech_out += tech[int(translate_code(tech_in))]
    
print(tech_out)

print(divider)

print(f"{name}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")

print(divider)