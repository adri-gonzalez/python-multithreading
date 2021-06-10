# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # Creando hilos
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # empezando el primer hilo
    t1.start()

    # empezando el segundo hilo
    t2.start()

    # esperando hasta que el primer hilo termine su tarea
    t1.join()
    # esperando hasta que el segundo hilo termine su tarea
    t2.join()

    # ambos hilos han terminado de correr sus tareas
    print("Done!")
