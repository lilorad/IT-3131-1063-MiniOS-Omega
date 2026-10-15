import os
import users
import filesystem
import processes
import memory
from datetime import datetime

OS_NAME = "MiniOS Omega(1063)"   # change to your group's MiniOS name
VERSION = "1.0"


def banner():
    print("=" * 40)
    print(f"        {OS_NAME.upper()} v{VERSION}")
    print("=" * 40)
    print("\nWelcome to MiniOS!\n")


# ---------- General commands ----------
def cmd_help(args):
    print("\nAvailable Commands:\n")
    for name in COMMANDS:
        print(f"  {name:<12} - {COMMANDS[name][1]}")
    print()


def cmd_clear(args):
    os.system("cls" if os.name == "nt" else "clear")


def cmd_date(args):
    print("Date:", datetime.now().strftime("%Y-%m-%d"))


def cmd_time(args):
    print("Time:", datetime.now().strftime("%H:%M:%S"))


def cmd_exit(args):
    print("\nShutting down MiniOS...\n")
    print("Goodbye!")
    return "EXIT"

def cmd_whoami(args):
    print("Current User:", users.current_user)

def cmd_systeminfo(args):
    print("\n" + "=" * 40)
    print("          SYSTEM INFORMATION")
    print("=" * 40 + "\n")
    print(f"OS Name: {OS_NAME}")
    print(f"Version: {VERSION}")
    print("Architecture: 64-bit")
    print("CPU: Virtual CPU")
    print(f"Memory: {memory.TOTAL} MB")
    print(f"User: {users.current_user}")
    print("\n" + "=" * 40)


# ---------- Command table: name -> (function, description) ----------
COMMANDS = {
    "help":   (cmd_help,   "Show available commands"),
    "clear":  (cmd_clear,  "Clear the screen"),
    "date":   (cmd_date,   "Show current date"),
    "time":   (cmd_time,   "Show current time"),
    "whoami": (cmd_whoami, "Show current user"),
    "exit":   (cmd_exit,   "Shut down MiniOS"),
    "dir":    (filesystem.cmd_dir,    "List files and folders"),
    "mkdir":  (filesystem.cmd_mkdir,  "Create a directory"),
    "create": (filesystem.cmd_create, "Create an empty file"),
    "write":  (filesystem.cmd_write,  "Write text to a file"),
    "read":   (filesystem.cmd_read,   "Read a file"),
    "delete": (filesystem.cmd_delete, "Delete a file or empty folder"),
    "cd":     (filesystem.cmd_cd,     "Change directory"),
    "process": (processes.cmd_process, "Show running processes"),
    "run":     (processes.cmd_run,     "Start a process"),
    "kill":    (processes.cmd_kill,    "Terminate a process by PID"),
    "memory":   (memory.cmd_memory,   "Show memory status"),
    "allocate": (memory.cmd_allocate, "Allocate memory (MB)"),
    "free":     (memory.cmd_free,     "Release memory (MB)"),
    "systeminfo": (cmd_systeminfo, "Show system information"),
}


def shell():
    while True:
        try:
            line = input("MiniOS> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            line = "exit"

        if not line:
            continue

        parts = line.split()
        name = parts[0].lower()
        args = parts[1:]

        if name not in COMMANDS:
            print("Unknown command.\n")
            print("Type 'help' to see the available commands.")
            continue

        try:
            result = COMMANDS[name][0](args)
        except Exception as e:
            print(f"Error: {e}")
            continue

        if result == "EXIT":
            break


def main():
    if not users.login():
        return
    banner()
    shell()


if __name__ == "__main__":
    main()