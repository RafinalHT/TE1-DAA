import tracemalloc
import time

def main(array):
    SL = 0
    SR = len(array) - 1
    while SL < SR:
        mid = (SR - SL) // 2
        for i in range(SL, SL + mid + 1):
            j = SR - (i - SL)
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        if array[SL] == array[SR]:
            if is_equal(array, SL, SR) == -1:
                return
        if array[SL] > array[SR]:
            array[SL], array[SR] = array[SR], array[SL]
        if SR - SL >= 100:
            for i in range(SL + 1, SR - SL):
                if array[SR] < array[i]:
                    array[SR], array[i] = array[i], array[SR]
                elif array[SL] > array[i]:
                    array[SL], array[i] = array[i], array[SL]
        else:
            i = SL + 1
        LC = array[SL]
        RC = array[SR]
        while i < SR:
            CurrItem = array[i]
            if CurrItem >= RC:
                array[i] = array[SR - 1]
                ins_right(array, CurrItem, SR, len(array) - 1)
                SR -= 1
            elif CurrItem <= LC:
                array[i] = array[SL + 1]
                ins_left(array, CurrItem, SL, SL + 1)
                SL += 1
                i += 1
            else:
                i += 1
        SL += 1
        SR -= 1

def is_equal(array, SL, SR):
    for k in range(SL + 1, SR):
        if array[k] != array[SL]:
            array[k], array[SL] = array[SL], array[k]
            return k
    return -1

def ins_right(array, CurrItem, SR, right):
    j = SR
    while j <= right and CurrItem > array[j]:
        array[j - 1] = array[j]
        j += 1
    array[j - 1] = CurrItem

def ins_left(array, CurrItem, SL, left):
    j = SL
    while j >= left and CurrItem < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = CurrItem

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

# https://www.geeksforgeeks.org/counting-sort/
def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)
 
    # Initializing count_array with 0
    count_array = [0] * (M + 1)
 
    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1
 
    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array


def Complexity(file_path, algorithm):
    tracemalloc.start()
    file = open(file_path)
    file_content = file.read().splitlines()
    file.close()
    numbers = [int(line) for line in file_content]

    if algorithm == "BCIS":
        start_time = time.perf_counter()
        main(numbers)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
    elif algorithm == "CS":
        start_time = time.perf_counter()
        output_numbers = count_sort(numbers)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
    
    print(f"Running time {file_path} make {algorithm}  {execution_time} ms")

    print("Memory :", tracemalloc.get_traced_memory())
    tracemalloc.reset_peak()
    tracemalloc.stop()
    print()

file_paths = ["reversed_sedang.txt","random_besar.txt", "sorted_besar.txt", "reversed_besar.txt"]

for file_path in file_paths:
    Complexity(file_path, "BCIS")
    Complexity(file_path, "CS")
    print()
