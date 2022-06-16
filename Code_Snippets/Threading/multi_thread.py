from concurrent.futures import thread
import time
import os
import threading
import concurrent.futures
from unittest import result

def do_something(val):
        # print("--> Sleeping for 1 second")
        time.sleep(1)
        # print("--> Done sleeping")
        return f"Done Sleeping {val}"
    

class Basic_Manual:
    def run(self):
        start = time.perf_counter()
        for _ in range(10):
            do_something(val=2)

        print(f"Time taken without threads = {time.perf_counter()-start}")
    
    def run_with_thread(self):
        start = time.perf_counter()

        # th1 = threading.Thread(target = self.do_something)
        # th1.start()
        # th1.join()

        threads = []
        for _ in range(10):
            t = threading.Thread(target=do_something, args=(1.5,))
            t.start()
            threads.append(t)

        # wait for all threads to complete
        for t in threads:
            t.join()

        print(f"Time taken with threads= {time.perf_counter()-start}")
    
    def run_with_futures(self):
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # th1 = executor.submit(do_something, 2.5)
            # print("Single Job: ",th1.result())

            # DOESNT MANTAIN ORDER
            results = [executor.submit(do_something, _) for _ in range(10)]
            for f in concurrent.futures.as_completed(results):
                print(f.result())

        print(f"Time taken with threads + Futures (Order not maintained)= {time.perf_counter()-start}")
    
    def run_with_futures_map(self):
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            #maintain order
            results = executor.map(do_something, range(10))

            for res in results:
                print(res)
            print(f"Time taken with threads + Futures + Map (Order maintained)= {time.perf_counter()-start}")




# Basic_Manual().run()
Basic_Manual().run_with_futures()
Basic_Manual().run_with_futures_map()

