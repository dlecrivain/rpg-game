from dependencies import *
from quest import *

quest_number = 0

while True:
    choice_race = input('Selectionner une race:\n'
    '1: Orc \n' \
    '2: Elfe \n'
    'q: quitter le jeu \n\n')

    if choice_race.lower() in ['1']:
        clear()
        print("Vous avez choisi la race Orc\n\n")
        race = 'Orc'
        from races.orc import *
        break
    elif choice_race.lower() in ['2']:
        clear()
        print("Vous avez choisi la race Elfe\n\n")
        race = 'Elfe'
        from races.elfe import *
        break
    elif choice_race.lower() in ['q']:
        exit()
    else:
        print("Not match")

tete = "non equipé"
corps = "non equipé"
bras = "non equipé"
jambes = "non equipé"
pieds = "non equipé"
equip_1 = "non equipé"
equip_2 = "non equipé"


def capacites():
    print("\n###########################\n" \
    "Race: " +race+"\n"\
    "PV: " +str(pv_actuel)+"/"+str(pv_max)+"\n"\
    "Attaque: " +str(attaque)+ "\n"\
    "Defense: " +str(defense)+ "\n"\
    "Vitesse: " +str(vitesse)+ "\n"\
    "###########################\n")

equipements = "\n##########################\n" \
"Tete: " +tete+ "\n" \
"Corps: " +corps+ "\n" \
"Bras: " +bras+ "\n" \
"Jambes: " +jambes+ "\n" \
"Pieds: " +pieds+ "\n" \
"Equipement divers 1: " +equip_1+ "\n" \
"Equipement divers 2: " +equip_2+ "\n" \
"###########################\n"


while True:
    choice = input('Menu:\n'
                    'c: caracteristiques du personnage \n'
                    'e: equipement du personnage \n'
                    'a: attaquer \n'
                    'go: aller à l\'aventure \n'
                    'q: quitter le jeu \n\n')
    if choice.lower() in ['c']:
        clear()
        while True:
            capacites()
            choice_capacites = input('Menu:\n'
                    'l: augmenter d\'un niveau \n' \
                    'p: utiliser un parchemin \n'
                    'r: retour au menu principal \n\n')
            if choice_capacites.lower() in ['l']:
                clear()
                print("Vous n\'avez pas encore les droits de niveau\n\n")
            elif choice_capacites.lower() in ['p']:
                clear()
                print("Bloc de parchemin\n\n")
            elif choice_capacites.lower() in ['r']:
                print("Retour au menu principal")
                sleep(0.5)
                clear()
                break
            else:
                print("Not match")
    elif choice.lower() in ['e']:
        clear()
        while True:
            print(equipements)
            choice_equipements = input('Menu:\n'
                    'e: equiper \n' \
                    'r: retour au menu principal \n\n')
            if choice_equipements.lower() in ['e']:
                clear()
                print("Quel endroit equiper ?\n\n")
                while True:
                    choice_equipements_part = input(
                    '1: Tete (' +tete+ ')\n' \
                    '2: Corps (' +corps+ ')\n' \
                    '3: Bras (' +bras+ ')\n' \
                    '4: Jambes (' +jambes+ ')\n' \
                    '5: Pieds (' +pieds+ ')\n' \
                    '6: Equipement divers 1 (' +equip_1+ ')\n' \
                    '7: Equipement divers 2 (' +equip_2+ ')\n' \
                    '0: retour au menu equipement \n\n')
                    if choice_equipements_part.lower() in ['1']:
                        clear()
                        print("Vous avez choisi la tete\n\n")
                    elif choice_equipements_part.lower() in ['2']:
                        clear()
                        print("Vous avez choisi le corps\n\n")
                    elif choice_equipements_part.lower() in ['3']:
                        clear()
                        print("Vous avez choisi le bras\n\n")
                    elif choice_equipements_part.lower() in ['4']:
                        clear()
                        print("Vous avez choisi les jambes\n\n")
                    elif choice_equipements_part.lower() in ['5']:
                        clear()
                        print("Vous avez choisi les pieds\n\n")
                    elif choice_equipements_part.lower() in ['6']:
                        clear()
                        print("Vous avez choisi l\'equipement divers 1\n\n")
                    elif choice_equipements_part.lower() in ['7']:
                        clear()
                        print("Vous avez choisi l\'equipement divers 2\n\n")   
                    elif choice_equipements_part.lower() in ['0']:
                        print("Retour au menu equipement")
                        sleep(0.5)
                        clear()
                        break
                    else:
                        print("Not match\n\n")
            elif choice_equipements.lower() in ['r']:
                print("Retour au menu principal")
                sleep(0.5)
                clear()
                break
            else:
                print("Not match")
    elif choice.lower() in ['a']:
        attaque = 50
        pv_actuel -= attaque
        print("Le personnage s'est pris "+str(attaque)+" points dans la gueule")
        print("il reste "+str(pv_actuel)+"/"+str(pv_max))
        sleep(2)
        if pv_actuel <= 0 :
            print("Le personnage meurt")
            break
        clear()
    elif choice.lower() in ['go']:
        print("l'aventure commence !")
        #quest(quest_number)
        number = quest(int(quest_number))
        #quest_number = int(quest_number)
        print(number)
        input('valeur number')
        quest_number = number
        clear()
    elif choice.lower() in ['q', 'exit', 'quit']:
        print("Le jeu se ferme")
        break
    else:
        print("Not match")
