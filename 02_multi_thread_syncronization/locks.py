import threading

# variable global x
x = 0


def increment():
    """
    funcion para incrementar la variable global x
    """
    global x
    x += 1


def thread_task(lock):
    """
    tarea para correr en el hilo
    llama a la función de increment 100000 veces.
    """
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    # setteando la variable global x igual a 0
    x = 0

    # creando un lock
    lock = threading.Lock()

    # creando hilos
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # corriendo hilos
    t1.start()
    t2.start()

    # esperando hasta que los hilos terminen de correr sus tareas asignadas
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))
