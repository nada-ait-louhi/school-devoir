#devoir numero 2 - python pour la sciences des donnees
#professeure  :    Sanae KHALI ISSA

def menu():
    print("Menu général :")
    print("(1) Ajouter les produits")
    print("(2) Calculer le prix total à payer par le client")
    print("(3) Afficher la facture totale du client")
    print("(4) Modifier les informations d'un produit")
    print("(5) Supprimer un produit")
    ch=int(input("Entrer votre choix :"))
    return(ch)

panier={}

choix=0
while choix!=5:
    choix=menu()

    # 1 - Ajouter le code, le nom, le prix et la quantité pour les N produits

    if choix==1:
        N=int(input("Entrer le nombre des produits (N) : "))
        for i in range(N):
            print("Produit", i+1)
            code=input("Code du produit = ")
            nom=input("Nom du produit = ")
            prix=float(input("Prix unitaire = "))
            qte=int(input("Quantité = "))
            panier[code]=[nom, prix, qte]
        print(panier)


    # 2 - Calculer et afficher le prix total

    elif choix==2:
        if bool(panier)==False:
            print("Panier vide !")
        else:
            total=0
            for x,y in panier.items():
                total=total + y[1]*y[2]
            print("Prix total à payer par le client : ", total)

    # 3 - Afficher la facture par ordre alphabétique selon le code

    elif choix==3:
        if bool(panier)==False:
            print("Aucun produit acheté")
        else:
            total=0
            for x,y in panier.items():
                total=total + y[1]*y[2]
            print("{:<15} {:<15} {:<15} {:<15}".format("Code du produit","Nom du produit","Quantité","Prix Unitaire"))
            for code in sorted(panier.keys()):
                print("{:<15} {:<15} {:<15} {:<15}".format(code, panier[code][0], panier[code][2], panier[code][1]))
            print("\nPrix total : ", total)


     # 4 - Modifier code, nom, prix, quantité

    elif choix==4:
        code=input("Entrer le code du produit à modifier : ")
        if panier.get(code)==None:
            print("Element introuvable")
        else:
            print("1. modifier le code")
            print("2. modifier le nom")
            print("3. modifier le prix")
            print("4. modifier la quantité")
            c=int(input("Votre choix : "))
            if c==1:
                nouveau_code=input("Nouveau code = ")
                panier[nouveau_code]=panier.pop(code)
                print("Code modifié avec sucées")
            elif c==2:
                panier[code][0]=input("Nouveau nom = ")
                print("Nom modifié avec sucées")
            elif c==3:
                panier[code][1]=float(input("Nouveau prix = "))
                print("Prix modifié avec sucées")
            elif c==4:
                panier[code][2]=int(input("Nouvelle quantité = "))
                print("Quantité modifiée avec sucées")

    # 5 - Supprimer un produit

    elif choix==5:
        code=input("Entrer le code du produit à supprimer : ")
        if panier.get(code)==None:
            print("Element introuvable")
        else:
            panier.pop(code)
            print("Le produit a été supprimé avec succés")
            

    
