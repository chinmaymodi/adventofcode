import time
from hashlib import md5
import multiprocessing

def worker(a, start, end, ans1, ans2, stop_event1, stop_event2):
    for i in range(start, end):
        if stop_event1.is_set() and stop_event2.is_set():
            return
        h = md5((a+str(i)).encode()).hexdigest()
        if h.startswith("00000"):
            with ans1.get_lock():
                if i < ans1.value:
                    ans1.value = i
            stop_event1.set()
            if h[5] == "0":
                with ans2.get_lock():
                    if i < ans2.value:
                        ans2.value = i
                stop_event2.set()

def process_manager(a, chunk, ans1, ans2, stop_event1, stop_event2):
    start = 0
    active = []
    max_procs = multiprocessing.cpu_count()

    # initialize core processes
    for _ in range(max_procs):
        p = multiprocessing.Process(target=worker,
                                    args=(a, start, start+chunk,
                                          ans1, ans2, stop_event1, stop_event2))
        p.start()
        active.append(p)
        start += chunk

    # monitor processes
    while ans1.value == 10**10 or ans2.value == 10**10:
        for p in list(active):
            if not p.is_alive():
                active.remove(p)
                p.join()
                if ans1.value == 10**10 or ans2.value == 10**10:
                    # spawn one new process
                    new_p = multiprocessing.Process(target=worker,
                                                    args=(a, start, start+chunk,
                                                          ans1, ans2, stop_event1, stop_event2))
                    new_p.start()
                    active.append(new_p)
                    start += chunk
        time.sleep(0.01)  # avoid busy spin

    # wait for all to finish
    for p in active:
        p.join()

if __name__ == "__main__":
    timestart = time.time()
    file = "4/biginput.txt"

    ans1 = multiprocessing.Value('q', 10**10)
    ans2 = multiprocessing.Value('q', 10**10)
    stop_event1 = multiprocessing.Event()
    stop_event2 = multiprocessing.Event()

    with open(file, 'r') as inputfile:
        for line in inputfile:
            a = line.strip()
            chunk = 10000
            process_manager(a, chunk, ans1, ans2, stop_event1, stop_event2)

    print("Final answer is:")
    print(ans1.value, md5((a+str(ans1.value)).encode()).hexdigest())
    print(ans2.value, md5((a+str(ans2.value)).encode()).hexdigest())
    print("Total duration is", time.time()-timestart)
