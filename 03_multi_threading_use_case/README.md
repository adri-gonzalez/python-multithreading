# Multithreading tasks usando python 3

Dentro de este directorio se encuentran tres posibles ejemplos en los cuales podriamos utilizar multithreading con el
objetivo de encontrar formas de ser más eficiente automatizando algunos de tus flujos de trabajo.

## Sections:

1. Que es una worker function?
2. Que es queue?
3. Que es thread?
4. Multithreaded Ping Sweep
5. Multithreaded Port Scanner

## Que es una worker function?

A worker function es el conjunto de instrucciones que define para que se ejecuten dentro de cada subproceso para cada
tarea en la cola. Podría ser una función con todo incluido o incluso puede contener otras funciones que defina. Dentro
de esta función, debe tomar una tarea de la cola, que es la forma en que su trabajador conocerá cada tarea única que
debe completar. Una vez que haya terminado, le dirá a la cola que ha terminado con esa tarea.

Cuando escribe su serie de instrucciones para una operación enhebrada, debe protegerse contra el acceso simultáneo a un
objeto. En el fragmento a continuación, el objeto compartido es la variable del elemento. Si no usa un candado, lo que
sucederá con un script que usa muchos subprocesos podría tropezar entre sí y causar daños en los datos o resultados
inexactos. Esto puede ser útil en los casos en los que también agrega cálculos matemáticos en su lógica.

```python
def worker():
    while True:
        item = q.get()
        with thread_lock:
            print(f'Working on {item}')
            print(f'Finished {item}')
        time.sleep(1)
        q.task_done()


thread_lock = threading.Lock()
 ```

## Que es queue?

A queue proporciona un medio lógico para ejecutar una secuencia de tareas de manera organizada, lo cual es muy útil
cuando se incorpora con programas enhebrados. Creas tu cola y la llenas de tareas. Por ejemplo, su secuencia de comandos
podría apuntar a una lista de direcciones IP para que pueda llenar su cola de direcciones IP. Cuando se ejecute su
función de trabajador, tomará una IP de la cola y ejecutará su serie de instrucciones. Tenga en cuenta que por cada hilo
que tenga, esa es la cantidad de tareas que se ejecutarán a la vez.

* One Thread = Una tarea a la vez hasta que la cola está vacía
* Two Threads = Dos tareas a la vez hasta que la cola está vacía
* Ten Threads = Diez tareas a la vez hasta que la cola está vacía

No olvide la importancia de q.join (). Esto le indicará al hilo principal que espere hasta que se completen todas las
tareas antes de continuar. Ésta es una información importante. Si no pone esto en su lugar, después de crear su cola y
comenzar su trabajo, el hilo principal terminará, eliminando todas las tareas en ejecución sin darles tiempo para
terminar.

```python
q = queue.Queue()

for item in range(10):
    q.put(item)

q.join()
```

## What is a thread?

Un thread por sí solo es un conjunto consolidado de instrucciones. Con un solo hilo, un comando se ejecuta a la vez,
como un script simple. Cuando introduce más subprocesos, o subprocesos múltiples, puede tener varias series de
instrucciones ejecutándose al mismo tiempo para una ejecución simultánea.

Por ejemplo, supongamos que tiene un script que envía cuatro sondeos ICMP a dos servidores y tarda dos segundos en
sondear cada servidor. En este caso, todo el tiempo de procesamiento en un solo hilo toma cuatro segundos. Puede que no
suene como un gran problema, pero cuando estás escaneando una red / 24 eso puede llevar algo de tiempo. Especialmente
cuando empiezas a hablar de / 16 o a / 8. Cuando introduces dos subprocesos, con cada subproceso probando un servidor,
tomará dos segundos sondear ambos servidores porque las tareas se ejecutan simultáneamente Si bien parece que cuantos
más subprocesos arroje en una cola, más rápido se completará su tarea, sin embargo, tenga en cuenta que esto no siempre
es cierto. Debe asegurarse de que su sistema pueda manejar los recursos que se están aprovisionando, especialmente si su
sistema ya está procesando otras tareas dentro y fuera del script.

```python
# Definir el numero de hilos
for r in range(2):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
```

## Estructura

Pongamos la narrativa anterior en código funcional. Como podemos ver con Python, es muy fácil crear usted mismo una
estructura básica para un proceso multiproceso.
**Let's summarize:**

* Creas una función worker con tu conjunto de instrucciones
* Define la cantidad de subprocesos que desea aprovisionar
* Envía las solicitudes de trabajo a la cola en función de las tareas que desea ejecutar
* Esperas a que terminen los trabajos y finalizas tu guión

Tómese el tiempo para aumentar la cantidad de subprocesos y tareas y vea cómo cambia la salida. También agregué una
función de suspensión a la función de trabajador para que pueda simular el tiempo que tarda una tarea en completarse.

```python
#!/usr/bin/python3

import threading  # https://docs.python.org/3/library/threading.html
import queue  # https://docs.python.org/3/library/queue.html
import time  # https://docs.python.org/3/library/time.html


def worker():
    while True:
        item = q.get()
        with thread_lock:
            print(f'Working on {item}')
            print(f'Finished {item}')
        time.sleep(1)
        q.task_done()


thread_lock = threading.Lock()

q = queue.Queue()

for r in range(2):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

start_time = time.time()

print(f"Creating a task request for each item in the given range\n")

for item in range(10):
    q.put(item)

q.join()

print(f"All workers completed their tasks after {round(time.time() - start_time, 2)} seconds")

```

### Ping Sweep

Descubra hosts en vivo en una red y una de las formas más eficientes es simplemente enviar sondas ICMP para ver quién
responde. Cuando hablamos de una red / 24, esto no será demasiado difícil. Sin embargo, cuando empiece a hablar de un /
16 o incluso de un / 8, estará corriendo contrarreloj como mencionamos anteriormente. Para incorporar subprocesos
múltiples en este ejemplo, crearemos tareas llenando la cola con una lista de direcciones IP y cada subproceso se
utilizará para hacer ping a una IP de la cola a la vez.

## Recursos

* https://docs.python.org/3/library/threading.html
* https://docs.python.org/3/library/queue.html
* https://docs.python.org/3/library/socket.html
