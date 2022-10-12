"""pair_ou_impair = int(input(" Entrez un nombre :"))
if pair_ou_impair % 2 == 0:
    print(" Nombre pair")
elif pair_ou_impair % 2 != 0:
    print(" Nombre Impair")
else :
    print(erreur)
    """

while True:
    try:
        pair_ou_impair = int(input(" Entrer un nombre "))
        if pair_ou_impair %2 ==0:
            print(" Nombre pair ")
        elif pair_ou_impair % 2 != 0:
            print(" Nombre impair ")
            break
    except ValueError:
        print(" Oula tu n'as pas compros la consigne !")

