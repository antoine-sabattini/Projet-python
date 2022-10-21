# import random & re
import random
import re
running = True

# prints a random value from the list
file = open("dico_france.txt", encoding = "ISO-8859-1")
#transformer le fichier texte en tableau
tableau = file.readlines()
wordtoguess = (random.choice(tableau))
#mesure de la longueur du mot
length = len(wordtoguess)


#boucle affichant le nombre de lettres du mot
display_blank = ''

for l in wordtoguess:
    display_blank += "_ "
li = list(display_blank.split(" "))
print(li)
print(display_blank)
while running == True:

    print('le mot contient',length,'lettres')
    #input de la réponse
    guess = input()
    #debug mot a deviner
    #print(wordtoguess)

    #les lettres présentes
    letterlist = list(wordtoguess)
    print(letterlist)
    #comparer l'input aux lettres présentes
    if guess in letterlist:
        for letterguess in letterlist:
            print(letterguess)
            if guess == letterguess:
                #debug

#\n = faire un saut de ligne
#!if input dans le mot a trouvé & stocké lettre trouvé liste!
#sauvegarder l'index de la lettre dans un tableau/liste
#diflvl = input("Choisissez votre niveau de difficulté : 1-Facile, 2-Moyen, 3-Expert")
#if diflvl == '1':
#    print ('niveau : facile, 7 essais')
#elif diflvl == '2':
#    print('niveau : medium, 5 essais')
#elif diflvl == '3':
#    print('niveau : expert, 3 essais')
