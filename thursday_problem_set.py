import doctest

def efficient_operation(operations, N):
    """
    Consider a list which represent K instances of an operation, called 'increment range' 
    which takes the form 
        operations = [(start1,end1,delta1), ... (start_i, end_i, delta_i) ...]
    where len(operations) = K.

    A single instance of 'increment range' acts on a list of length N and increments the value 
    for indices between start_i and end_i (inclusive) by delta_i

    e.g: calling 
    >>> efficient_operation([(0,5,3),(4,6,2)], 8)
    would update target_list to be [3, 3, 3, 3, 5, 5, 2, 0] hence the function should return 5

    Complete the code to efficiently apply the operations to target_list 
    (instantiated to an array of zeros) and return the maximum value from the result
    """
    target_list = [0] * N
    maximum = None
    #Start applying operations
    #TODO
    #Finished applying operations
    return maximum


def get_pairs_that_sum(numbers, target_sum):
    """
    Given a list of integers 'numbers' return a list of combinations of pairs 
    of numbers (tuples of length 2) that sum to 'target_sum'

    e.g. calling
    >>> get_pairs_that_sum([0,1,2,2,3,4], 4)
    would return [(0,4), (1,3), (2,2)]
    """

    pairs_that_sum = []
    #Populate pairs that sum
    #TODO
    #Returning result
    return pairs_that_sum


def get_tuples_that_sum(numbers, target_sum, N):
    """
    Extend get_pairs_that_sum but rather that finding pairs of number that sum to 
    target_sum, find all combinations of length N
    e.g. calling 
    >>> get_tuples_that_sum([0,1,2,2,3,4], 4, 2) would result in the same as calling
    >>> get_pairs_that_sum([0,1,2,2,3,4], 4)

    however calling 
    >>> get_tuples_that_sum([0,1,2,2,3,4], 4, 3)
    would return [(0,1,3), (0,2,2)] 
    """
    combinations_of_tuples_that_sum = []
    #Populate combinations_of_tuples_that_sum
    #TODO
    #Returning result
    return combinations_of_tuples_that_sum

#if __name__ == "__main__":
#    doctest.testmod()