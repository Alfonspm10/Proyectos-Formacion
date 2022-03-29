import random

contador=0

print('Bienvenido viajero! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,20)
numero_intentos=6
print('Bueno, '+nombre+', piensa un número entre 1 y 20.')

while contador<6:
    print ('Adivina el numero! Tienes ' + str(numero_intentos) + ' intentos')
    adivina=input()
    adivina=int(adivina)
    contador= contador + 1
    numero_intentos = numero_intentos - 1

    if adivina<numero:
        print ('Demasiado pequeño')
        
    if adivina>numero:
        print('Demasiado grande')
        
    if adivina==numero:
        break

if adivina==numero:
    contador=str(contador)
    print('Muuuuuuuuy bien, '+ nombre +', has acertado el numero en '+ contador +' intentos. Buen trabajo joven padawan')

if adivina!=numero:
    numero=str(numero)
    print('Esperaba demasiadas cosas de ti '+ nombre +' El numero correcto era '+ numero)