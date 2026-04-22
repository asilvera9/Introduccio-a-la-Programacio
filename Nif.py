DNI = int(input("Quin es el teu DNI?")) #Demana al usuari el seu DNI
residuDNI = DNI - int(DNI / 23) * 23 #Calcula el residu del DNI per a poder obtenir la lletra
modul23 = "TRWAGMYFPDXBNJZSQVHLCKE" #Afegim el modul23 com a variable
print (str(DNI) + modul23[residuDNI]) #Mostrem per pantalla el DNI amb la seva lletra, agafant-la de la variable modul23