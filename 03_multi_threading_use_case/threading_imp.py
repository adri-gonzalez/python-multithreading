import threading
import queue
import time


def worker():
    while True:
        item = q.get()
        with thread_lock:
            print(f'Working on {item}')
            print(f'Finished {item}')
        time.sleep(1)
        q.task_done()


# Definimos un lock
thread_lock = threading.Lock()

# Creamos nuestro Queue
q = queue.Queue()

# Definimos el numero de threads
for r in range(2):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Iniciamos el temporizador antes de enviar tareas a la cola
start_time = time.time()

print(f"Creating a task request for each item in the given range\n")

# mandamos 10 request al worker
for item in range(10):
    q.put(item)

# bloqueamos hasta que todas las tareas esten listas
q.join()

print(f"All workers completed their tasks after {round(time.time() - start_time, 2)} seconds")
