from utils.input_reader import ingest
import part1
import part2

# format options: raw, line, tuple, list, grid
file_format = "line"
base_type = int
example_result_1 = None
example_result_2 = None


def test_part1():
    if example_result_1:
        # do test on example data
        example_data = ingest("example.input", file_format, base_type=base_type)

        assert part1.run(example_data) == example_result_1

        # if test passed, do the real input
        real_data = ingest("real.input", file_format, base_type=base_type)

        print("\nPart 1 Results\n----------------\n")
        print(part1.run(real_data))


def test_part2():
    if example_result_2:
        # do test on example data
        example_data = ingest("example.input", file_format, base_type=base_type)

        assert part2.run(example_data) == example_result_2

        # if test passed, do the real input
        real_data = ingest("real.input", file_format, base_type=base_type)

        print("\nPart 2 Results\n----------------\n")
        print(part2.run(real_data))
