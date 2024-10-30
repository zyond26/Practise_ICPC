def solve_task(n,tasks):
    days = []
    completed = [False] *n

    while not all(completed):
        day_tasks = []
        current = -1

        for i in range(n):
            if not completed[i] and tasks[i] > current :
                day_tasks.append(i+1)
                current = tasks[i]
                completed[i] = True
        days.append(day_tasks)

    print(len(days))
    for day in days:
        print(len(day),' '.join(map(str,day)))

n = int(input())
tasks = list(map(int,input().split()))
solve_task(n,tasks)

