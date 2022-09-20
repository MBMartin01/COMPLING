def getCounts(fname: str) -> dict:
    """
    Args: 
        fname: A variable holding the name of file to read

    Returns:
        A dict mapping words (i.e. space delinated tokens by line) to its 
        frequency in a corpus. For example, 

        With a file containing:
            The cat ate the cat food.

        This should return:

            {'the': 2, 'cat': 2, 'ate': 1, 'food.': 1}

    Hints:

        For a nice introduction to python dictionaries see https://realpython.com/python-dicts/ 
        Make sure to remove new line characters. Keep punctuation.

    """
    pass


if __name__ == '__main__':

    fname = 'small_alice.txt'

    getCounts(fname)

