def task_assignment(cost):
    tasks = len(cost)
    processors = len(cost[0])

    print("\nTask Assignment:")

    total_cost = 0

    for i in range(tasks):
        min_cost = cost[i][0]
        processor = 0

        for j in range(1, processors):
            if cost[i][j] < min_cost:
                min_cost = cost[i][j]
                processor = j

        print(f"Task {i+1} -> Processor {processor+1} (Cost: {min_cost})")
        total_cost += min_cost

    print("\nTotal Minimum Cost:", total_cost)


if __name__ == "__main__":
    tasks = int(input("Enter number of tasks: "))
    processors = int(input("Enter number of processors: "))

    cost = []

    print("Enter cost matrix row by row:")
    for i in range(tasks):
        row = list(map(int, input().split()))
        cost.append(row)

    task_assignment(cost)