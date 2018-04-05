def spiral_matrix(m, n):
    """
    Given a dimensions of a matrix (m,n) return a clockwise 
    spiral matrix of those dimensions which can be indexed using standard i,j notation
    e.g:
    >>> spiral_matrix(3,4)
    returns 
    [
        [0,  1,  2, 3],
        [9, 10, 11, 4],
        [8,  7,  6, 5]
    ]
    """
    pass

"""
Implement the following methods to create a price tracker that can
give you the price of a stock for a given time by recording ticker events
"""
class PriceTracker(object):

    def __init__(self, initial_timestamp, initial_price):
        """
        Takes t0 timestamp and the initial price for the stock STK
        """
        pass

    def process_ticker_for(self, timestamp, price):
        """
        Will be called to represent the live stock ticker with the a
        timestamp representing the time the new price is valid from

        e.g. if we had a stock which ticked every minute and the following
        sequence...
        2018-04-05 09:00:00.0 £1.00
        2018-04-05 09:01:00.0 £1.50
        2018-04-05 09:02:00.0 £1.25

        Then the prices in the range [9:00, 9:01) (inclusive start exclusive end)
        would be £1.

        Extension - what if it is not guaranteed that the each consequitive process_ticker_for 
        method call the timestamp increases.
        """
        pass
        #TODO

    def get_price_at(self, timestamp):
        """
        Returns the price of STK at a given time, should return None is
        it is not possible to find the price
        """
        pass
        #TODO


def sort_integer_list(lst):
    """
    Efficiently sort a list of integers of length N where each 
    element 0 <= n_i < 100 and 500 < N < 10^6

    FYI - the sorted() method uses 'Timsort' - is a variant of 
    insertion and merge sort.
    """