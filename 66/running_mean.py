def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    total = 0
    for value, element in enumerate(sequence):
        total += element
        yield round(total / (value + 1), 2)
