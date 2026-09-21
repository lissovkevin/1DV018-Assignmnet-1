import random
import time
import matplotlib.pyplot as plt


def threesum_brute(lst, sum=0):
    sumZero = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                triple = tuple(sorted((lst[i], lst[j], lst[k])))
                if lst[i] + lst[j] + lst[k] == sum and triple not in sumZero:
                    sumZero.append((triple))
    return sumZero


def threesum_cache(lst, sum=0):
    sumZero = []

    for i in range(len(lst)):
        seen = set()
        for j in range(i + 1, len(lst)):
            needed = sum - lst[i] - lst[j]
            if needed in seen:
                triple = tuple(sorted((lst[i], lst[j], needed)))
                if triple not in sumZero:
                    sumZero.append(triple)
            seen.add(lst[j])
    return sumZero


brute_sizes = list(range(200, 696, 35))
brute_times = []
for n in brute_sizes:
    brute_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(-10 * n, 10 * n))
        start = time.time()
        result = threesum_brute(random_lst)
        end = time.time()
        brute_times[-1].append(end - start)
        print(f'{end - start:.10f}')

cache_sizes = list(range(950, 2476, 108))
cache_times = []
for n in cache_sizes:
    cache_times.append([])
    for _ in range(3):
        random_lst = []
        for _ in range(n):
            random_lst.append(random.randint(-10 * n, 10 * n))
        start = time.time()
        result = threesum_cache(random_lst)
        end = time.time()
        cache_times[-1].append(end - start)
        print(f'{end - start:.10f}')

plt.plot(brute_sizes, [rad[0] for rad in brute_times], label='Körning 1', color='blue')
plt.plot(brute_sizes, [rad[1] for rad in brute_times], label='Körning 2', color='red')
plt.plot(brute_sizes, [rad[2] for rad in brute_times], label='Körning 3', color='green')
plt.xlabel('Brute Sizes')
plt.ylabel('Brute times')
plt.legend()
plt.show()
