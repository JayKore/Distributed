class RingElection:
    def __init__(self, processes):
        self.processes = processes
        self.alive = {p: True for p in processes}
        self.coordinator = max(processes)

    def crash(self, pid):
        self.alive[pid] = False
        print(f"Process {pid} crashed.")

    def start_election(self, starter):
        print(f"\nProcess {starter} starts election")

        active = []
        n = len(self.processes)
        index = self.processes.index(starter)

        for i in range(n):
            pid = self.processes[(index + i) % n]
            if self.alive[pid]:
                active.append(pid)

        print("Active processes:", active)

        self.coordinator = max(active)
        print(f"Process {self.coordinator} elected as Coordinator")

    def show_coordinator(self):
        print("Current Coordinator:", self.coordinator)


if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    ring = RingElection(processes)

    print("Ring Election Algorithm")
    ring.show_coordinator()

    ring.crash(4)
    ring.start_election(2)

    ring.show_coordinator()