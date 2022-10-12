while True:
	try:
		import math



		nombre = int(input(" Entrer un nombre : "))
		print("Voici sa racine carré : ", math.sqrt(nombre))

		break

	except ValueError:
		print(" Erreur lors de la saisi , entrer un nombre ! ")



