import threading

class messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x=messenger(name='Send out messages')
y=messenger(name='Recieve messages')
x.start()
y.start()
