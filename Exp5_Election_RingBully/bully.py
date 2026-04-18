class BullyElection:
    def __init__(self, processes):
        self.processes = processes
        self.alive = {p: True for p in processes}
        self.coordinator = max(processes)

    def crash(self, pid):
        self.alive[pid] = False
        print(f"Process {pid} crashed.")

    def start_election(self, pid):
        print(f"\nProcess {pid} starts election")

        higher = [p for p in self.processes if p > pid and self.alive[p]]

        if not higher:
            self.coordinator = pid
            print(f"Process {pid} becomes new Coordinator")
        else:
            print(f"Process {pid} sends Election to {higher}")
            next_process = max(higher)
            self.start_election(next_process)

    def show_coordinator(self):
        print("Current Coordinator:", self.coordinator)


if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    bully = BullyElection(processes)

    print("Bully Election Algorithm")
    bully.show_coordinator()

    bully.crash(5)        # simulate coordinator crash
    bully.start_election(2)

    bully.show_coordinator()