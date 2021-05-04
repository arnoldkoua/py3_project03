"""Structure conditionnelle avancée - Exercice 01
Dans cet exercice, tu dois remettre la structure conditionnelle dans l'ordre !

Voici le texte qui doit être affiché selon les conditions :

Note plus petite que 3 : Sans commentaire...

Note supérieure ou égale à  3 et inférieure à  6 : Tu n'as rien compris !

Note supérieure ou égale à  7 et inférieure à  10 : Il faut tout revoir...

Note supérieure ou égale à  10 et inférieure à  14 : Peut mieux faire.

Note supérieure ou égale à  14 et inférieure à  18 : Bon travail !

Note supérieure ou égale à  18 et inférieure à 20 : Excellent !!

Note égale à  20 : C'est un sans faute !

Attention :

Tu ne dois pas modifier les conditions en tant que tel, juste l'ordre des if / elif.

N'enlève pas le print à la fin de l'exercice et ne modifie pas les 3 premières lignes."""

#Solution - Exercice 01

if Note < 3 :
    print("Sans commentaire...")
elif Note >= 3 and Note < 6 :
    print("Tu n'as rien compris !")
elif Note >= 7 and Note < 10 :
    print("Il faut tout revoir...")
elif Note >= 10 and Note < 14 :
    print("Peut mieux faire.")
elif Note >= 14 and Note < 18 :
    print("Bon travail !")
elif Note >= 18 and Note < 20 :
    print("Excellent !!")
else :
    print("C'est un sans faute !")