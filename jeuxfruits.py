def jeu_fruits(a_trouver):
    essais = 3
     
    while essais > 0:
        proposition = input("Quel fruit choisis-tu ?")

        if proposition == a_trouver:
            print("Bravo")
            return
        else:
            print("Erreur")
            essais = essais - 1
            print(essais) 

    print("Perdu, le mot était ", a_trouver)

   
    


fruits = ["pomme","banane","abricot","fraise"]
a_trouver = fruits[1]

jeu_fruits("a_trouver")