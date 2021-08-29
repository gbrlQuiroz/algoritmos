print('Ejercicio 1')


# función para pedir los valores y meterlos en los arreglos
# si se da un valor incorrecto o que no cumpla la rgla de negocio  se pone valor de cero(0) en el arreglo
def valuesInput(lista):
    categorias = ['Claridad del problema', 'Originalidad', 'Dificultad']
    for i in categorias:
        try:
            valor = int(input(f'{i}: '))
            if valor <= 1 or valor >= 100:
                raise TypeError
            lista.append(valor)
        except ValueError:
            lista.append(0)
            print('--->>>Error: valor dado no es correcto')
        except TypeError:
            lista.append(0)
            print('--->>>Error: el valor no esta dentro del rango')

# se piden valores
print('\nIntroduce valores para Alice:')
alice = []
valuesInput(alice)

print('\nIntroduce valores para Bob:')
bob = []
valuesInput(bob)

# se imprimen los valores capturados por el cliente
print(f'\nCalificaciones de Alice: {alice}')
print(f'Calificaciones de Bob: {bob}')

puntosAlice = 0
puntosBob = 0

# verificacion de valores y asignacion de puntos segun lo solicitado en el problema
for (al, bo) in zip(alice, bob):
    if al > bo:
        puntosAlice += 1
    elif al < bo:
        puntosBob += 1

puntosTotales = []
puntosTotales.append(puntosAlice)
puntosTotales.append(puntosBob)
print(f'\n{puntosTotales}')
print(f'\n\nPuntos Alice: {puntosAlice}, Puntos Bob: {puntosBob}')
