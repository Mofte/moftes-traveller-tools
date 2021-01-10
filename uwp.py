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


print("Ein simpler UWP-Translator für Mongoose Traveller 1Ed.\n")

name = input("Bitte den Namen der Welt eingeben: ")

print(divider)

print("Bitte das gewünschte UWP nach und nach eingeben.")

print(divider)

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
else:
    print("falsche Eingabe")
    port_out += "Fehler bei der Eingabe!"
    
print(port_out)

divider()

size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")

size_in = int(translate_code(size_in))

if size_in >= 0 and size_in <= 10:
  size_out += size[size_in]
else:
    print("falsche Eingabe")
    size_out += "Fehler bei der Eingabe!"
    
print(size_out)

divider()

atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")

atmo_in = int(translate_code(atmo_in))

if atmo_in >= 0 and atmo_in <= 15:
  atmo_out += atmo[atmo_in]
else:
  print("falsche Eingabe")
  atmo_out += "Fehler bei der Eingabe!"
    
print(atmo_out)

divider()
  
hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")

hydro_in = int(translate_code(hydro_in))

if hydro_in >= 0 and hydro_in <= 10:
  hydro_out += hydro[hydro_in]
else:
  print("falsche Eingabe")
  hydro_out += "Fehler bei der Eingabe!"
    
print(hydro_out)

divider()

pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")

pop_in = int(translate_code(pop_in))

if pop_in >= 0 and pop_in <= 12:
  pop_out += pop[pop_in]
else:
  print("falsche Eingabe")
  pop_out += "Fehler bei der Eingabe!"
    
print(pop_out)

divider()

gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")

gov_in = int(translate_code(gov_in))

if gov_in >= 0 and gov_in <= 13:
  gov_out += gov[gov_in]
else:
  print("falsche Eingabe")
  gov_out += "Fehler bei der Eingabe!"
    
print(gov_out)

divider()

just_in = input("7. Bitte den Justizgrad (0-9) eingeben: ")

if just_in >= 0 and just_in <= 9:
  just_out += just[just_in]
else:
  print("falsche Eingabe")
  just_out += "Fehler bei der Eingabe!"
    
print(just_out)

divider()

tech_in = input("8. Bitte das Technologielevel (0-F) eingeben: ")

tech_in = int(translate_code(tech_in))

if tech_in >= 0 and tech_in <= 15:
  tech_out += tech[tech_in]
else:
  print("falsche Eingabe")
  tech_out += "Fehler bei der Eingabe!"
    
print(tech_out)

divider()

print(f"{name}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")