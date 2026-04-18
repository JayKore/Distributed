import threading
import time
import random

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.has_token = False
        self.request = False

    def request_cs(self):
        print(f"Process {self.pid} requesting CS")
        self.request = True

    def enter_cs(self):
        print(f"Process {self.pid} >>> ENTERED CS")
        time.sleep(2)
        print(f"Process {self.pid} <<< EXITING CS")
        self.request = False


def token_ring(processes):
    token_holder = 0
    processes[token_holder].has_token = True

    while True:
        current = processes[token_holder]

        print(f"\n[Token with Process {current.pid}]")

        if current.request:
            current.enter_cs()

        # Pass token to next process
        current.has_token = False
        token_holder = (token_holder + 1) % len(processes)
        processes[token_holder].has_token = True

        time.sleep(1)


def generate_requests(processes):
    while True:
        time.sleep(2)  # faster + visible
        p = random.choice(processes)
        if not p.request:
            p.request_cs()


if __name__ == "__main__":
    n = 3
    processes = [Process(i) for i in range(n)]

    # Force initial request so output starts immediately
    processes[0].request_cs()

    threading.Thread(target=token_ring, args=(processes,), daemon=True).start()
    threading.Thread(target=generate_requests, args=(processes,), daemon=True).start()

    time.sleep(20)