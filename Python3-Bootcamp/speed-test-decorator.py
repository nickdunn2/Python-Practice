from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = fn(*args, **kwargs)
        total_time = time() - start_time
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {total_time}")
        return res

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])


print(sum_nums_gen())
print(sum_nums_list())
