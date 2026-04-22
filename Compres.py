DNI = input("Quin es el teu DNI?") #Demana al usuari el seu DNI
preu_inicial = float(input("Quant et va costar l'article?")) #Demana al usuari el preu del article
descompte = float(input("Quin es el descompte en aquest article?")) #Demana al usuari el descompte del article
IVA = float(input("Quin es l'IVA en aquest article?")) #Demana al usuari l'IVA del article

preu_amb_descompte = preu_inicial - (preu_inicial * descompte / 100) #Calcula el preu amb descompte
preu_final = preu_amb_descompte + (preu_amb_descompte * IVA / 100) #Calcula el preu final sumant l'IVA

print(DNI) #Mostra per pantalla el DNI del usuari
print(preu_final) #Mostra per pantalla el preu final del article