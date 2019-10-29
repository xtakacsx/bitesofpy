from itertools import accumulate


def running_mean(sequence):
    # total = 0
    # for value, element in enumerate(sequence):
    #     total += element
    #     yield round(total / (value + 1), 2)
    for i, num in enumerate(accumulate(sequence), 1):
        print(i, num)
        yield round(num / i, 2)
