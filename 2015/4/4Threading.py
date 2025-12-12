import time
from hashlib import md5
import threading

def worker(a, start, end, ans1, ans2, stop_event1, stop_event2, lock):
    for i in range(start, end):
        if stop_event1.is_set() and stop_event2.is_set():
            return
        h = md5((a+str(i)).encode()).hexdigest()
        if h.startswith("00000"):
            with lock:
                if ans1[0] is None or i < ans1[0]:
                    ans1[0] = i
                    ans1[1] = h
            stop_event1.set()
            if h[5] == "0":
                with lock:
                    if ans2[0] is None or i < ans2[0]:
                        ans2[0] = i
                        ans2[1] = h
                stop_event2.set()

def thread_manager(a, chunk, ans1, ans2, stop_event1, stop_event2):
    start = 0
    active_threads = []
    max_threads = threading.active_count()  # or use os.cpu_count()

    lock = threading.Lock()

    # initialize core threads
    for _ in range(max_threads):
        t = threading.Thread(target=worker,
                             args=(a, start, start+chunk,
                                   ans1, ans2, stop_event1, stop_event2, lock))
        t.start()
        active_threads.append(t)
        start += chunk

    # monitor threads
    while ans1[0] is None or ans2[0] is None:
        for t in list(active_threads):
            if not t.is_alive():
                active_threads.remove(t)
                if ans1[0] is None or ans2[0] is None:
                    # spawn one new thread
                    new_t = threading.Thread(target=worker,
                                             args=(a, start, start+chunk,
                                                   ans1, ans2, stop_event1, stop_event2, lock))
                    new_t.start()
                    active_threads.append(new_t)
                    start += chunk
        time.sleep(0.01)  # avoid busy spin

    # wait for all threads to finish
    for t in active_threads:
        t.join()

if __name__ == "__main__":
    timestart = time.time()
    file = "4/biginput.txt"

    # shared answers: [index, hash]
    ans1 = [None, None]
    ans2 = [None, None]
    stop_event1 = threading.Event()
    stop_event2 = threading.Event()

    with open(file, 'r') as inputfile:
        for line in inputfile:
            a = line.strip()
            chunk = 10000
            thread_manager(a, chunk, ans1, ans2, stop_event1, stop_event2)

    print("Final answer is:")
    print(ans1[0], ans1[1])
    print(ans2[0], ans2[1])
    print("Total duration is", time.time()-timestart)
