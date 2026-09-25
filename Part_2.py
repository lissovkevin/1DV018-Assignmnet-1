import random
import time
import matplotlib.pyplot as plt
import math


def selection_sort(lst):
    lst_copy = lst.copy()
    for i in range(len(lst_copy) - 1):
        min_index = i
        for j in range(i + 1, len(lst_copy)):
            if lst_copy[j] < lst_copy[min_index]:
                min_index = j
        lst_copy[i], lst_copy[min_index] = lst_copy[min_index], lst_copy[i]
    return lst_copy


def bubble_sort(lst):
    lst_copy = lst.copy()
    for i in range(len(lst_copy) - 1):
        swapped = False
        for j in range(len(lst_copy) - i - 1):
            if lst_copy[j] > lst_copy[j + 1]:
                lst_copy[j], lst_copy[j + 1] = lst_copy[j + 1], lst_copy[j]
                swapped = True
        if not swapped:
            break
    return lst_copy


def insertion_sort(lst):
    lst_copy = lst.copy()
    for i in range(1, len(lst_copy)):
        key = lst_copy[i]
        j = i - 1
        while j >= 0 and lst_copy[j] > key:
            lst_copy[j + 1] = lst_copy[j]
            j = j - 1
        lst_copy[j + 1] = key
    return lst_copy


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]

    smaller = [x for x in lst if x < pivot]
    same = [x for x in lst if x == pivot]
    bigger = [x for x in lst if x > pivot]

    return quick_sort(smaller) + same + quick_sort(bigger)


def bucket_sort(lst):
    if len(lst) <= 1:
        return lst

    num_buckets = len(lst)
    buckets = [[] for _ in range(num_buckets)]
    min_value, max_value = min(lst), max(lst)

    for num in lst:
        index = int(((num - min_value) / (max_value - min_value + 1) * num_buckets))
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        for value in bucket:
            result.append(value)
    return result


def radix_sort(lst):
    lst_copy = lst.copy()

    if len(lst_copy) <= 1:
        return lst_copy

    max_value = max(lst_copy)
    exp = 1
    while max_value // exp > 0:
        buckets = [[] for i in range(10)]

        for num in lst_copy:
            index = (num // exp) % 10
            buckets[index].append(num)

        lst_copy.clear()
        for bucket in buckets:
            for num in bucket:
                lst_copy.append(num)
        exp = exp * 10
    return lst_copy


def lin_reg(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    lst_xy = []
    for i in range(n):
        lst_xy.append(x[i] * y[i])
    sum_xy = sum(lst_xy)

    lst_x2 = []
    for i in range(n):
        lst_x2.append(x[i] ** 2)
    sum_x2 = sum(lst_x2)

    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x) ** 2)
    m = (sum_y - k * sum_x) / n

    return m, k


sort_sizes = list(range(2000, 10001, 571))
merge_quick_sizes = list(range(100000, 2000000, 135714))

selection_times = []
for n in sort_sizes:
    selection_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(2000, 10000))
        start = time.time()
        result = selection_sort(random_lst)
        end = time.time()
        selection_times[-1].append(end - start)
        print(f"selection n={n}: {end - start:.4f}")

bubble_times = []
for n in sort_sizes:
    bubble_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(2000, 10000))
        start = time.time()
        result = bubble_sort(random_lst)
        end = time.time()
        bubble_times[-1].append(end - start)
        print(f"bubble n={n}: {end - start:.4f}")

insertion_times = []
for n in sort_sizes:
    insertion_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(2000, 10000))
        start = time.time()
        result = insertion_sort(random_lst)
        end = time.time()
        insertion_times[-1].append(end - start)
        print(f"insertion n={n}: {end - start:.4f}")

selection_avg = [sum(rad) / len(rad) for rad in selection_times]
bubble_avg = [sum(rad) / len(rad) for rad in bubble_times]
insertion_avg = [sum(rad) / len(rad) for rad in insertion_times]


merge_times = []
for n in merge_quick_sizes:
    merge_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(2000, 10000))
        start = time.time()
        result = merge_sort(random_lst)
        end = time.time()
        merge_times[-1].append(end - start)
        print(f'merge n={n}: {end - start:.4f}')

