import threading
import time

sem = threading.Semaphore()


def fun1():
    i = 0
    while i in range(10):
        sem.acquire()
        print(1)
        i+=1
        sem.release()
        time.sleep(1)


def fun2():
    j = 0
    while j in range(10):
        sem.acquire()
        print(2)
        if(j == 5):
            print("Pausing for 5s")
            time.sleep(5)
        j += 1
        sem.release()
        time.sleep(1)


t = threading.Thread(target=fun1)
t.start()
t2 = threading.Thread(target=fun2)
t2.start()
