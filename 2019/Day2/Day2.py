import sys

intcode_raw = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 2, 10, 23, 27, 1, 27, 6, 31, 1,
           13, 31, 35, 1, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 47, 9, 51, 2, 51, 13, 55, 1, 5, 55, 59, 2, 59, 9,
           63, 1, 13, 63, 67, 2, 13, 67, 71, 1, 71, 5, 75, 2, 75, 13, 79, 1, 79, 6, 83, 1, 83, 5, 87, 2, 87, 6, 91, 1,
           5, 91, 95, 1, 95, 13, 99, 2, 99, 6, 103, 1, 5, 103, 107, 1, 107, 9, 111, 2, 6, 111, 115, 1, 5, 115, 119, 1,
           119, 2, 123, 1, 6, 123, 0, 99, 2, 14, 0, 0]


for noun in range(99):
    for verb in range(99):
        i = 0
        intcode = intcode_raw.copy()
        intcode[1] = noun
        intcode[2] = verb
        while i <= len(intcode):
            code = intcode[i]
            if code == 99:
                if intcode[0] == 19690720:
                    print(f"noun:{noun} - verb:{verb} - output:{intcode[0]}")
                    sys.exit()
                else:
                    break

            elif code == 1:
                pos1 = intcode[i + 1]
                pos2 = intcode[i + 2]
                out = intcode[i + 3]
                intcode[out] = intcode[pos1] + intcode[pos2]
                i += 4
            elif code == 2:
                pos1 = intcode[i + 1]
                pos2 = intcode[i + 2]
                out = intcode[i + 3]
                intcode[out] = intcode[pos1] * intcode[pos2]
                i += 4
            else:
                print(f"{i} - {code}")
                break

