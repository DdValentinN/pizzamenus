# PIZZA MENU PROGRAMME :

def afficher(collection,a_premiers_elements= -1):
    collection.sort( )
    c= collection
    if not a_premiers_elements == -1:
        c= collection[:a_premiers_elements]

    nombre_pizzas= len(collection)
    if nombre_pizzas == 0:
        print("AUCUNE PIZZA")
        return

    print(f"-------MENU DES PIZZAS: {nombre_pizzas} pizzas -------")
    for i in c:
        print(i)
    print()
    print(f"Première pizza de la collection : {collection[0]}")
    print(f"Dernière pizza : {collection[-1]}")

def nouvelle_pizza_user(collection) :
    p = input("Nouvelle pizza à ajouter :")
    if p.lower() in collection:
        print(f"ERREUR: La pizza {p} existe déjà ")
    else:
        collection.append(p)

pizzas = ["calzone", "4 fromages", "bolognaise", "saumon","hawaïenne"]
nouvelle_pizza_user(pizzas)
afficher(pizzas,)
