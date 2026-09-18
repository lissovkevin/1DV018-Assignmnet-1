import random


def threesum_brute(lst, sum=0):
    sumZero = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                triple = tuple(sorted((lst[i], lst[j], lst[k])))
                if lst[i] + lst[j] + lst[k] == sum and triple not in sumZero:
                    sumZero.append((triple))

    return sumZero


for _ in range(3):
    n = 15
    random_lst = []
    for _ in range(n):
        random_lst.append(random.randint(-10 * n, 10 * n))
    print(random_lst)
    print(threesum_brute(random_lst))
