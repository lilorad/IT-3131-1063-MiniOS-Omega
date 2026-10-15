processes = {}   # pid -> {"name": ..., "status": ...}
next_pid = 1


def cmd_run(args):
    global next_pid
    if not args:
        print("Usage: run <program>")
        return
    pid = next_pid
    next_pid += 1
    processes[pid] = {"name": args[0], "status": "RUNNING"}
    print("\nProcess started.\n")
    print(f"PID: {pid}")
    print(f"Name: {args[0]}")
    print("Status: RUNNING\n")


def cmd_process(args):
    if not processes:
        print("No running processes.")
        return
    print(f"\n{'PID':<7}{'NAME':<15}STATUS")
    for pid, p in processes.items():
        print(f"{pid:<7}{p['name']:<15}{p['status']}")
    print()


def cmd_kill(args):
    if not args:
        print("Usage: kill <pid>")
        return
    if not args[0].isdigit():
        print("Error: PID must be a number.")
        return
    pid = int(args[0])
    if pid not in processes:
        print("Error: Process does not exist.")
        return
    del processes[pid]
    print(f"Process {pid} terminated.")