import random
import time
import matplotlib.pyplot as plt
import math


def threesum_brute(lst, sum=0):
    sumZero = []
    seen_triples = set()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                triple = tuple(sorted((lst[i], lst[j], lst[k])))
                if lst[i] + lst[j] + lst[k] == sum and triple not in seen_triples:
                    sumZero.append((triple))
                    seen_triples.add(triple)
    return sumZero


def threesum_cache(lst, sum=0):
    sumZero = []
    seen_triples = set()

    for i in range(len(lst)):
        seen = set()
        for j in range(i + 1, len(lst)):
            needed = sum - lst[i] - lst[j]
            if needed in seen:
                triple = tuple(sorted((lst[i], lst[j], needed)))
                if triple not in seen_triples:
                    sumZero.append(triple)
                    seen_triples.add(triple)
            seen.add(lst[j])
    return sumZero


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
        print(f"{end - start:.10f}")

cache_sizes = list(range(2300, 14001, 835))
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
        print(f"{end - start:.10f}")


plt.plot(brute_sizes, [rad[0] for rad in brute_times], label="Körning 1", color="blue")
plt.plot(brute_sizes, [rad[1] for rad in brute_times], label="Körning 2", color="red")
plt.plot(brute_sizes, [rad[2] for rad in brute_times], label="Körning 3", color="green")
plt.xlabel("Brute Sizes")
plt.ylabel("Brute times")
plt.title("Figure 1 Brute")
plt.legend()
plt.show()

brute_avg = [sum(rad) / len(rad) for rad in brute_times]

plt.plot(brute_sizes, brute_avg)
plt.xlabel("Brute Sizes")
plt.ylabel("Averege brute time")
plt.title("Figure 1a Avg Brute")
plt.show()

plt.plot(cache_sizes, [rad[1] for rad in cache_times], label="Körning 2", color="red")
plt.plot(cache_sizes, [rad[2] for rad in cache_times], label="Körning 3", color="green")
plt.plot(cache_sizes, [rad[0] for rad in cache_times], label="Körning 1", color="blue")
plt.xlabel("Cache Sizes")
plt.ylabel("Cache times")
plt.title("Figure 1 Cache")
plt.legend()
plt.show()

cache_avg = [sum(rad) / len(rad) for rad in cache_times]

plt.plot(cache_sizes, cache_avg)
plt.xlabel("Cache Sizes")
plt.ylabel("Averege cache time")
plt.title("Figure 1 Avg Cache")
plt.show()


log_n_brute = []
for n in brute_sizes:
    log_n_brute.append(math.log(n))

log_t_brute = []
for t in brute_avg:
    log_t_brute.append(math.log(t))

m_brute, k_brute = lin_reg(log_n_brute, log_t_brute)
print(f"k = {k_brute:.3f}")

log_n_cache = []
for n in cache_sizes:
    log_n_cache.append(math.log(n))

log_t_cache = []
for t in cache_avg:
    log_t_cache.append(math.log(t))

m_cache, k_cache = lin_reg(log_n_cache, log_t_cache)
print(f"k = {k_cache:.3f}")

fitted_brute = [m_brute + k_brute * x for x in log_n_brute]
plt.scatter(log_n_brute, log_t_brute, label="Uppmätt Data")
plt.plot(log_n_brute, fitted_brute, label="Anpassad Linje", color="red")
plt.xlabel("log(n)")
plt.ylabel("log(körtid)")
plt.title("Figure 2b - Brute")
plt.legend()
plt.show()

fitted_cache = [m_cache + k_cache * x for x in log_n_cache]
plt.scatter(log_n_cache, log_t_cache, label="Uppmätt Data")
plt.plot(log_n_cache, fitted_cache, label="Anpassad Linje", color="red")
plt.xlabel("log(n)")
plt.ylabel("log(körtid)")
plt.title("Figure 2b - Cache")
plt.legend()
plt.show()
