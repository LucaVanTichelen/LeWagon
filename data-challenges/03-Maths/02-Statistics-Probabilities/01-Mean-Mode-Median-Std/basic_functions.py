'''returns the mean of the observations'''

def my_mean(samples):
    '''returns the mean of the observations'''
    return sum(samples) / len(samples)

def my_standard_deviation(samples):
    '''returns the standard deviation of the observations'''
    return (sum([(sample - my_mean(samples)) ** 2 for sample in samples])/
            (len(samples) - 1)) ** 0.5


def my_mode(samples):
    '''returns the mode of the observations'''
    return max(set(samples), key = samples.count)

print(my_mode([0, 1, 2, 3, 3, 1, 4, 5, 6, 7, 1]))

def my_multimodes(samples):
    '''returns the modes of the observations as a sorted list'''
    return samples

def my_median(samples):
    '''returns the median of the observations'''
    ordered = sorted(samples)
    if len(samples) % 2 == 1:
        return ordered[((len(samples) + 1) // 2) - 1]
    return (ordered[len(samples) // 2 - 1] + ordered[(len(samples) // 2)]) / 2
