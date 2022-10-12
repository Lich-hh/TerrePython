while True:
    try:

        nombre = int(input( " Entrer un nombre : "))
        if nombre >= 2 and nombre % 2 != 0:
            print(" Le nombre est premier ")
            break
        elif nombre < 2:
            print(" 0 et 1 ne peuvent pas etre premier et les négatifs aussi !")
            break
        elif nombre > 2 and nombre % 2 == 0:
            print(" Ce nombre n'est pas premier ")
            break
        else:
            print(" 2 est un nombre entier ")
            break
    except ValueError:
        print(" Erreur lors de la saisi !!! , retaper un nombre svp :  ")

