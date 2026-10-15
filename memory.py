TOTAL = 1024        # MB
OS_RESERVED = 256   # MB used by the "OS" itself
allocated = 0       # MB allocated by the user


def _used():
    return OS_RESERVED + allocated


def cmd_memory(args):
    print("\nMemory Status")
    print("-" * 24)
    print(f"Total Memory: {TOTAL:>5} MB")
    print(f"Used Memory:  {_used():>5} MB")
    print(f"Free Memory:  {TOTAL - _used():>5} MB\n")


def _get_amount(args, usage):
    if not args:
        print(usage)
        return None
    if not args[0].isdigit() or int(args[0]) <= 0:
        print("Error: Amount must be a positive number.")
        return None
    return int(args[0])


def cmd_allocate(args):
    global allocated
    amount = _get_amount(args, "Usage: allocate <MB>")
    if amount is None:
        return
    if amount > TOTAL - _used():
        print("Error: Not enough free memory.")
        return
    allocated += amount
    print(f"{amount} MB allocated.")


def cmd_free(args):
    global allocated
    amount = _get_amount(args, "Usage: free <MB>")
    if amount is None:
        return
    if amount > allocated:
        print("Error: Cannot free more memory than allocated.")
        return
    allocated -= amount
    print(f"{amount} MB released.")