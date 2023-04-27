import math
import time
import multiprocessing


def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('time: ', time.time() - start)

    return inner


def ex(num):
    return str(math.sqrt(math.sqrt(math.sqrt(num / 2) * 10 / 15))) + 'H'


@time_decor
def main_process():
    print('main_process')
    r = range(10000000)
    with open('file1.txt', 'w') as f:
        for p in r:
            print(ex(p), file=f)


# main_process()

@time_decor
def main_process_all_cpu():
    print('main_process_all_cpu')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')
    with multiprocessing.Pool(count) as p:
        r = range(10000000)
        with open('file2.txt', 'w') as f:
            tasks = p.map(ex, r)
            for task in tasks:
                print(task, file=f)


if __name__ == '__main__':
    main_process_all_cpu()
