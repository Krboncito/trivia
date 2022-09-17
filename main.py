RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
MAGENTA="\033[35m"
RESET = "\033[39m"
iniciar_trivia = True
intentos=0
x=1
import time 
import random
puntaje = random.randint(0,10)
print("Bienvenido a mi trivia sobre historia del Perú")
print("en esta trivia pondrás a prueba tus conocimientos muy básicos y generales en este tema, pero ten cuidado algunas respuestas incorrectas pueden restarte puntos, ¡mucha suerte!")
time.sleep(1)
nombre=input("ingresa tu nombre: ")
print("hola ",nombre)
print("escribe la alternativa correcta y presiona enter")

time.sleep(1)
print("cargando...")
for x in range(1,6,1):
  print(x)
  time.sleep(1)

print("tienes 0 puntos")
while iniciar_trivia==True:
  intentos+=1
  puntaje=0
  print("\n intento numero: ",intentos)
  input("presiona enter para continuar")

  print(BLUE+"1. ¿En qué año se declaró la independencia del Perú?\n"+RESET)
  time.sleep(1)

  print("a)1879")
  print("b)1789")
  print("c)1821")
  print("d)1914")

  respuesta_1 = input("\n Ingrese su respuesta: ")
  time.sleep(1)
  while respuesta_1 not in ("a","b","c","d"):
   respuesta_1 = input("Debes escoger a,b,c o d.Ingresa nuevamente tu respuesta:")
  if respuesta_1 == "a":
         print(RED+"incorrecto"+RESET,nombre,"ese año comenzó la guerra del pacífico")
         puntaje= puntaje-1
  elif respuesta_1 == "b":
         print(RED+"incorrecto"+RESET,nombre,"ese año inició la revolución francesa")
         puntaje= puntaje-2
  elif respuesta_1 == "d":
         print(RED+"incorrecto"+RESET,nombre,"ese año comenzó la primera guerra mundial")
  else:
   print(GREEN+"respuesta correcta"+RESET,nombre)
  if respuesta_1== "c":
   puntaje+=10
  time.sleep(1)

  print(BLUE+"\n 2.¿Cual de los siguientes personajes es considerado el caballero de los mares?"+RESET)
  time.sleep(1)
  print("a) José Olaya")
  print("b) Ramón Castilla")
  print("c) Evo Morales")
  print("d) Miguel Grau") 

  respuesta_2 = input("\n Ingresa tu respuesta: ")
  time.sleep(1)

  while respuesta_2 not in ("a","b","c","d"):
   respuesta_2 = input("Debes escoger a,b,c o d .Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "a":
         print(RED+"incorrecto"+RESET,nombre,"él fue un mártir pero no es él")
         puntaje=puntaje-2
  elif respuesta_2 == "b":
         print(RED+"incorrecto"+RESET,nombre,"él fue un presidente peruano")
  elif respuesta_2 == "c":
         print(RED+"incorrecto"+RESET,nombre,"él fue un presidente boliviano")
         puntaje=puntaje-2
  else:
   print(GREEN+"respuesta correcta"+RESET,nombre)
  if respuesta_2 == "d":
   puntaje=puntaje*2
  time.sleep(1)
  
  print(BLUE+"\n 3. ¿Quién fue el último inca?"+RESET)
  time.sleep(1)
  print("a) Qin Shi Huang")
  print("b) Pacachutec")
  print("c) Atahualpa")
  print("d) Tzilacatsin")

  respuesta_3 = input("\n Ingresa tu respuesta: ")
  time.sleep(1)

  while respuesta_3 not in ("a","b","c","d"):
   respuesta_3 = input("Debes escoger a,b,c o d .Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
         print(RED+"incorrecto"+RESET,nombre,"él fue un emperador chino")
         puntaje=puntaje-1
  elif respuesta_3 == "b":
         print(RED+"incorrecto"+RESET,nombre,"él fue un inca pero no fue el último")
  elif respuesta_3 == "d":
         print(RED+"incorrecto"+RESET,nombre,"él fue un guerrero jaguar mexicano")
         puntaje=puntaje-1
  else:
   print(GREEN+"respuesta correcta"+RESET,nombre)
  if respuesta_3 == "c":
   puntaje+=10
  
  time.sleep(1)
  print(BLUE+"\n 4.¿Cuál es el nombre del dios que adoraban los incas?"+RESET)
  print("a) Shiva")
  print("b) Susano no Mikoto")
  print("c) Inti")
  print("d) Belzebú")

  respuesta_4 = input("\n Ingresa tu respuesta: ")
  time.sleep(1)

  while respuesta_4 not in ("a","b","c","d"):
   respuesta_4 = input("Debes escoger a,b,c o d .Ingresa nuevamente tu respuesta: ")

  if respuesta_4 == "a":
         print(RED+"incorrecto"+RESET,nombre,"él es el dios de la destrucción hindú")
         puntaje = puntaje-1
  elif respuesta_4 == "b":
         print(RED+"incorrecto¡¡"+RESET,nombre,"él es el dios de las tormentas japonés")
         puntaje=puntaje-2      
  elif respuesta_4 == "d":
         print(RED+"incorrecto"+RESET,nombre,"él es un dios demonio hebraico")
  else:
   print(GREEN+"respuesta correcta"+RESET,nombre)
  if respuesta_4 == "c":
   puntaje+=10
  time.sleep(1)

  print(BLUE+"\n 5. ¿Quien héroe nacional dijo la siguiente frase:No me rendiré hasta quemar el último cartucho?"+RESET)

  time.sleep(1)
  print("a) Francisco Bolognesi")
  print("b) Simo Haya")
  print("c) Alan García")
  print("d) Nicola Tesla")
  respuesta_5 = input("\n Ingresa tu respuesta: ")

  time.sleep(1)
  while respuesta_5 not in ("a","b","c","d"):
   respuesta_5 = input("Debes escoger a,b,c o d .Ingresa nuevamente tu respuesta: ")
  time.sleep(1)
  
  if respuesta_5 =="c":
   print(RED+"incorrecto¡"+RESET,nombre,"él fue un presidente peruano")
   puntaje=puntaje-3
  elif respuesta_5 == "b":
        print(RED+"incorrecto"+RESET,nombre,"él fue un francotirador finlandés")
  elif respuesta_5 == "d":
         print(RED+"incorrecto¡¡"+RESET,nombre,"él fue un ingeniero e inventor croata")
         puntaje = puntaje-1 
  else:
   print(GREEN+"respuesta correcta"+RESET,nombre)
  if respuesta_5 == "a":
   puntaje=puntaje*2
  time.sleep(2)
  print(MAGENTA+"Gracias por jugar mi trivia",nombre,"tienes",puntaje,"puntos!"+RESET)
  time.sleep(1)

  print("\n ¿Deseas repetir la trivia nuevamente?")
  repetir_trivia=input("Escribe si para repetir o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":
   time.sleep(1)
  print(MAGENTA+"Gracias",nombre,"por jugar mi trivia , ¡hasta pronto!"+RESET)
  iniciar_trivia = False
