from pathlib import Path
from typing import List

def load_lines_as_char_lists(path: Path) -> List[List[str]]:
    """
    Open the given file and return a list of lists of characters.
    Each inner list represents one line; newline characters are removed.
    """
    with path.open('r', encoding='utf-8') as f:
        return [list(line.rstrip('\n')) for line in f]

def find_highest(start: int = 0, drop: int = 11, remaining: int = 12) -> List[str]:
            # stop when we've found enough numbers or there is nothing left to search
            if remaining == 0:
                return []
            end = len(nums) - drop
            if start >= end:
                return []
            # search the slice start:end, choose first occurrence on ties
            slice_nums = nums[start:end]
            max_val = max(slice_nums)
            idx_in_slice = slice_nums.index(max_val)
            abs_idx = start + idx_in_slice
            # include this digit and recurse: next search starts after abs_idx, drop one fewer from the end
            return [str(max_val)] + find_highest(abs_idx + 1, drop - 1, remaining - 1)


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data.txt"
    try:
        battery_pack = load_lines_as_char_lists(data_file)
        print(battery_pack)  # or do further processing
    except FileNotFoundError:
        print(f"File not found: {data_file}")

### Part 1 #####

    total_voltage = 0
    for pack in battery_pack:
        nums = [int(c) for c in pack]
        max_val1 = max(nums[:-1])
        max_idx = nums.index(max_val1)
        print(f"max value: {max_val1} at index: {max_idx}")

        pack = pack[max_idx + 1:] 
        nums = [int(c) for c in pack]
        max_val2 = max(nums)
        print(f"second max value: {max_val2}")
        print(f"Number found : {max_val1}{max_val2}")
        total_voltage += int(f"{max_val1}{max_val2}")

    print(f"Total voltage: {total_voltage}")

#### Part 2 #####

    print('\nPart 2\n')

    total_voltage = 0
    for pack in battery_pack:
        nums = [int(c) for c in pack]
        digits = find_highest()
        if len(digits) < 12:
            print(f"Warning: only found {len(digits)} digits in pack {''.join(pack)}")
        number_str = ''.join(digits) if digits else "0"
        print(f"Number found: {number_str}")
        total_voltage += int(number_str)

    print(f"Total voltage: {total_voltage}")