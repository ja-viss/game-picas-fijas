import random

def generar_numero_secreto():
    """Genera un número secreto de 4 dígitos sin repetir."""
    digitos = random.sample(range(10), 4)
    print(digitos)
    return ''.join(map(str, digitos))

def contar_picas_y_fijas(numero_secreto, intento):
    """Calcula el número de picas y fijas entre el número secreto y el intento."""
    fijas = sum(1 for s, i in zip(numero_secreto, intento) if s == i)
    picas = sum(1 for i in intento if i in numero_secreto) - fijas
    return picas, fijas

def jugar_picas_y_fijas():
    """Función principal del juego."""
    numero_secreto = generar_numero_secreto()
    intentos = 0

    print("¡Bienvenido a Picas y Fijas!")
    print("Adivina un número de 4 dígitos sin repetir. ¡Buena suerte!")

    while True:
        intento = input("Ingresa tu intento (4 dígitos): ").strip()

        # Validar el intento
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("Por favor, ingresa un número válido de 4 dígitos sin repetir.")
            continue

        intentos += 1
        picas, fijas = contar_picas_y_fijas(numero_secreto, intento)

        # Mostrar pistas
        print(f"Picas: {picas}, Fijas: {fijas}")

        # Verificar si el jugador adivinó el número
        if fijas == 4:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Iniciar el juego
jugar_picas_y_fijas()
