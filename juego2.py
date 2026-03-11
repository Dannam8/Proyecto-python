print('Bienvenido! \n' 
'Adivinaré tu número...')

condicion = True
partidas_ganadas = 0

while condicion:
    print('¿Listo?')
    min = 1
    max = 100 
    try:
        numero_de_intentos = 1
        i = 0
        while i<8:
            i += 1
            intento_numero = int((min + max) / 2)
            correcto = input(f'Tu número es {intento_numero}? (y or n): ')
            if correcto in ['y', 'Y']:
                print('Gané cuaaaaa')
                partidas_ganadas += 1
                break
            elif correcto in ['n', 'N']:
                numero_de_intentos += 1
                pista = input('¿Es mayor (ma) o menor (me)?: ')

                if pista in ['ma', 'MA', 'Ma']:
                    min = intento_numero

                elif pista in ['me', 'ME', 'Me']:
                    max = intento_numero

                else: 
                    print('ingresa opción válida: ')
            else: 
                print('Ingrese opción válida: ')
    except:
        print('Ingresa número válido: ')
        
    print(f'Las estadísticas son: \n' \
    f'Número de intentos hechos: {numero_de_intentos} \n'
    f'Partidas ganadas: {partidas_ganadas}')

    condicion = input('Quieres volver a jugar? (y or n): ')
    if condicion in ['y', 'Y']:
        condicion = True
    else:
        print('Chao pescao')
        condicion = False