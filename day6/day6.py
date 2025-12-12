import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import operator
ops = { "+": operator.add, "-": operator.sub , "*": operator.mul, "/": operator.truediv} 


def load_space_separated(path):
    """
    Read 'dataExemple.txt' (or given path) as space-separated values and
    return a NumPy array. If rows have equal column count, returns a 2D
    str array; otherwise returns an object array of row lists.
    """
    data_file = Path(__file__).with_name(path)
    print(data_file)
       
    with open(data_file, "r", encoding="utf-8") as f:
        rows = [line.strip().split() for line in f if line.strip()]

    lengths = {len(r) for r in rows}
    
    if len(lengths) == 1:
        return np.array(rows, dtype=str)
    else:
        return np.array(rows, dtype=object)

if __name__ == "__main__":
    data_array = load_space_separated("dataExemple.txt")
    print("Loaded array shape:", data_array.shape)
    print(data_array)
    print(data_array.shape)
    total_res = 0 
    
    for i in range(data_array.shape[1]):
        operator_str = data_array[data_array.shape[0]-1][i]
        print(str(operator_str))
        res = int(data_array[0][i])
        for j in range(1, data_array.shape[0]-1):
            print(data_array[j][i])
            res = ops[operator_str](res, int(data_array[j][i]))
            
        print(res)
        total_res += res
    
    print(f"Total result: {total_res}")
            


##### Part 2 #####

    total_res = 0 
    # Read file and store each character (including spaces) in a 2D numpy array
    data_file = Path(__file__).with_name("data.txt")
    with open(data_file, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        char_array = np.array([[]], dtype=str)
    else:
        max_len = max(len(l) for l in lines)
        padded = [l + " " * (max_len - len(l)) for l in lines]
        char_array = np.array([list(row) for row in padded], dtype=str)

    print("Character grid shape:", char_array.shape)
    print(char_array)
    
    # identify columns that are all spaces (separators)
    sep_cols = np.all(char_array == " ", axis=0)

    # indices of columns that are not separators
    non_sep_idx = np.where(~sep_cols)[0]

    sub_arrays = []
    if non_sep_idx.size:
        # find contiguous runs of non-separator columns
        run_start = non_sep_idx[0]
        prev = non_sep_idx[0]
        for idx in non_sep_idx[1:]:
            if idx != prev + 1:
                sub_arrays.append(char_array[:, run_start:prev + 1])
                run_start = idx
            prev = idx
        # add final run
        sub_arrays.append(char_array[:, run_start:prev + 1])

    print(f"Split into {len(sub_arrays)} sub-arrays.")
    for i, sub in enumerate(sub_arrays):
        print(f"Sub-array {i}: shape={sub.shape}")
        print(sub)

        operator_str = sub[-1, 0]
        print(str(operator_str))
        res = -1
        for col in range(sub.shape[1]):
            number = ''
            for row in range(sub.shape[0]-1):
                number += sub[row, col]
            print(f"Column {col}: {number}")
            if res == -1:
                res = int(number)
            else:
                res = ops[operator_str](res, int(number))
        print(f"Result for sub-array {i}: {res}")
        total_res += res
    print(f"Total result for all sub-arrays: {total_res}")