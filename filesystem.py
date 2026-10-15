fs_root = {}   # folder = dict, file = str
cwd = []       # current directory path


def _current_dir():
    node = fs_root
    for name in cwd:
        node = node[name]
    return node


def cmd_dir(args):
    node = _current_dir()
    path = "\\" + "\\".join(cwd)
    print(f"\nDirectory of {path}\n")
    if not node:
        print("  (empty)")
    for name, item in sorted(node.items()):
        if isinstance(item, dict):
            print(f"  {'<DIR>':<9}{name}")
        else:
            print(f"  {str(len(item)) + ' B':<9}{name}")
    print()


def cmd_mkdir(args):
    if not args:
        print("Usage: mkdir <folder>")
        return
    node = _current_dir()
    if args[0] in node:
        print("Error: Name already exists.")
        return
    node[args[0]] = {}
    print("Directory created.")


def cmd_create(args):
    if not args:
        print("Usage: create <file>")
        return
    node = _current_dir()
    if args[0] in node:
        print("Error: Name already exists.")
        return
    node[args[0]] = ""
    print("File created.")


def cmd_write(args):
    if len(args) < 2:
        print("Usage: write <file> <text>")
        return
    node = _current_dir()
    if args[0] not in node or isinstance(node[args[0]], dict):
        print("Error: File does not exist.")
        return
    node[args[0]] = " ".join(args[1:])
    print("File saved.")


def cmd_read(args):
    if not args:
        print("Usage: read <file>")
        return
    node = _current_dir()
    if args[0] not in node or isinstance(node[args[0]], dict):
        print("Error: File does not exist.")
        return
    print()
    print(node[args[0]] if node[args[0]] else "(empty file)")
    print()


def cmd_delete(args):
    if not args:
        print("Usage: delete <name>")
        return
    node = _current_dir()
    if args[0] not in node:
        print("Error: File or directory does not exist.")
        return
    if isinstance(node[args[0]], dict) and node[args[0]]:
        print("Error: Directory is not empty.")
        return
    del node[args[0]]
    print("Deleted.")


def cmd_cd(args):
    if not args:
        print("Usage: cd <folder> or cd ..")
        return
    if args[0] == "..":
        if cwd:
            cwd.pop()
        return
    node = _current_dir()
    if args[0] not in node or not isinstance(node[args[0]], dict):
        print("Error: Directory does not exist.")
        return
    cwd.append(args[0])