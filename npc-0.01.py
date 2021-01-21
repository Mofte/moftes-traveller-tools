#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

divider = "\n" + "-"*48 + "\n"

fertigkeiten = ["Astrogation", 
"Athletik (Koordination)", 
"Athletik (Durchhaltevermögen)", 
"Athletik (Kraft)", 
"Athletik (Fliegen)", 
"Aufklärung", 
"Biowissenschaften (Biologie)", 
"Biowissenschaften (Kybernetik)", 
"Biowissenschaften (Genetik)", 
"Biowissenschaften (Psionikologie)", 
"Bordschütze (Geschütztürme)", 
"Bordschütze (Ortillerie)", 
"Bordschütze (Schilde)", 
"Bordschütze (Schwere Bordgeschütze)", 
"Computer", 
"Diplomatie", 
"Ermitteln", 
"Fahrer (Grabungsfahrzeuge)", 
"Fahrer (Kettenfahrzeuge)", 
"Fahrer (Radfahrzeuge)", 
"Fernsteuerung", 
"Flieger (Grav)", 
"Flieger (Rotor)", 
"Flieger (Tragflächen)", 
"Führung", 
"Geselligkeit", 
"Glücksspiel", 
"Handeln", 
"Handfeuerwaffen (Projektilgewehr)", 
"Handfeuerwaffen (Projektilpistole)", 
"Handfeuerwaffen (Schrotflinte)", 
"Handfeuerwaffen (Energiegewehr)", 
"Handfeuerwaffen (Energiepistole)", 
"Handwerk (Biologie)", 
"Handwerk (Bauingenieruswesen)", 
"Handwerk (Weltraumarchitektur)", 
"Handwerk (Hydroponik)", 
"Handwerk (Polymere)", 
"Ingenieur (M-Antrieb)", 
"Ingenieur (S-Antrieb)", 
"Ingenieur (Elektronik)", 
"Ingenieur (Lebenserhaltung)", 
"Ingenieur (Reaktor)", 
"Kampfanzug", 
"Kommunikation", 
"Kunst (Schauspieler)", 
"Kunst (Tanz)", 
"Kunst (Holographie)", 
"Kunst (Instrument)", 
"Kunst (Schriftsteller)", 
"Mechanik", 
"Medizin", 
"Milieu", 
"Multitalent", 
"Nahkampf (Unbewaffnet)", 
"Nahkampf (Klingenwaffen)", 
"Nahkampf (Stumpfe Waffen)", 
"Nahkampf (Natürliche Waffen)", 
"Navigation", 
"Null-G", 
"Physikalische Wissenschaften (Physik)", 
"Physikalische Wissenschaften (Chemie)", 
"Physikalische Wissenschaften (Elektronik)", 
"Pilot  (Kleine Schiffe)", 
"Pilot (Raumschiffe)", 
"Pilot (Große Raumschiffe)", 
"Raumanzug", 
"Rechtswissenschaften", 
"Schwere Waffen (Werfer)", 
"Schwere Waffen (Tragbare Artillerie)", 
"Schwere Waffen (Feldartillerie)", 
"Seefahrer (Segeln)", 
"Seefahrer (U-Boote)", 
"Seefahrer (Ozeankreuzer)", 
"Seefahrer (Motorboote)", 
"Sensoren", 
"Sozialwissenschaften (Archäologie)", 
"Sozialwissenschaften (Wirtschaftswissenschaften)", 
"Sozialwissenschaften (Geschichte)", 
"Sozialwissenschaften (Linguistik)", 
"Sozialwissenschaften (Philosophie)", 
"Sozialwissenschaften (Psychologie)", 
"Sozialwissenschaften (Sophontologie)", 
"Sprachen (Anglisch)", 
"Sprachen (Vilani)", 
"Sprachen (Zdetl)", 
"Sprachen (Oynprith)", 
"Sprengstoff", 
"Steward", 
"Taktik (planetar)", 
"Taktik (interplanetar)", 
"Täuschung", 
"Tiere (Reiten)", 
"Tiere (Tierarzt)", 
"Tiere (Abrichten)", 
"Tiere (Landwirtschaft)", 
"Überleben", 
"Überreden", 
"Verdeckte Operation", 
"Verwaltung", 
"Weltraumwissenschaften (Planetologie)", 
"Weltraumwissenschaften (Robotik)", 
"Weltraumwissenschaften (Xenologie)",]

nkwaffen = ["unbewaffnet", "improvisierte Waffe", "Keule", "Dolch", "Schild", "Stab", "Klinge", "Breitschwert", "Entermesser", "Rapier", "Betäubungsstock"]

fkwaffen = ["Antike Pistole", "Revolver", "Automatikpistole", "Kurzlaufrevolver", "Körperpistole", "Gauss-Pistole", "Antikes Gewehr", "Gewehr", "Automatikgewehr", "Sturmgewehr", "Erweitertes Gefechtsgewehr", "Gauss-Gewehr", "Schrotflinte", "Laserpistole", "Betäubungswaffe", "Laserkarabiner", "Lasergewehr", "Plasmagewehr"]

def dice(sides):
    sides = int(sides)
    result = random.randint(1,sides)
    return result

def d6x2():
    result = (dice(6) + dice(6))
    return result

def attr_mod(attribut):
    if attribut == 0:
        mod = "(-3)"
    elif attribut >= 1 and attribut <= 2:
        mod = "(-2)"
    elif attribut >= 3 and attribut <= 5:
        mod = "(-1)"
    elif attribut >= 6 and attribut <= 8:
        mod = "(+0)"
    elif attribut >= 9 and attribut <= 11:
        mod = "(+1)"
    elif attribut >= 12 and attribut <= 14:
        mod = "(+2)"
    elif attribut == 15:
        mod = "(+3)"
    return mod


print(divider)

print("Ein simpler NPC-Generator für Mongoose Traveller 1Ed.")

print(divider)

name = input("Bitte den Namen des NPC eingeben: ")
strength = d6x2()
dexterity = d6x2()
endurance = d6x2()
intellect = d6x2()
education = d6x2()
social = d6x2()

print(divider)

if social == 11:
    print("Ritter " + name)
elif social == 12:
    print("Baron " + name)
elif social == 13:
    print("Marquis " + name)
elif social == 14:
    print("Graf " + name)
elif social >= 15:
    print("Herzog " + name)
else:
    print(name)

divider_npc = ("\n" + "-" * len(name) + "\n")

print(divider_npc)



print("Attribute\n")

print(f"Stärke: {strength} {attr_mod(strength)}")
print(f"Geschick: {dexterity} {attr_mod(dexterity)}")
print(f"Ausdauer: {endurance} {attr_mod(endurance)}")
print(f"Intelligenz: {intellect} {attr_mod(intellect)}")
print(f"Bildung: {education} {attr_mod(education)}")
print(f"Sozialstatus: {social} {attr_mod(social)}")

print(divider_npc)

print("Fertigkeiten\n")

print(random.choice(fertigkeiten))
print(random.choice(fertigkeiten))
print(random.choice(fertigkeiten))
print(random.choice(fertigkeiten))
print(random.choice(fertigkeiten))

print(divider_npc)

print("Bewaffnung\n")

print(random.choice(nkwaffen))
print(random.choice(fkwaffen))

print(divider)