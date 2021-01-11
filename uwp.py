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

def translate_port_code(port_code):
    port_code = port_code.replace("A", "0")
    port_code = port_code.replace("a", "0")
    port_code = port_code.replace("B", "1")
    port_code = port_code.replace("b", "1")
    port_code = port_code.replace("C", "2")
    port_code = port_code.replace("c", "2")
    port_code = port_code.replace("D", "3")
    port_code = port_code.replace("d", "3")
    port_code = port_code.replace("E", "4")
    port_code = port_code.replace("e", "4")
    port_code = port_code.replace("X", "5")
    port_code = port_code.replace("x", "5")
    return port_code

port = ["A - hervorragend","B - gut","C - mittelmäßig","D - schlecht","E - lediglich eine Grenzinstallation","X - kein Raumhafen"]
port_true = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "X", "x"]
port_out = "Raumhafenklasse: "
size = ["800 km", "1.600 km", "3.200 km", "4.800 km", "6.400 km", "8.000 km", "9.600 km", "11.200 km", "12.800 km", "14.400 km", "16.000 km"]
size_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a"]
size_out = "Weltengröße: "
atmo = ["keine", "Spuren", "Verschmutzt, sehr dünn", "Sehr dünn", "Verschmutzt, dünn", "Dünn", "Standard", "Verschmutzt, Standard", "Dicht", "Verschmutzt, Dicht", "Exotisch", "Ätzend", "Aggressiv", "Dicht, Hoch", "Dünn, Niedrig", "Ungewöhnlich"]
atmo_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]
atmo_out = "Atmosphäre: "
hydro = ["Wüstenwelt", "Trockene Welt", "Einige wenige kleine Meere", "Kleine Meere und Ozeane", "Feuchte Welt", "Große Ozeane", "Größere Ozeane", "Erdähnliche Welt", "Wasserwelt", "Nur einige kleine Inseln und Archipele", "Fast nur Wasser"]
hydro_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a"]
hydro_out = "Hydrographie: "
pop = ["Keine", "Wenige", "Hunderte", "Tausende", "Zehntausende", "Huderttausende", "Millionen", "Zehnmillionenn", "Hundertmillionen", "Millarden", "Zehmillarden", "Hundertmilliarden", "Billionen"]
pop_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c"]
pop_out = "Population: "
gov = ["keine", "Firma/Konzern", "Partizipierende Demokratie", "Selbsterhaltende Oligarchie", "Repräsentative Demokratie", "Feudaltechnokratie", "Gefangene Regierung", "Balkanisierung", "Staatsdienst-Bürokratie", "Unpersönliche Bürokratie", "Charismatischer Diktator", "Uncharismatischer Führer", "Charismatische Oligarchie","Religiöse Diktatur"]
gov_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d"]
gov_out = "Regierungsform: "
just = ["ist quasi inexistent","schränkt kaum etwas ein","ist sehr permissiv","ist ausgewogen, aber permissiv","ist ausgewogen","ist restriktiv","ist streng","ist sehr streng","ist harsch","ist totalitär"]
just_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
just_out = "Justizgrad: "
tech = ['primitiv','primitiv','primitiv','primitiv','industriell','industriell','industriell','prä-stellar','prä-stellar','prä-stellar','früh-stellar','früh-stellar','stellar','stellar','stellar','hochstellar']
tech_true = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a",  "B", "b", "C", "c", "D", "d", "E", "e", "F", "f"]
tech_out = "Technologielevel: "

print(divider)

print("Ein simpler UWP-Translator für Mongoose Traveller 1Ed.\n")

print(divider)

name = input("Bitte den Namen der Welt eingeben: ")

print(divider)

print("Soll das UWP komplett oder Schritt für Schritt eingegeben werden?")
input_choice =""
while input_choice != "1" and input_choice != "2":
    input_choice = input("Für die Eingabe eines kompletten UWP bitte '1' eingeben, für die Eingabe jedes einzelnen Codes bitte '2' eingeben: ")

print(divider)

if input_choice == "1":
    print("""Hinweis:
Das UWP ist in der folgenden Reihenfolge einzugeben:
    1. Raumhafenklasse (A-E, X)
    2. Weltengröße (0-A)
    3. Atmosphäre (0-F)
    4. Hydrographie (0-A)
    5. Population (0-C)
    6. Regierungsform (0-D)
    7. Justizgrad (0-9)
    8. Bindestrich
    9. Technologielevel (0-F)
(Bsp.: A325B93-E)""")
    
    print(divider)
        
    uwp_in=""
    while (len(uwp_in) != 9) or str(uwp_in[0]) not in port_true or uwp_in[1] not in size_true or uwp_in[2] not in atmo_true or uwp_in[3] not in hydro_true or uwp_in[4] not in pop_true or uwp_in[5] not in gov_true or uwp_in[6] not in just_true or uwp_in[8] not in tech_true:
        uwp_in = input("Bitte das UWP eingeben: ")
        
    port_out += port[int(translate_port_code(uwp_in[0]))]
    size_out += size[int(translate_code(uwp_in[1]))]
    atmo_out += atmo[int(translate_code(uwp_in[2]))]
    hydro_out += hydro[int(translate_code(uwp_in[3]))]
    pop_out += pop[int(translate_code(uwp_in[4]))]
    gov_out += gov[int(translate_code(uwp_in[5]))]
    just_out += just[int(translate_code(uwp_in[6]))]
    tech_out += tech[int(translate_code(uwp_in[7]))]


elif input_choice == "2":
    print("Bitte das gewünschte UWP nach und nach eingeben.")

    print(divider)

    port_in = ""

    while port_in not in port_true:
        port_in = input("1. Bitte die Raumhafenklasse (A-E, X) eingeben: ")
    
    port_out += port[int(translate_port_code(port_in))]
        
    print(port_out)

    print(divider)

    size_in=""

    while size_in not in size_true:
        size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")

    size_out += size[int(translate_code(size_in))]

    print(size_out)

    print(divider)

    atmo_in=""

    while atmo_in not in atmo_true:
        atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")

    atmo_out += atmo[int(translate_code(atmo_in))]
    
    print(atmo_out)

    print(divider)

    hydro_in=""

    while hydro_in not in hydro_true:
        hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")

    hydro_out += hydro[int(translate_code(hydro_in))]

    print(hydro_out)

    print(divider)

    pop_in=""

    while pop_in not in pop_true:
        pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")

    pop_out += pop[int(translate_code(pop_in))]

    print(pop_out)

    print(divider)

    gov_in=""

    while gov_in not in gov_true:
        gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")

    gov_out += gov[int(translate_code(gov_in))]
  
    print(gov_out)

    print(divider)

    just_in=""

    while just_in not in just_true:
        just_in = input("7. Bitte den Justizgrad (0-9) eingeben: ")

    just_out += just[int(just_in)]
    
    print(just_out)

    print(divider)

    tech_in=""

    while tech_in not in tech_true:
        tech_in = input("8. Bitte das Technologielevel (0-F) eingeben: ")

    tech_out += tech[int(translate_code(tech_in))]
    
    print(tech_out)

print(divider)

print(f"{name}\n{'-' * len(name)}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")

print(divider)