quick_times = []
for n in merge_quick_sizes:
    quick_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(2000, 10000))
        start = time.time()
        result = quick_sort(random_lst)
        end = time.time()
        quick_times[-1].append(end - start)
        print(f'quick n={n}: {end - start:.4f}')

merge_avg = [sum(rad) / len(rad) for rad in merge_times]
quick_avg = [sum(rad) / len(rad) for rad in quick_times]

plt.plot(merge_quick_sizes, merge_avg, '+', label='Merge Sort', color='purple')
plt.plot(merge_quick_sizes, quick_avg, 'x', label='Quick Sort', color='orange')
plt.xlabel('n (liststorlek)')
plt.ylabel('Genomsnittlig körtid (s)')
plt.title('Figure 1: Jämförelse O(n·log n) algoritmer')
plt.legend()
plt.show()

log_n_mq = [math.log(n) for n in merge_quick_sizes]
log_t_merge = [math.log(t) for t in merge_avg]
log_t_quick = [math.log(t) for t in quick_avg]

m_merge, k_merge = lin_reg(log_n_mq, log_t_merge)
m_quick, k_quick = lin_reg(log_n_mq, log_t_quick)

print(f'k_merge = {k_merge:.3f}')
print(f'k_quick = {k_quick:.3f}')


fitted_merge = [m_merge + k_merge * x for x in log_n_mq]
fitted_quick = [m_quick + k_quick * x for x in log_n_mq]

plt.scatter(log_n_mq, log_t_merge, marker='+', color='purple', label='Merge Sort')
plt.scatter(log_n_mq, log_t_quick, marker='x', color='orange', label='Quick Sort')
plt.plot(log_n_mq, fitted_merge, color='purple')
plt.plot(log_n_mq, fitted_quick, color='orange')
plt.xlabel('log(n)')
plt.ylabel('log(körtid)')
plt.title('Figure 2: Log-log plot för O(n·log n) algoritmer')
plt.legend()
plt.show()

plt.plot(sort_sizes, selection_avg, "+", label="Selection Sort", color="red")
plt.plot(sort_sizes, insertion_avg, "x", label="Insertion Sort", color="blue")
plt.plot(sort_sizes, bubble_avg, "v", label="Bubble Sort", color="green")
plt.xlabel("n (liststorlek)")
plt.ylabel("Genomsnittlig körtid (s)")
plt.title("Figure 1: Jämförelse O(n²) algoritmer")
plt.legend()
plt.show()

log_n = [math.log(n) for n in sort_sizes]

log_t_selection = [math.log(t) for t in selection_avg]
log_t_bubble = [math.log(t) for t in bubble_avg]
log_t_insertion = [math.log(t) for t in insertion_avg]

m_selection, k_selection = lin_reg(log_n, log_t_selection)
m_bubble, k_bubble = lin_reg(log_n, log_t_bubble)
m_insertion, k_insertion = lin_reg(log_n, log_t_insertion)

print(f'k_selection = {k_selection:.3f}')
print(f'k_bubble = {k_bubble:.3f}')
print(f'k_insertion = {k_insertion:.3f}')

fitted_selection = [m_selection + k_selection * x for x in log_n]
fitted_bubble = [m_bubble + k_bubble * x for x in log_n]
fitted_insertion = [m_insertion + k_insertion * x for x in log_n]

plt.scatter(log_n, log_t_selection, marker='+', color='red', label='Selection')
plt.scatter(log_n, log_t_insertion, marker='x', color='blue', label='Insertion')
plt.scatter(log_n, log_t_bubble, marker='v', color='green', label='Bubble')

plt.plot(log_n, fitted_selection, color='red')
plt.plot(log_n, fitted_insertion, color='blue')
plt.plot(log_n, fitted_bubble, color='green')

plt.xlabel('log(n)')
plt.ylabel('log(körtid)')
plt.title('Figure 2: Log-log plot för O(n²) algoritmer')
plt.legend()
plt.show()
