import random

while True:
    accion = input("Hola viajero! Debes elegir entre piedra, papel o tijera): ")
    acciones_jugador = ["piedra", "papel", "tijera"]
    acciones_ordenador = random.choice(acciones_jugador)
    print(f"\nTu has elegido {accion} y el ordenador ha elegido {acciones_ordenador}.\n")

    if accion == acciones_ordenador:
        print(f"Ambos jugadores seleccionaron: {accion}. Es un empate")
    elif accion == "piedra":
        if acciones_ordenador == "tijeras":
            print("La roca revienta a las tijeras!! TU GANAS")
        else:
            print("El papel asfixia a la piedra... YOU LOSE.")
    elif accion == "papel":
        if acciones_ordenador == "piedra":
            print("El papel asfixia a la piedra!! TU GANAS!")
        else:
            print("Las afiladas tijeras cortan al papel!! YOU LOSE.")
    elif accion == "tijeras":
        if acciones_ordenador == "papel":
            print("Las afiladas tijeras cortan al papel!! TU GANAS!")
        else:
            print("La roca revienta a las tijeras!! YOU LOSE.")

    repetir = input("Quieres volver a jugar? (y/n): ")
    
    if repetir != "y":
        break




