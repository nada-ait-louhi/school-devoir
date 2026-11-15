# Devoir N1 - Convertisseur de bases
# Licence Ingénierie des données - Python pour la science des données
# Professeure: Sanae KHALI ISSA

def tester_nombre(nombre_str, base):
    """Vérifie si nombre appartient à la base"""
    nombre_str = nombre_str.strip().upper()
    if nombre_str == "":
        return False

    if base == 2:
        autorise = "01"
    elif base == 8:
        autorise = "01234567"
    elif base == 10:
        autorise = "0123456789"
    elif base == 16:
        autorise = "0123456789ABCDEF"
    else:
        return False

    for c in nombre_str:
        if c not in autorise:
            return False
    return True

def conversion_to_decimal(nombre_str, base):
    """Binaire/Octal/Hexa -> Décimal"""
    nombre_str = nombre_str.strip().upper()
    valeurs_hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    decimal = 0
    puissance = len(nombre_str) - 1
    
    for char in nombre_str:
        if char in valeurs_hexa:
            chiffre = valeurs_hexa[char]
        else:
            chiffre = int(char)
        decimal += chiffre * (base ** puissance)
        puissance -= 1
    
    return decimal

def conversion_from_decimal(nombre_decimal, base):
    """Décimal -> Binaire/Octal/Hexa (sans bin/oct/hex)"""
    if nombre_decimal == 0:
        return "0"
    
    caracteres = "0123456789ABCDEF"
    resultat = ""
    n = nombre_decimal
    
    while n > 0:
        reste = n % base
        resultat = caracteres[reste] + resultat
        n = n // base
    
    return resultat

def menu():
    while True:
        print("\nMenu principal")
        print("-" * 30)
        print("(1) Conversion décimale => binaire")
        print("(2) Conversion décimale => octale")
        print("(3) Conversion décimale => héxadécimale")
        print("(4) Conversion binaire => décimale")
        print("(5) Conversion octale => décimale")
        print("(6) Conversion héxadécimale => décimale")
        print("(7) Quitter")
        
        choix = input("Votre choix: ").strip()
        
        if choix == "7":
            print("Au revoir!")
            break
        
        # Décimal vers autre
        if choix in ["1", "2", "3"]:
            nombre = input("Entrez le nombre décimal: ").strip()
            if not tester_nombre(nombre, 10):
                print("Erreur: nombre décimal invalide!")
                continue
            nombre = int(nombre)
            if choix == "1":
                print(f"{nombre})10 = {conversion_from_decimal(nombre, 2)})2")
            elif choix == "2":
                print(f"{nombre})10 = {conversion_from_decimal(nombre, 8)})8")
            else:
                print(f"{nombre})10 = {conversion_from_decimal(nombre, 16)})16")
        
        # Binaire vers décimal
        elif choix == "4":
            nombre = input("Entrez le nombre binaire: ").strip()
            if not tester_nombre(nombre, 2):
                print("Erreur: binaire invalide! seulement 0 et 1")
                continue
            print(f"{nombre})2 = {conversion_to_decimal(nombre, 2)})10")
        
        # Octal vers décimal
        elif choix == "5":
            nombre = input("Entrez le nombre octal: ").strip()
            if not tester_nombre(nombre, 8):
                print("Erreur: octal invalide! seulement 0-7")
                continue
            print(f"{nombre})8 = {conversion_to_decimal(nombre, 8)})10")
        
        # Hexa vers décimal
        elif choix == "6":
            nombre = input("Entrez le nombre héxadécimal: ").strip()
            if not tester_nombre(nombre, 16):
                print("Erreur: héxadécimal invalide! 0-9 et A-F")
                continue
            print(f"{nombre})16 = {conversion_to_decimal(nombre, 16)})10")
        
        else:
            print("Choix invalide! Entre 1 et 7")

# Lancement du programme
menu()
