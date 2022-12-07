global console
global dir_sizes

def run_cd():
    directory = {}
    line = console.pop(0)
    global dir_sizes

    if line == "$ ls":
        line = console.pop(0)
        while not line.startswith("$"):
            output = line.split(" ")
            if output[0] == "dir":
                directory[output[1]] = {}
            else:
                directory[output[1]] = {"size": int(output[0])}
            try:
                line = console.pop(0)
            except IndexError:
                line = "$ cd .."

    while line != "$ cd ..":
        command = line.split(" ")
        directory[command[2]] = run_cd()
        try:
            line = console.pop(0)
        except IndexError:
            line = "$ cd .."

    directory['size'] = 0
    for file in directory:
        if file != "size":
            directory['size'] += directory[file]['size']
    if directory['size'] <= 100000:
        dir_sizes += directory['size']

    return directory


def run(data):
    global console
    console = data
    global dir_sizes
    dir_sizes = 0
    dir_tree = {}

    line = data.pop(0)
    dir_tree["/"] = run_cd()

    return dir_sizes
