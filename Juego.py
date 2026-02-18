print('Adivina adivinador...\n' 
'Tengo un número entre el 1 al 100\n'
'Quieres adivinar?')
import random
Seguir = input('Para comenzar ingresa "Y", para salir "N": ')
Rango = list(range(1, 101))

while Seguir == 'Y' or Seguir == 'y':
   Dificultad = int(input('Ingresa nivel de dificultad:\n'
         '1.Fácil: Tienes 10 oportunidades\n'
         '2.Medio: Tienes 5 oportunidades y 1 pista\n' 
         '3.Dificil:Tienes 3 oportunidades y 2 pistas\n' \
         'Tu elección: '))
   Adivinar = random.choice(Rango)
   if Dificultad == 1:
    veces = 10

   elif Dificultad == 2:
    veces = 5
    if Adivinar % 2 == 0:
      print('Pista 1: El número es par')
    else:
       print('Pista 1: El número es impar')

   elif Dificultad == 3:
    veces = 3
    if Adivinar % 2 == 0:
      print('Pista 1: El número es par')
    else:
       print('Pista 1: El número es impar')

    if Adivinar < 50:
       print('Pista 2: Está entre la primera mitad')
    else:
       print('Pista 2: Está entre la segunda imera mitad')
   else:
    print('Ingrese opción válida')
    continue
   for i in range(veces):
     Intento = int(input('Introduce tu intento de adivinanza: '))
     if Intento == Adivinar:
        print('Adivinaste waos!!!!')
        break
     if Intento != Adivinar and Intento < Adivinar:
      print('Incorrecto! un poquito mayor...')
     elif Intento != Adivinar and Intento > Adivinar:
       print('Incorrecto! un poquito menor...')
   print(f'Perdiste cuaaaaaa\n'
      f'El número era {Adivinar}')
   Seguir = input('¿Quieres jugar otra vez? (Y/N): ')
   
             
   if Seguir == 'N' or Seguir == 'n':
       print('Chaoooo')
       break
   #holA 