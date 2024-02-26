import subprocess
import threading

# Variable para indicar si una emisora está reproduciéndose actualmente
emisora_reproduciendose = False

# Función para reproducir emisora de radio FM con mpg123 en segundo plano
def reproducir_emisora(emisora):
    global emisora_reproduciendose
    emisora_reproduciendose = True
    proceso = subprocess.Popen(["mpg123", "-q", emisora])
    proceso.wait()
    emisora_reproduciendose = False

# Función para detener la reproducción de la emisora actual
def detener_reproduccion():
    global emisora_reproduciendose
    if emisora_reproduciendose:
        subprocess.run(["pkill", "mpg123"])
        emisora_reproduciendose = False

# Función para mostrar el menú y obtener la selección del usuario
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Emisora 1")
    print("2. Emisora 2")
    print("3. GranadaFM")
    print("4. Salir")
    return input("Elija una opción: ")

# URLs de las emisoras de radio
emisora_1 = "https://online.vibacomunicacion.com:9304/stream"
emisora_2 = "http://streaming.elitecomunicacion.es:8086/"
emisora_3 = "https://streaming2.elitecomunicacion.es:8028/stream"

# Ciclo para mostrar el menú y controlar la reproducción de la emisora seleccionada
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        detener_reproduccion()
        hilo_emisora_1 = threading.Thread(target=reproducir_emisora, args=(emisora_1,))
        hilo_emisora_1.start()
    elif opcion == "2":
        detener_reproduccion()
        hilo_emisora_2 = threading.Thread(target=reproducir_emisora, args=(emisora_2,))
        hilo_emisora_2.start()
    elif opcion == "3":
        detener_reproduccion()
        hilo_emisora_3 = threading.Thread(target=reproducir_emisora, args=(emisora_3,))
        hilo_emisora_3.start()
    elif opcion == "4":
        detener_reproduccion()
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

