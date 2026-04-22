while True: #Executa el codi en bucle
 primerNumero = float(input("Introdueix el primer número")) #Demanar el primer número amb el que es vol operar
 segonNumero = float(input("Introdueix el segon número")) #Demanar el segon número amb el que es vol operar
 Operacio = (input("Introdueix l'operació que vols fer (+,-,*,/,%):")) #Demanar la operació que es vol fer

 if Operacio == '+': #Si la operació és una suma
  resultat = primerNumero + segonNumero #Fes la suma dels dos números
 elif Operacio == '-': #Si la operació és una resta
  resultat = primerNumero - segonNumero #Fes la resta dels dos números
 elif Operacio == '*': #Si la operació és una multiplicació
  resultat = primerNumero * segonNumero #Fes la multiplicació dels dos números
 elif Operacio == '/': #Si la operació és una divisió
  resultat = primerNumero / segonNumero #Fes la divisió dels dos números
 elif Operacio == '%': #Si la operació és un %
  resultat = primerNumero % segonNumero #Fes la divisió i torna el residu
 else: #I sino
  resultat = "Introdueix una operació válida" #Demanar al usuari que introdueixi una operació válida
 print(resultat) #Mostrar per pantalla el valor de: resultat
 if resultat == "Introdueix una operació válida": #Si s'ha de demanar a l'usuari que introdueixi una operació válida
  break #Atura el bucle