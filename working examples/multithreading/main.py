from threading import Thread
import threading
from time import sleep

class FB(Thread):
    def run(self):
        for x in range(1,6):
            print("fb")
            sleep(3)
class Whatsapp(Thread):
    def run(self):
        for x in range(1,6):
            print("Whatsapp")
            sleep(2.5)
t1=FB()
t2=Whatsapp()

t1.start()
t1.join()
t2.start()