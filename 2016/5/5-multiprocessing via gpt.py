from hashlib import md5

# Top-level function — must be outside any other function
def check_range(args):
    doorID, start_index, batch_size = args
    results = []
    for i in range(start_index, start_index + batch_size):
        hash = md5(f"{doorID}{i}".encode()).hexdigest()
        if hash[:5] == "00000":
            results.append((i, hash[5]))
    return results

if __name__ == "__main__":
    import time
    from multiprocessing import Pool, Manager, freeze_support

    freeze_support()
    start = time.time()

    filename = "5/input.txt"
    filename = "5/smalltest.txt"

    batch_size = 1000
    max_found = 8
    num_processes = 10

    def runhash(doorID):
        with Manager() as manager:
            found = manager.dict()
            i = 0
            pool = Pool(processes=num_processes)

            while len(found) < max_found:
                batch_args = [(doorID, i + j * batch_size, batch_size) for j in range(num_processes)]
                results = pool.map(check_range, batch_args)

                for result_set in results:
                    for index, char in result_set:
                        if len(found) < max_found:
                            found[index] = char
                i += num_processes * batch_size

            pool.close()
            pool.join()

            decoded = ''.join([found[k] for k in sorted(found.keys())[:max_found]])
            return decoded

    with open(filename, 'r') as inputfile:
        line = inputfile.readline().strip()
        ans = runhash(line)

    print('Answer:')
    print(ans)
    print('Total duration is', time.time() - start)