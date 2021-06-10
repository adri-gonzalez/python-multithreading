# Python program to illustrate the concept
# of threading
import threading
import os


def task1():
    print("Tarea 1 asignada al hilo: {}".format(threading.current_thread().name))
    print("ID del proceso corriendo la tarea 1: {}".format(os.getpid()))


def task2():
    print("Tarea 2 asignada al hilo: {}".format(threading.current_thread().name))
    print("ID del proceso corriendo la tarea 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
    print("ID del proceso corriendo el programa principal: {}".format(os.getpid()))

    # print name of main thread
    print("Nombre del hilo principal: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
