import random
def saludar_e_instrucciones(saludo: str, instrucciones: str):
   print(saludo)
   print(instrucciones)


def ingresar_si_o_no(pregunta_y_or_n: str):
   while True:
      seguir = input(pregunta_y_or_n)
      if seguir in ['Y', 'y', 'N', 'n']:
       break
      else: 
         print('Ingrese opción válida')
   return seguir

def preguntar_comenzar():
   Seguir = ingresar_si_o_no('Para comenzar ingresa "Y", para salir "N": ')

   
def elegir_dificultad(mensaje_dificultad_1_2_3: str):
   while True:
      Rango = list(range(1, 101))
      Adivinar = random.choice(Rango)
      Dificultad = input(mensaje_dificultad_1_2_3)
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
   return veces, Adivinar



def iniciar_juego(veces, Adivinar):
   i = 0
   total_intentos = 1
   partidas_ganadas = 0
   while i < veces:
      try:
         Intento = int(input('Introduce tu intento de adivinanza: '))
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
      except ValueError:
         print('Ingrese un número válido: ')
       
   print('Tus estadísticas:\n'
   f'Total partidas jugadas: {total_intentos}\n'
   f'Total partidas ganadas: {partidas_ganadas}')

def preguntar_jugar_nuevo_juego():
   Seguir = ingresar_si_o_no('¿Quieres jugar otra vez? (Y/N): ')
   if Seguir == 'Y' or Seguir == 'y':
      total_intentos += 1

   if Seguir == 'N' or Seguir == 'n':
      print('Chaoooo')
   return Seguir, total_intentos







partidas_ganadas = 0
total_intentos = 1
print('Adivina adivinador...\n' 
'Tengo un número entre el 1 al 100\n'
'Quieres adivinar?')
Seguir = ingresar_si_o_no('Para comenzar ingresa "Y", para salir "N": ')
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
     try:
         Intento = int(input('Introduce tu intento de adivinanza: '))
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
     except ValueError:
        print('Ingrese un número válido: ')
       
   print('Tus estadísticas:\n'
   f'Total partidas jugadas: {total_intentos}\n'
   f'Total partidas ganadas: {partidas_ganadas}')

   Seguir = ingresar_si_o_no('¿Quieres jugar otra vez? (Y/N): ')
   if Seguir == 'Y' or Seguir == 'y':
      total_intentos += 1

   if Seguir == 'N' or Seguir == 'n':
       print('Chaoooo')
       break