import random #Genera un número aleatori
numeroAleatori = int(random.randrange(1,11)) #Aquest serà un número entre el 1 i el 10
numeroIntents = 3 #El número d'intents a l'inici es 3

while True: #Bucle Infinit
 numeroResposta = int(input("Adivina el número")) #Demana a l'usuari que endevini el número
 numeroIntents -= 1 #Per cada resposta resta 1 al número d'intents
 if numeroResposta < numeroAleatori: #Si la resposta és més petita que el número aleatori
  print("El número és més gran") #Mostra per pantalla que "El número és més gran"
 elif numeroResposta > numeroAleatori: #Si la resposta és més gran que el número aleatori
  print("El número és més petit") #Mostra per pantalla que "El número és més petit"
 elif numeroResposta == numeroAleatori: #Si la resposta és igual que elnúmero aleatori
  print("Has guanyat, el número era:", numeroAleatori) #Mostra per pantalla que el usuari ha guanyat i quin era el número aleatori
  break #Una vegada l'usuari hagi guanyat trenca el bucle
 if numeroIntents == 0: #I si el número d'intents és 0
  print("Has perdut, el número era:", numeroAleatori) #Mostra per pantalla que l'usuari ha perdut i quin era el número aleatori
  break #Una vegada l'usuari hagi perdut trenca el bucle