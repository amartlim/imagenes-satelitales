import threading
import queue
import time
import random

cola = queue.Queue()
TOTAL_IMAGENES = 10

def receptor():
    for i in range(TOTAL_IMAGENES):
        imagen = f"imagen_{i+1}"
        cola.put(imagen)
        print(f"Recibida: {imagen}")
        time.sleep(random.uniform(0.2, 1.2))  # llegada a veces rápida, a veces lenta

def procesador():
    for _ in range(TOTAL_IMAGENES):
        imagen = cola.get()   # si no hay imágenes, espera
        print(f"Procesando: {imagen}")
        time.sleep(random.uniform(0.3, 1.5))  # procesamiento a veces rápido, a veces lento
        print(f"Procesada: {imagen}")
        cola.task_done()

productor = threading.Thread(target=receptor)
consumidor = threading.Thread(target=procesador)

productor.start()
consumidor.start()

productor.join()
cola.join()

print("Sistema terminado.")