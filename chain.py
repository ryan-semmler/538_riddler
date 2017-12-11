import random


upto = 1000


def factors(n):
    return [i for i in range(1, n + 1) if not n % i]


def multiples(n):
    return [n * i for i in range(1, int(upto / n + 1))]


def numbers(n):
    return sorted(list(set(factors(n) + multiples(n))))


def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if not n % i:
            return False
    return True


# best list, up to 100: [61, 1, 85, 17, 34, 68, 4, 52, 26, 78, 6, 48, 24, 72, 36, 12, 60, 30, 15, 75, 25, 50, 10, 100, 20, 40, 80, 16, 64, 32, 96, 8, 56, 28, 84, 42, 21, 63, 9, 81, 27, 54, 18, 90, 45, 3, 99, 33, 66, 22, 44, 88, 11, 77, 7, 49, 98, 14, 70, 35, 5, 95, 19, 38, 76, 2, 92, 46, 23, 69]
primes = [i for i in range(1, upto + 1) if is_prime(i)]
starting_numbers = [i for i in range(int(upto / 2) + 1, upto + 1) if is_prime(i)]
dic = {i: numbers(i) for i in range(1, upto + 1)}


def get_path(dic, start=[]):
    """
    Default: starting from random choice from starting_numbers.
    With 'start' argument included, beginning with that list
    :param dic:
    :return:
    """
    if not start:
        start = [random.sample(starting_numbers, 1)[0]]
    path = start
    count = 1
    while True:
        next_steps = [thing for thing in dic[path[-1]] if thing not in path and thing not in primes]
        if len(next_steps) == 0:
            next_steps = [thing for thing in dic[path[-1]] if thing not in path]
        if len(next_steps) > 0:
            path.append(random.sample(next_steps, 1)[0])
        elif count <= 5:
            path.pop()
            path.pop()
            count += 1
        else:
            return path


longest = []
while True:
    path = get_path(dic)
    if len(path) > len(longest):
        longest = path
        print(f"\n\nWith numbers up to {upto}:\nLength of longest path: {len(longest)}\n{path}")
