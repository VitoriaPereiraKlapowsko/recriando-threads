import threading
import time
import random

class MinhaThread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)
        print(f"Iniciando com uma classe !! {self.i}")

def main():
    threads = []

    print("Dando inicio ao processo principal")
    print("Criando as threads...")

    # Criando 10 threads
    for a in range(10):
        thread = MinhaThread(a)
        threads.append(thread)
        thread.start()  

    for thread in threads:
        thread.join()  
    print("Finalizando...")

if __name__ == "__main__":
    main()