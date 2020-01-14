import random

def partition(iterable, idx_start, idx_end):
    idx_rand = random.randint(idx_start, idx_end)
    iterable[idx_start], iterable[idx_rand] = iterable[idx_rand], iterable[idx_start]

    pivot = iterable[idx_start]
    print("Pivot", pivot)
    idx_pivot = idx_start + 1

    for idx_bound in range(idx_start + 1, idx_end + 1):
        if iterable[idx_bound] <= pivot:
            iterable[idx_bound], iterable[idx_pivot] = iterable[idx_pivot], iterable[idx_bound]
            idx_pivot += 1
    
    iterable[idx_start], iterable[idx_pivot-1] = iterable[idx_pivot-1], iterable[idx_start]
    print(iterable)

    return idx_pivot-1

def quicksort(iterable, idx_start=0, idx_end=None):
    if idx_end is None:
        idx_end = len(iterable)-1

    if idx_start >= idx_end:
        return
    idx_pivot = partition(iterable, idx_start, idx_end)
    quicksort(iterable, idx_start, idx_pivot-1)
    quicksort(iterable, idx_pivot+1, idx_end)

array = [2, 54, 351, 8, 3, 684, 654, 65, 552, 0, 1, 63, 1, 963, 82, 36, 92, 5, 56214, 2682, 3, 8452]
quicksort(array)
print(array)