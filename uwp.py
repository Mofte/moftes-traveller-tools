#!/usr/bin/env python
# -*- coding: utf-8 -*-

divider = "\n" + "-"*48 + "\n"

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

print(divider)

size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")
if int(size_in) >= 0 and int(size_in) <= 9:
    size_out += size[int(size_in)]
elif size_in == "A" or size_in == "a":
    size_out += size[10]
else:
    print("falsche Eingabe")
    size_out += "Fehler bei der Eingabe!"
    
print(size_out)

print(divider)

atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")
if int(atmo_in) >= 0 and int(atmo_in) <=9:
    atmo_out += atmo[int(atmo_in)]
elif atmo_in == "A" or atmo_in == "a":
    atmo_out += atmo[10]
elif atmo_in == "B" or atmo_in == "b":
    atmo_out += atmo[11]
elif atmo_in == "C" or atmo_in == "c":
    atmo_out += atmo[12]
elif atmo_in == "D" or atmo_in == "d":
    atmo_out += atmo[13]
elif atmo_in == "E" or atmo_in == "e":
    atmo_out += atmo[14]
elif atmo_in == "F" or atmo_in == "f":
    atmo_out += atmo[15]
else:
    print("falsche Eingabe")
    atmo_out += "Fehler bei der Eingabe!"
    
print(atmo_out)

print(divider)

hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")
if int(hydro_in) >= 0 and int(hydro_in) <= 9:
    hydro_out += hydro[int(hydro_in)]
elif hydro_in == "A" or hydro_in == "a":
    hydro_out += hydro[10]
else:
    print("falsche Eingabe")
    hydro_out += "Fehler bei der Eingabe!"
    
print(hydro_out)

print(divider)

pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")
if int(pop_in) >= 0 and int(pop_in) <= 9:
    pop_out += pop[int(pop_in)]
elif pop_in == "A" or pop_in == "a":
    pop_out += pop[10]
elif pop_in == "B" or pop_in == "b":
    pop_out += pop[11]
elif pop_in == "C" or pop_in == "c":
    pop_out += pop[12]
else:
    print("falsche Eingabe")
    pop_out += "Fehler bei der Eingabe!"
    
print(pop_out)

print(divider)

gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")
if int(gov_in) >= 0 and int(gov_in) <= 9:
    gov_out += gov[int(gov_in)]
elif gov_in == "A" or gov_in == "a":
    gov_out += gov[10]
elif gov_in == "B" or gov_in == "b":
    gov_out += gov[11]
elif gov_in == "C" or gov_in == "c":
    gov_out += gov[12]
elif gov_in == "D" or gov_in == "d":
    gov_out += gov[13]
else:
    print("falsche Eingabe")
    gov_out += "Fehler bei der Eingabe!"

print(gov_out)

print(divider)

just_in = input("7. Bitte den Justizgrad (0-9+) eingeben: ")
if int(just_in) >= 0 and int(just_in) <= 9::
    just_out += just[int(just_in)]
elif just_in == "9+":
    just_out += just[9]
else:
    print("falsche Eingabe")
    just_out += "Fehler bei der Eingabe!"

print(just_out)

print(divider)

tech_in = input("8. Bitte das Technologielevel (0-F) eingeben: ")
if int(tech_in) >= 0 abd int(tech_in) <= 9:
    tech_out += tech[int(tech_in)]
elif tech_in == "A" or tech_in == "a":
    tech_out += tech[10]
elif tech_in == "B" or tech_in == "b":
    tech_out += tech[11]
elif tech_in == "C" or tech_in == "c":
    tech_out += tech[12]
elif tech_in == "D" or tech_in == "d":
    tech_out += tech[13]
elif tech_in == "E" or tech_in == "e":
    tech_out += tech[14] 
elif tech_in == "F" or tech_in == "f":
    tech_out += tech[15]
else:
    print("falsche Eingabe")
    tech_out += "Fehler bei der Eingabe!"
    
print(tech_out)

print(divider)

print(f"{name}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")