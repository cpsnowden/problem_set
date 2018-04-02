import doctest


def print_hello_world():
    """
    Prints Hello World

    """
    print("Hello World")


def get_top_n_of_users_by_score(users_and_score, n):
    """
    Returns a list of users' names which have the top n scores ordered alphabetically, consider joint scores!
    users_and_score is in the format [(user1,score),(user_2,score)]
    >>> get_top_n_of_users_by_score([("Adam", 10),("Charlotte", 12),("Bob", 8),("Rachel", 9)], 2)
    ['Adam', 'Charlotte']
    >>> get_top_n_of_users_by_score([("Adam", 10),("Charlotte", 12),("Bob", 8),("Rachel", 9), ("Victoria", 10)], 2)
    ['Adam', 'Charlotte', 'Victoria']
    >>> get_top_n_of_users_by_score([("Charlotte", 12)], 2)
    ['Charlotte']
    """
    nth_score = sorted(set([user_and_score[1] for user_and_score in users_and_score]), reverse=True )[:n][-1]
    return sorted([user_and_score[0] for user_and_score in users_and_score if user_and_score[1] >= nth_score])

def is_power_of_ten(number: float):
    """
    Returns 'True' is number is a multiple of 10 else 'False'
    >>> is_power_of_ten(1)
    True
    >>> is_power_of_ten(10)
    True
    >>> is_power_of_ten(20)
    False
    >>> is_power_of_ten(100)
    True
    >>> is_power_of_ten(0)
    True
    >>> is_power_of_ten(0.1)
    True
    """
    import math
    return number == 0 or math.log10(number).is_integer()


def reverse_a_word(string: str):
    """
    Reverses the characters in a string
    >>> reverse_a_word("")
    ''
    >>> reverse_a_word("abcdef")
    'fedcba'
    >>> reverse_a_word("aibohphobia")
    'aibohphobia'
    """
    return string[::-1]


def reverse_a_sentence(sentence: str):
    """
    Reverses a sentence
    >>> reverse_a_sentence("")
    ''
    >>> reverse_a_sentence("a sentence")
    'ecnetnes a'
    """
    return sentence[::-1]


def anagram(first_string: str, second_string: str):
    """
    Returns 'True' if first_string is an anagram of second_string, should be case insensitive
    >>> anagram("","")
    True
    >>> anagram("abc","b")
    False
    >>> anagram("abc def","d efabc")
    True
    >>> anagram("Welcome","welcome")
    True
    """
    if len(first_string) != len(second_string):
        return False
    character_counts = {}
    for f_char, s_char in zip(first_string, second_string):
        lf_char = f_char.lower()
        ls_char = s_char.lower()
        f_char_count = character_counts.get(lf_char, 0)
        character_counts[lf_char] = f_char_count + 1
        s_char_count = character_counts.get(ls_char, 0)
        character_counts[ls_char] = s_char_count - 1
    return not any(character_counts.values())
    # Could also use sort, depending on performance requirements


def sort_list_of_sorted_lists(list_of_lists):
    """
    Returns a sorted (in ascending order) list containing all the members of each sublist contained in list_of_lists
     >>> sort_list_of_sorted_lists([[2],[],[3,9,12],[-1,8,15]])
     [-1, 2, 3, 8, 9, 12, 15]
    """
    result = []
    while any(list_of_lists):
        index = 0
        cur_min = None
        for i, l in enumerate(list_of_lists):
            if len(l) and (cur_min is None or l[0] < cur_min):
                index = i
                cur_min = l[0]
        result.append(list_of_lists[index].pop(0))
    # better to use a heap for O(nlogn) or heapq.merge
    return result


def get_all_subsets_of_length(a_set, n):
    """
    Returns all subsets of 'a_set' that are of length n
    >>> sorted(get_all_subsets_of_length([1,3,5,7,8],3))
    [[1, 3, 5], [1, 3, 7], [1, 3, 8], [1, 5, 7], [1, 5, 8], [1, 7, 8], [3, 5, 7], [3, 5, 8], [3, 7, 8], [5, 7, 8]]
    """
    if n == 0:
        return [[]]
    result = []
    for i in range(len(a_set)):
        for ss in get_all_subsets_of_length(a_set[i + 1:], n - 1):
            result.append([a_set[i]] + ss)
    return result


def fibonacci(n: int):
    """
    Returns the nth number in the fibonacci sequence, what should happen if n is an invalid number...
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(6)
    8
    >>> fibonacci(17)
    1597
    """
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n > 1:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    else:
        raise ValueError()

    return result


def factorial(n: int):
    """
    Returns n!
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(10)
    3628800
    """
    import functools
    return functools.reduce(lambda x, y: x * y, range(1, max(2, n + 1)))
    # Or just use math.factorial()


def get_all_subcomponents(graph):
    """
    Return a list of all the sub-components of the graph
    e.g.
    [[1,1,0],
     [1,1,0]
     [0,0,1]]
    returns [ [ 0, 1 ], [ 2 ] ]
    :param graph: [[]] list of lists representing the graph matrix
    >>> sorted([sorted(i) for i in get_all_subcomponents([[1,1,0],[1,1,0],[0,0,1]])])
    [[0, 1], [2]]
    >>> sorted([sorted(i) for i in get_all_subcomponents([[1,0,0],[0,1,0],[0,0,1]])])
    [[0], [1], [2]]
    """
    def flood(visited_array, idx, graph):
        visited_array[idx] = True
        adjacent_nodes = graph[idx]
        component = [idx]
        for other_idx, is_connected in enumerate(adjacent_nodes):
            if is_connected and not visited_array[other_idx]:
                component += flood(visited_array, other_idx, graph)
        return component

    result = []
    visited = [ False ] * len(graph)
    for node_idx in range(len(graph)):
        if not visited[node_idx]:
            result.append(flood(visited, node_idx, graph))
    return result


if __name__ == "__main__":
    doctest.testmod(name="Solutions", verbose=True)
