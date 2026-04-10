import threading
import queue
import time
import random

cola = queue.Queue()

def receptor():
    for i in range(12):
        imagen = f"imagen_{i+1}"
        cola.put(imagen)
        print(f"Recibida: {imagen}")
        time.sleep(random.uniform(0.2, 1.2))  # llegada variable:a veces lento,a veces más rápido

    cola.put(None)  # señal de fin

def procesador():
    while True:
        imagen = cola.get()

        if imagen is None:   # no quedan más imágenes
            cola.task_done()
            break

        print(f"Procesando: {imagen}")
        time.sleep(random.uniform(0.3, 1.5))  # procesamiento variable: a veces más lento  a veces más rápido
        print(f"Procesada: {imagen}")
        cola.task_done()

productor = threading.Thread(target=receptor)
consumidor = threading.Thread(target=procesador)

productor.start()
consumidor.start()

productor.join()
cola.join()
consumidor.join()

print("Sistema terminado.")