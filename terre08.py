while True:
    try:

        nombre = int(input(" Entre le nombre : "))
        puissance = int(input(" Entre sa puissance : "))
        if puissance >= 0 :
            print(pow(nombre,puissance))

        else:
         print(" Erreur l'exposant ne peut pas etre négatif ! ")

        break

    except ValueError:
        print(" Erreur , mauvais arguments , entrer seulement des nombres ! ")


