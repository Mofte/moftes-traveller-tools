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

print("\n------------------------------------------------\n")

print("Bitte das gewünschte UWP nach und nach eingeben.")

print("\n------------------------------------------------\n")

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

print("\n------------------------------------------------\n")

size_in = input("2. Bitte die Weltengröße (0-A) eingeben: ")
if size_in == "0":
    size_out += size[0]
elif size_in == "1":
    size_out += size[1]
elif size_in == "2":
    size_out += size[2]
elif size_in == "3":
    size_out += size[3]
elif size_in == "4":
    size_out += size[4]
elif size_in == "5":
    size_out += size[5]
elif size_in == "6":
    size_out += size[6]
elif size_in == "7":
    size_out += size[7]
elif size_in == "8":
    size_out += size[8]
elif size_in == "9":
    size_out += size[9]
elif size_in == "A" or size_in == "a":
    size_out += size[10]
else:
    print("falsche Eingabe")
    size_out += "Fehler bei der Eingabe!"
    
print(size_out)

print("\n------------------------------------------------\n")

atmo_in = input("3. Bitte den Atmosphärewert (0-F) eingeben: ")
if atmo_in == "0":
    atmo_out += atmo[0]
elif atmo_in == "1":
    atmo_out += atmo[1]
elif atmo_in == "2":
    atmo_out += atmo[2]
elif atmo_in == "3":
    atmo_out += atmo[3]
elif atmo_in == "4":
    atmo_out += atmo[4]
elif atmo_in == "5":
    atmo_out += atmo[5]
elif atmo_in == "6":
    atmo_out += atmo[6]
elif atmo_in == "7":
    atmo_out += atmo[7]
elif atmo_in == "8":
    atmo_out += atmo[8]
elif atmo_in == "9":
    atmo_out += atmo[9]
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

print("\n------------------------------------------------\n")

hydro_in = input("4. Bitte den Hydrographiewert (0-A) eingeben: ")
if hydro_in == "0":
    hydro_out += hydro[0]
elif hydro_in == "1":
    hydro_out += hydro[1]
elif hydro_in == "2":
    hydro_out += hydro[2]
elif hydro_in == "3":
    hydro_out += hydro[3]
elif hydro_in == "4":
    hydro_out += hydro[4]
elif hydro_in == "5":
    hydro_out += hydro[5]
elif hydro_in == "6":
    hydro_out += hydro[6]
elif hydro_in == "7":
    hydro_out += hydro[7]
elif hydro_in == "8":
    hydro_out += hydro[8]
elif hydro_in == "9":
    hydro_out += hydro[9]
elif hydro_in == "A" or hydro_in == "a":
    hydro_out += hydro[10]
else:
    print("falsche Eingabe")
    hydro_out += "Fehler bei der Eingabe!"
    
print(hydro_out)

print("\n------------------------------------------------\n")

pop_in = input("5. Bitte den Populationswert (0-C) eingeben: ")
if pop_in == "0":
    pop_out += pop[0]
elif pop_in == "1":
    pop_out += pop[1]
elif pop_in == "2":
    pop_out += pop[2]
elif pop_in == "3":
    pop_out += pop[3]
elif pop_in == "4":
    pop_out += pop[4]
elif pop_in == "5":
    pop_out += pop[5]
elif pop_in == "6":
    pop_out += pop[6]
elif pop_in == "7":
    pop_out += pop[7]
elif pop_in == "8":
    pop_out += pop[8]
elif pop_in == "9":
    pop_out += pop[9]
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

print("\n------------------------------------------------\n")
gov_in = input("6. Bitte den Regierungstyp (0-D) eingeben: ")
if gov_in == "0":
    gov_out += gov[0]
elif gov_in == "1":
    gov_out += gov[1]
elif gov_in == "2":
    gov_out += gov[2]
elif gov_in == "3":
    gov_out += gov[3]
elif gov_in == "4":
    gov_out += gov[4]
elif gov_in == "5":
    gov_out += gov[5]
elif gov_in == "6":
    gov_out += gov[6]
elif gov_in == "7":
    gov_out += gov[7]
elif gov_in == "8":
    gov_out += gov[8]
elif gov_in == "9":
    gov_out += gov[9]
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

print("\n------------------------------------------------\n")
just_in = input("7. Bitte den Justizgrad (0-9+) eingeben: ")
if just_in == "0":
    just_out += just[0]
elif just_in == "1":
    just_out += just[1]
elif just_in == "2":
    just_out += just[2]
elif just_in == "3":
    just_out += just[3]
elif just_in == "4":
    just_out += just[4]
elif just_in == "5":
    just_out += just[5]
elif just_in == "6":
    just_out += just[6]
elif just_in == "7":
    just_out += just[7]
elif just_in == "8":
    just_out += just[8]
elif just_in == "9" or just_in == "9+":
    just_out += just[9]
else:
    print("falsche Eingabe")
    just_out += "Fehler bei der Eingabe!"

print(just_out)

print("\n------------------------------------------------\n")

tech_in = input("8. Bitte das Technologielevel (0-15) eingeben: ")
if tech_in == "0":
    tech_out += tech[0]
elif tech_in == "1":
    tech_out += tech[1]
elif tech_in == "2":
    tech_out += tech[2]
elif tech_in == "3":
    tech_out += tech[3]
elif tech_in == "4":
    tech_out += tech[4]
elif tech_in == "5":
    tech_out += tech[5]
elif tech_in == "6":
    tech_out += tech[6]
elif tech_in == "7":
    tech_out += tech[7]
elif tech_in == "8":
    tech_out += tech[8]
elif tech_in == "9":
    tech_out += tech[9]
elif tech_in == "10":
    tech_out += tech[10]
elif tech_in == "11":
    tech_out += tech[11]
elif tech_in == "12":
    tech_out += tech[12]
elif tech_in == "13":
    tech_out += tech[13]
elif tech_in == "14":
    tech_out += tech[14]
elif tech_in == "15":
    tech_out += tech[15]
else:
    print("falsche Eingabe")
    tech_out += "Fehler bei der Eingabe!"
    
print(tech_out)

print("\n------------------------------------------------\n")

print(f"{name}\n{port_out}\n{size_out}\n{atmo_out}\n{hydro_out}\n{pop_out}\n{gov_out}\n{just_out}\n{tech_out}")