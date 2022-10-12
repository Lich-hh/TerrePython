while True:
    try:
        a = int(input(" Entrer un premier nombre "))
        b = int(input(" Entrer un second nombre "))
        division = a//b
        reste = a % b
        if a > b:
            print(division)
            print(reste)
        elif a or b == 0:
            print(" On ne peut pas diviser par 0")
            break
        else:
            print(" Erreur !")
        break
    except ValueError:
        print("t'es hors piste")
        break

