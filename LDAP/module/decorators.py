import time


def print_out(func):
    def f(x, y, z):
        print('Start task.')
        a = func(x, y, z)
        print('End task.')
        input()
        return a
    return f



def timer(func):
    def f(x, y):
        start = time.time()
        a = func(x, y)
        end= time.time()
        print('Execution time: {} (s).'.format(end - start))
        return a
    return f


