def run(data):
    elves = []
    elf = []
    for item in data:
        if not item:
            elves.append(sum(elf))
            elf = []
        else:
            elf.append(int(item))
    elves.append(sum(elf))

    return max(elves)
