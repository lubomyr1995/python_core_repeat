import threading
import time

# def show(n):
#     for i in range(n):
#         time.sleep(0.5)
#         print(i, threading.current_thread().name)
#
#
# # show(5)
#
# thread1 = threading.Thread(target=show, args=(5,), name='thread1')
# thread2 = threading.Thread(target=show, args=(8,), name='thread2')
#
# thread1.start()
# thread2.start()
# show(3)

count = 0
lock = threading.Lock()


def inc():
    with lock:
        global count
        count += 1
        print(count)


threads = []
for i in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
