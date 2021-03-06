#!usr/bin/env python3
"""
counter.py

String splitting and sorting logic for a term frequency counter.

Functions
---------
split_words
    Splits a text string into component words.
count_frequency
    Term frequency counter for a list.
find_top_words
    Return the most frequent words and their counts.
"""

import re


def split_words(text):
    """Split a string into words.

    Split a Unicode string on non-alphanumeric characters.

    Parameters
    ----------
    text : string
        Unicode string containing text to be split.

    Returns
    -------
    list
        List of strings, containing individual words and word fragments
    """
    p = re.compile(r'[^a-zA-Z0-9]')  # this will split on accents and Unicode
    split_text = p.split(text)
    words = [word for word in split_text if word]  # strip empty strings
    return words


def count_frequency(words):
    """ Count term frequency in a list of words.

    Parameters
    ----------
    words : list
        A list of strings.

    Returns
    -------
    dict
        A dict mapping a lower-case string to the number of instances of
        that string in the given list.
    """
    word_count = {}
    for word in words:
        if word.lower() in word_count:  # case insensitive matching
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1
    return word_count


def find_top_words(word_count, n=10):  # would rather not hard-code but spec
                                       # said logic should return 10 words
    """Return the most frequent words from a frequency-counted dict.

    Sort through a given word:word frequency dict by value to return
    (word, frequency) tuples for the most common n words in the dict.

    Parameters
    ----------
    word_count : dict
        A dict mapping words to their frequencies (str: int).
    n : int
        The number of words to return, default 10.

    Returns
    -------
    list
        A list of tuples containing (word[string], frequency[int])
    """
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:n]


if __name__ == '__main__':
    # Small test script
    with open('tests/files/anne_of_green_gables.txt', 'r') as f:
        text = f.read()
    words = split_words(text)
    word_count = count_frequency(words)
    print(find_top_words(word_count, 10))
