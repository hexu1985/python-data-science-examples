#P73: Find the variance and standard deviation

'''
Find the variance and standard deviation of a list of numbers
'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # calculate the mean
    mean = s/N
    return mean

def find_differences(numbers):
    # find the mean
    mean = calculate_mean(numbers)
    # find the differences from the mean
    diff = []
    
    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
    # find the list of differences
    diff = find_differences(numbers)
    # find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    #find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))
    std = variance**0.5
    print('The standard deviation of the list of numbers is {0}'.format(std))



