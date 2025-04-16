import time

def running_2000(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start
