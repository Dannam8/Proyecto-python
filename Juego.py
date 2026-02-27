import random
def saludar_e_instrucciones():
   print('Adivina adivinador...\n' 
         'Tengo un número entre el 1 al 100\n'
         'Quieres adivinar?')


def ingresar_si_o_no(pregunta_y_or_n: str):
   while True:
      seguir = input(pregunta_y_or_n)
      if seguir in ['Y', 'y', 'N', 'n']:
       break
      else: 
         print('Ingrese opción válida')
   return seguir

def preguntar_comenzar():
   comenzar = ingresar_si_o_no('Para comenzar ingresa "Y", para salir "N": ')
   if comenzar in ['Y', 'y']:
      comenzar = True
   else: 
      comenzar = False
   return comenzar

def elegir_numero_correcto():
   rango = list(range(1, 101))
   numero_correcto = random.choice(rango)
   return numero_correcto


def calcular_intentos_y_pistas(dificultad, numero_correcto):
   if dificultad == 1:
      intentos = 10
   elif dificultad == 2: 
      intentos = 5
      if numero_correcto % 2 == 0:
         print('Pista 1: El número es par')
      else:
         print('Pista 1: El número es impar')
   elif dificultad ==3:
      intentos = 3
      if numero_correcto % 2 == 0:
         print('Pista 1: El número es par')
      else: 
         print('Pista 1: El número es impar')
      if numero_correcto < 50:
         print('Pista 2: Está entre la primera mitad')
      else: 
         print('Pista 2: Está entre la segunda mitad')
   else:  
      print('Ingrese opción válida')
   return intentos

def elegir_dificultad():
   while True:
      dificultad = input('Ingresa nivel de dificultad:\n'
         '1.Fácil: Tienes 10 oportunidades\n'
         '2.Medio: Tienes 5 oportunidades y 1 pista\n' 
         '3.Dificil: Tienes 3 oportunidades y 2 pistas\n'
         'Tu elección: ')
      if dificultad in ['1', '2', '3']:
         dificultad = int(dificultad)
         break
      else: 
         print('Ingrese opción válida')
   return dificultad
         

def ejecutar_juego (intentos, numero_correcto):
   i = 0
   gano = False
   while i < intentos:
      try:
         intento = int(input('Introduce tu intento de adivinanza: '))
         if intento == numero_correcto:
            print('Adivinaste waos!!!!')
            gano = True
            break
         
         if intento < numero_correcto:
            print('Incorrecto! un poquito mayor...\n' \
            f'Te quedan {intentos - (i+1)} intentos')
         else:
            print('Incorrecto! un poquito menor...\n' \
            f'Te quedan {intentos - (i+1)} intentos')
         i += 1

         if i ==  intentos:
            print(f'Perdiste cuaaaaaa\n'
                  f'El número era {numero_correcto}')
            gano = False
      except ValueError:
         print('Ingrese un número válido: ')
       
   return gano

def preguntar_jugar_nuevo_juego():
   Seguir = ingresar_si_o_no('¿Quieres jugar otra vez? (Y/N): ')
   if Seguir in ['Y', 'y']:
      Seguir = True
   else: 
       Seguir = False
   return Seguir

def main():
   saludar_e_instrucciones() 
   seguir = preguntar_comenzar()
   total_intentos = 0
   partidas_ganadas = 0

   while seguir:
      total_intentos += 1 
      numero_correcto = elegir_numero_correcto()
      Dificultad = elegir_dificultad()
      intentos = calcular_intentos_y_pistas(Dificultad, numero_correcto)
      gano = ejecutar_juego(intentos, numero_correcto) 
      if gano:
         partidas_ganadas += 1
         print('Tus estadísticas:\n'
               f'Total partidas jugadas: {total_intentos}\n'
               f'Total partidas ganadas: {partidas_ganadas}')
      else:
         print('Tus estadísticas:\n'
               f'Total partidas jugadas: {total_intentos}\n'
               f'Total partidas ganadas: {partidas_ganadas}')
      seguir = preguntar_jugar_nuevo_juego()
   print('Chaoooo')


if __name__ == '__main__':
       main()




#partidas_ganadas = 0
#total_intentos = 1
#print('Adivina adivinador...\n' 
#'Tengo un número entre el 1 al 100\n'
#'Quieres adivinar?')
#Seguir = ingresar_si_o_no('Para comenzar ingresa "Y", para salir "N": ')
#Rango = list(range(1, 101))

#while Seguir == 'Y' or Seguir == 'y':
   #numero_correcto = random.choice(Rango)
   #while True:
      # try:
         # Dificultad = int(input('Ingresa nivel de dificultad:\n'
        # '1.Fácil: Tienes 10 oportunidades\n'
        # '2.Medio: Tienes 5 oportunidades y 1 pista\n' 
        # '3.Dificil: Tienes 3 oportunidades y 2 pistas\n'
        # 'Tu elección: '))
        ##  if Dificultad == 1:
        #       intentos = 10
           #   break
        #  elif Dificultad == 2: 
             #   intentos = 5
         #    if numero_correcto % 2 == 0:
             #    print('Pista 1: El número es par')
         #    else:
             #   print('Pista 1: El número es impar')
         #    break
         #  elif Dificultad ==3:
         #      intentos = 3
          #     if numero_correcto % 2 == 0:
         #       print('Pista 1: El número es par')
           #    else: 
         ###       print('Pista 1: El número es impar')
           #    if numero_correcto < 50:
#print('Pista 2: Está entre la primera mitad')
          #     else: 
         #          print('Pista 2: Está entre la segunda mitad')
          #     break
         # else:  
        #      print('Ingrese opción válida')
       # except ValueError:
         #  print('Ingresa un número')
      
   
   #i = 0
   #while i <   intentos:
     #try:
        # Intento = int(input('Introduce tu intento de adivinanza: '))
         #if Intento == numero_correcto:
           # print('Adivinaste waos!!!!')
           # partidas_ganadas += 1
           # break
         
         #if Intento < numero_correcto:
           # print('Incorrecto! un poquito mayor...\n' \
           # f'Te quedan    intentos - (i+1)} intentos')
         #else:
         #   print('Incorrecto! un poquito menor...\n' \
         ##   f'Te quedan    intentos - (i+1)} intentos')
       #  i += 1

         #if i ==  intentos:
          #  print(f'Perdiste cuaaaaaa\n'
           #       f'El número era {numero_correcto}')
     #except ValueError:
       # print('Ingrese un número válido: ')
       
   #print('Tus estadísticas:\n'
  # f'Total partidas jugadas: {total_intentos}\n'
  # f'Total partidas ganadas: {partidas_ganadas}')

  # Seguir = ingresar_si_o_no('¿Quieres jugar otra vez? (Y/N): ')
   #if Seguir == 'Y' or Seguir == 'y':
   #   total_intentos += 1

   #if Seguir == 'N' or Seguir == 'n':
   #    print('Chaoooo')
    #   break