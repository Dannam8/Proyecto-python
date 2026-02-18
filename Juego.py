print('Adivina adivinador...\n' 
'Tengo un número entre el 1 al 100\n'
'Quieres adivinar?')
import random
partidas_ganadas = 0
total_intentos = 0
while True:
   Seguir = input('Para comenzar ingresa "Y", para salir "N": ')
   if Seguir in ['Y', 'y', 'N', 'n']:
      total_intentos += 1
      break
   else:
      print('Ingrese opción válida')
   
Rango = list(range(1, 101))

while Seguir == 'Y' or Seguir == 'y':
   Adivinar = random.choice(Rango)
   while True:
       try:
          Dificultad = int(input('Ingresa nivel de dificultad:\n'
         '1.Fácil: Tienes 10 oportunidades\n'
         '2.Medio: Tienes 5 oportunidades y 1 pista\n' 
         '3.Dificil: Tienes 3 oportunidades y 2 pistas\n'
         'Tu elección: '))
          if Dificultad == 1:
             veces = 10
             break
          elif Dificultad == 2: 
             veces = 5
             if Adivinar % 2 == 0:
                print('Pista 1: El número es par')
             else:
               print('Pista 1: El número es impar')
             break
          elif Dificultad ==3:
              veces = 3
              if Adivinar % 2 == 0:
                print('Pista 1: El número es par')
              else: 
                print('Pista 1: El número es impar')
              if Adivinar < 50:
                   print('Pista 2: Está entre la primera mitad')
              else: 
                   print('Pista 2: Está entre la segunda mitad')
              break
          else:  
             print('Ingrese opción válida')
       except ValueError:
          print('Ingresa un número')
      
   
   i = 0
   while i < veces:
     Intento = int(input('Introduce tu intento de adivinanza: '))
     Intento_restante = veces - 1
     if Intento == Adivinar:
        print('Adivinaste waos!!!!')
        partidas_ganadas += 1
        break
     
     if Intento < Adivinar:
      print('Incorrecto! un poquito mayor...\n' \
      f'Te quedan {veces - (i+1)} intentos')
     else:
       print('Incorrecto! un poquito menor...\n' \
      f'Te quedan {veces - (i+1)} intentos')
     i += 1

     if i == veces:
       print(f'Perdiste cuaaaaaa\n'
             f'El número era {Adivinar}')
       
   print('Tus estadísticas:\n'
   f'Total partidas jugadas: {total_intentos}\n'
   f'Total partidas ganadas: {partidas_ganadas}')

   Seguir = input('¿Quieres jugar otra vez? (Y/N): ')  
   if Seguir == 'N' or Seguir == 'n':
       print('Chaoooo')
       break