import threading
from threading import Thread
from threading import Lock
from threading import currentThread
import time

shared_resource = [1,2,3]
lock = Lock()

def first_thread():
    print(f"Acquiring lock {currentThread().name}")
    lock.acquire()
    print(f"Got the lock {currentThread().name}")
    time.sleep(10)
    shared_resource[0] = 787
    print(f"releasing lock {currentThread().name}")
    lock.release()
    print(f"Released lock {currentThread().name}")

def second_thread():
    print(f"Acquiring lock {currentThread().name}")
    lock.acquire()
    print(f"Got the lock {currentThread().name}")
    print(shared_resource)
    time.sleep(3)
    shared_resource[0] = 1000
    print(f"releasing lock {currentThread().name}")
    lock.release()
    print(f"Released lock {currentThread().name}")

if __name__ == '__main__':
    thread1 = Thread(target=first_thread, name="Thread1")
    thread1.start()
    thread2 = Thread(target=second_thread, name="Thread2")
    thread2.start()

    thread1.join()
    thread2.join()
