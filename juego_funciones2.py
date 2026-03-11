def saludar():
    print('Bienvenido! \n' 
    'Adivinaré tu número...')

def main():
    saludar()
    condicion = True
    numero_intentos = 0
    while condicion:
        print('¿Listo?')
        min = 1
        max = 100
        num_intentos_final, min, max = ejecutar_juego(min, max, numero_intentos)
        imprimir_estadisticas(num_intentos_final)
        condicion = input('Quieres volver a jugar? (y or n): ')
        if condicion in ['y', 'Y']:
            condicion = True
        else:
            print('Chao pescao')
            condicion = False
        
def ejecutar_juego(min, max, numero_intentos):
    i = 0
    while i < 8:
        i += 1
        intento_numero = int((min + max) / 2)
        correcto = input(f'Tu número es {intento_numero}? (y or n): ')
        if correcto in ['y', 'Y']:
            print('Gané cuaaaaa')
            break
        else:
            min, max = evaluar_mayor_menor(correcto, intento_numero, min, max)
            numero_intentos += 1

    return numero_intentos, min, max

def evaluar_mayor_menor(correcto, intento_numero, min, max):
    if correcto in ['n', 'N']:
        pista = input('¿Es mayor (ma) o menor (me)?: ')

        if pista in ['ma', 'MA', 'Ma']:
            min = intento_numero

        elif pista in ['me', 'ME', 'Me']:
            max = intento_numero
    else: 
        print('ingresa opción válida: ')
    return min, max

def imprimir_estadisticas(numero_de_intentos: int):
     print(f'Las estadísticas son: \n' \
     f'Número de intentos hechos: {numero_de_intentos}')
     
if __name__ == '__main__':
    main()