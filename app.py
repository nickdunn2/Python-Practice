
def get_total_x(a, b):
    a_stop = max(a)
    counters = []

    while a_stop <= min(b):
        counters.append(a_stop)
        a_stop += max(a)

    # good_with_a = [num for num in a if nu]

    return counters


print(get_total_x([2, 6], [24, 36]))  # 2 (6, 12)
print(get_total_x([2, 4], [16, 32, 96]))  # 3 (4, 8, 16)
