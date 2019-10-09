def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if start is not 0:
        print(start)
        countdown_recursive(start - 1)
    else:
        print("time is up")