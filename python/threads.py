"""
Threading is important as opposed to async, in distributing and actually being able to run computational workflows in parallel.

In the new version of Python they have finally released the GIL which meant that instead of just concurrency, you can actually parallelize multiple threads.

Now a detour to how concurrency works!

A CPU contanins many cores, The OS can schedule computation on them with each having a stack frame. 

A thread is an piece/string of computation that shares the same process with other threads.

Meaning they can run at the same time, I assume the difficulty has been in Python dealing with the added complexity of it being a VM.
"""

import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

# Start threads for each link
threads = []
for link in links:
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
    threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()