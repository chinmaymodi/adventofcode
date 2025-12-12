import time
timestart = time.time()
from hashlib import md5
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

def worker(a, start, end) -> tuple[int, int]:
    ans1 = None
    ans2 = None
    for i in range(start, end):
        h = md5((a+str(i)).encode()).hexdigest()
        if ans1 is None and h.startswith("00000"):
            ans1 = i
        if ans2 is None and h.startswith("000000"):
            ans2 = i
            break
    return ans1, ans2

if __name__ == "__main__":
    file = "4/smallinput.txt"
    file = "4/biginput.txt"

    with open(file, 'r') as inputfile:
        for line in inputfile:
            a = line.strip()
            chunk = 100000
            limit = 2000000

            futures = []
            ranges = {}
            ans1 = None
            ans2 = None

            with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
                start = 0
                while start < limit:
                    f = executor.submit(worker, a, start, start + chunk)
                    futures.append(f)
                    ranges[f] = (start, start + chunk)
                    start += chunk
                completed_ranges = set()
                for f in as_completed(futures):
                    r1, r2 = f.result()
                    s, e = ranges[f]
                    completed_ranges.add((s, e))

                    if r1 and (ans1 is None or r1 < ans1):
                        ans1 = r1
                    if r2 and (ans2 is None or r2 < ans2):
                        ans2 = r2
                    if ans1 and ans2:
                        cutoff = min(ans1, ans2)
                        all_lower_done = True
                        for (rs, re) in ranges.values():
                            if rs < cutoff and (rs, re) not in completed_ranges:
                                all_lower_done = False
                                break
                        if all_lower_done:
                            for fut in futures:
                                if fut not in completed_ranges:
                                    rs, re = ranges[fut]
                                    if rs >= cutoff:
                                        fut.cancel()
                            break

    print('Final answer is:')
    print(ans1)
    print(ans2)
    print('Total duration is', time.time() - timestart)
