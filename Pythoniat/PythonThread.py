import threading

def runeer(num):
    print('hello world : ', num)

threads = []

for i in range(10):

    t = threading.Thread(target=runeer, args=(i,))
    threads.append(t)
    t.start()
