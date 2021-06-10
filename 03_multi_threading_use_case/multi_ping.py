import threading
import queue
import ipaddress
import subprocess
import time


def worker():
    while True:
        target = q.get()
        send_ping(target)
        q.task_done()


def send_ping(target):
    icmp = subprocess.Popen(['ping', '-c', '1', str(target)], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).communicate()
    with thread_lock:
        if "1 received" in icmp[0].decode('utf-8'):
            print(f"[*] {target} is UP")
        else:
            print(f"[*] {target} is DOWN")


# Definimos un lock
thread_lock = threading.Lock()

# Creamos nuestro Queue
q = queue.Queue()

# Definimos el numero de threads
for r in range(100):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Iniciamos el temporizador antes de enviar tareas a la cola
start_time = time.time()

# network a escanear
cidr_network = '192.168.74.0/24'
all_hosts = list(ipaddress.ip_network(cidr_network).hosts())

print(f"Creating a task request for each host in {cidr_network}\n")

# mandamos 10 request al worker
for item in all_hosts:
    q.put(item)

# bloqueamos hasta que todas las tareas esten listas
q.join()

print(f"\nAll workers completed their tasks after {round(time.time() - start_time, 2)} seconds")
