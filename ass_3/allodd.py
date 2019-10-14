# Assignment 03, Task 03
# Name: Vikrom Narula
# Collaborators: None
# TimeSpent: 70:00min


def is_all_odd(lst):
    """

    >>> is_all_odd([1,2,3])
    False
    >>> is_all_odd([3,1,7])
    True
    >>> is_all_odd([])
    True
    """
    lst1 = []
    if lst == []:
        return True
    for x in lst:
        if x % 2 != 0:
            lst1.append(x)
    if len(lst1) == len(lst):
        return True
    else:
        return False


###########################################################################
# Please don't mind me living down here. I provide some initial testing for
# your code. Run me (e.g., using the run button in Spyder).
###########################################################################
# Simple Tests
###########################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
###########################################################################
